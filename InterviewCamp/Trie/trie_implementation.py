from typing import Dict, List, Optional


class Node:
    def __init__(self):
        self.__is_word:bool = False
        self.__map:Dict[str, 'Node'] = dict()

    def get_is_word(self):
        return self.__is_word

    def set_is_word(self, is_word: bool):
        self.__is_word = is_word

    def contains(self, char:str):
        return char in self.__map

    def add_node(self, char:str):
        if char not in self.__map:
            self.__map[char] = Node()

    def get_node(self, char:str):
        return self.__map[char]

    def get_map(self):
        return self.__map


class Trie:
    def __init__(self):
        self.__root:Node = Node()

    # Insertion
    def insert(self, word:str):

        current_node = self.__root

        for char in word:
            if not current_node.contains(char):
                current_node.add_node(char)

            current_node = current_node.get_node(char)

        current_node.set_is_word(True)

    # Searching
    def has_prefix(self, prefix:str):
        current_node = self.__root

        for char in prefix:
            if not current_node.contains(char):
                return False
            else:
                current_node = current_node.get_node(char)

        return True

    def has_word(self, word:str):
        current_node = self.__root

        for char in word:
            if not current_node.contains(char):
                return False
            else:
                current_node = current_node.get_node(char)

        return current_node.get_is_word()

    # Deletion
    def delete(self, word:str):
        if word is None or word == "":
            return

        last_node:Node = self.get_last_node(word)

        # check if last node is_word is true: if not, the word not found
        # if found, send ius_word as false

        if last_node is None or not last_node.get_is_word():
            return

        last_node.set_is_word(False)
        # check if the last node has children, if yes, do not delete the node,
        # else delete the last node with no children

        if len(last_node.get_map()) > 0:
            return

        self.remove_last_node_with_multiple_children(word)

    def get_last_node(self, word):
        current_node = self.__root

        for char in word:
            if not current_node.contains(char):
                return
            else:
                current_node = current_node.get_node(char)

        return current_node

    def remove_last_node_with_multiple_children(self, word):
        current_node = self.__root
        last_node_with_multiple_children:Optional[Node] = None
        child_to_remove = 0

        for i in range(len(word)-1):
            if not current_node.contains(word[i]):
                return
            current_node = current_node.get_node(word[i])

            if len(current_node.get_map()) > 0 or current_node.get_is_word():
                last_node_with_multiple_children = current_node
                child_to_remove = word[i+1]

        # if deleting all child nodes after the last parent with multiple children
        # if no parent has multiple children, the word is a single chain, hence removing the word from the root
        if last_node_with_multiple_children is not None:
            last_node_with_multiple_children.get_map().pop(child_to_remove)
        else:
            self.__root.get_map().pop(word[0])


if __name__ == "__main__":
    my_trie:Trie= Trie()

    my_trie.insert("dog")
    my_trie.insert("cat")
    my_trie.insert("done")
    my_trie.insert("dot")
    my_trie.insert("don")
    my_trie.insert("dots")
    my_trie.insert("does")

    print(my_trie.has_prefix("dog"))
    print(my_trie.has_prefix("dodg"))
    print(my_trie.has_prefix("c"))
    print(my_trie.has_word("cat"))
    print(my_trie.has_word("do"))

    my_trie.delete("done")
    print(my_trie.has_word("done"))
    print(my_trie.has_word("don"))

    my_trie.delete("cat")
    print(my_trie.has_word("cat"))
    my_trie.delete("does")
    print(my_trie.has_word("does"))
    print(my_trie.has_word("dots"))
