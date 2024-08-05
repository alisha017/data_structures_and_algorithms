def print_subsets_of_array(a, buffer_, start_index, buffer_index):
    # 1 termination case - buffer full
    print(buffer_[: buffer_index])

    if buffer_index == len(buffer_) or start_index == len(a):
        return

    # 2 find candidates
    for i in range(start_index, len(a)):
        # 3 place item into buffer index
        buffer_[buffer_index] = a[i]
        # 4 recurse to next index
        print_subsets_of_array(a, buffer_, i+1, buffer_index+1)


if __name__ == "__main__":
    a = [1,2,3,4]
    buffer_ = [None, None, None, None]
    start_index = 0
    buffer_index = 0
    print(print_subsets_of_array(a, buffer_, start_index, buffer_index))