from typing import Optional, List, Dict


class TreeNode:
    def __init__(self, value: int, right: Optional['TreeNode'] = None,
                 left: Optional['TreeNode'] = None):
        self._value: int = value
        self.__right_node: Optional['TreeNode'] = right
        self.__left_node: Optional['TreeNode'] = left
        self.__visited: bool = False

    def get_node_value(self):
        return self._value

    def get_right_node(self):
        return self.__right_node

    def get_left_node(self):
        return self.__left_node

    def is_visited(self):
        return self.__visited

    def set_node_value(self, val: int):
        self._value = val

    def set_right_node(self, new_right: 'TreeNode'):
        self.__right_node = new_right

    def set_left_node(self, new_left: 'TreeNode'):
        self.__left_node = new_left

    def set_visited(self, new_visited):
        self.__visited = new_visited


def inorder_tree_traversal(root: TreeNode):
    stack = []
    node = root
    stack.append(node)
    inorder_list = []

    while len(stack) > 0:
        current_node = stack.pop(-1)
        if current_node.is_visited() is True:
            inorder_list.append(current_node.get_node_value())
        else:
            current_node.set_visited(True)
            if current_node.get_right_node() is not None:
                stack.append(current_node.get_right_node())
            stack.append(current_node)
            if current_node.get_left_node() is not None:
                stack.append(current_node.get_left_node())
    return inorder_list


# maintaining indices because sending a sliced list will not retain the original info since lists are immutable
def construct_tree_preorder(in_start: int, in_end: int, inorder_arr: List[int],
                            pre_start: int, pre_end: int, preorder_arr: List[int]):
    print("****" * 20)

    # exit condition
    if (pre_start > pre_end or in_start > in_end) or pre_start >= len(preorder_arr) or in_start >= len(inorder_arr):
        return None

    # getting the root from the preorder array
    print(f"pre_start:{pre_start}, pre_end:{pre_end}, in_start:{in_start}, in_end:{in_end}")
    root_val = preorder_arr[pre_start]
    root_node = TreeNode(root_val)

    root_index_inorder = inorder_arr.index(root_val)
    print(f"root_val:{root_val}, root_index_inorder:{root_index_inorder}")

    # indices for preorder and inorder arrays for left and right subtrees
    left_in_start, left_in_end = in_start, root_index_inorder
    right_in_start, right_in_end = root_index_inorder + 1, in_end

    left_pre_start, left_pre_end = pre_start + 1, pre_start + root_index_inorder - in_start
    right_pre_start, right_pre_end = pre_start + root_index_inorder - in_start + 1, pre_end

    print(f"left_in_start:{left_in_start}, left_in_end:({left_in_end} "
          f"--> {inorder_arr[left_in_start:left_in_end]} ,"
          f"\nleft_pre_start:{left_pre_start}, left_pre_end:{left_pre_end} "
          f"--> {preorder_arr[left_pre_start:left_pre_end]} ")
    print(f"right_in_start:{right_in_start}, right_in_end:{right_in_end} "
          f"--> {inorder_arr[right_in_start:right_in_end]},"
          f"\nright_pre_start:{right_pre_start}, right_pre_end:({right_pre_end} "
          f"--> {preorder_arr[right_pre_start:right_pre_end]} ")

    # set left and right nodes and return root
    root_node.set_left_node(
        construct_tree_preorder(left_in_start, left_in_end, inorder_arr, left_pre_start, left_pre_end, preorder_arr))

    print(f"---- left node set ------")
    # print(f"{root_node.get_node_value()}-->{root_node.get_left_node().get_node_value()}")
    root_node.set_right_node(
        construct_tree_preorder(right_in_start, right_in_end, inorder_arr, right_pre_start, right_pre_end,
                                preorder_arr))
    print(f"-----right node set -----")
    # print(f"{root_node.get_node_value()} -->{root_node.get_right_node().get_node_value()}")
    return root_node


def construct_tree(inorder_arr: List[int], preorder_arr: List[int]):
    return construct_tree_preorder(0, len(inorder_arr), inorder_arr, 0, len(preorder_arr), preorder_arr)


if __name__ == "__main__":
    inorder = [1, 2, 3, 4, 5, 6, 7]
    preorder = [4, 2, 1, 3, 6, 5, 7]

    root = construct_tree(inorder, preorder)
    print(root.get_node_value())
    print(inorder_tree_traversal(root))

    inorder = [4,2,5,1,6,3,7]
    preorder = [1,2,4,5,3,6,7]

    root = construct_tree(inorder, preorder)
    print(root.get_node_value())
    print(inorder_tree_traversal(root))
