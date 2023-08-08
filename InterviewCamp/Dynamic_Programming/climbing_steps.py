from typing import List, Dict


def bottom_up_approach(final_step_number: int, steps_allowed: List[int]) -> int:
    """
    Tabulation method to approach the question
    Permutations
    :time_complexity: O(nx3) = O(n)
    :space_complexity: O(n)
    :param: final_step_number: int
    :param: steps_allowed: List[int]
    :rtype: int, number of possibilities
    """
    if final_step_number < 1 or final_step_number is None or len(steps_allowed) < 1:
        return -1

    number_of_steps_array: List[int] = [0] * (final_step_number + 1)
    number_of_steps_array[0] = 1

    for i in range(len(number_of_steps_array)):
        for step in steps_allowed:
            if i + step > final_step_number:
                continue
            number_of_steps_array[i + step] += number_of_steps_array[i]
    print(number_of_steps_array)
    return number_of_steps_array[-1]


def top_down_approach(final_step_number: int, steps_allowed: List[int], step_count_dict: Dict[int, int]) -> int:
    """
    Permutations: sequence matters
    :time_complexity: O(n)
    :space_complexity: O(n)
    :param final_step_number: int
    :param steps_allowed: List[int]
    :param step_count_dict: Dict[int, int]
    :return: int, number of possibilities
    """
    if final_step_number == 1 or final_step_number == 0:
        return 1

    if final_step_number is None or final_step_number < 0:
        return -1

    if final_step_number in step_count_dict:
        return step_count_dict[final_step_number]

    for step in steps_allowed:
        if final_step_number - step >= 0:
            if final_step_number in step_count_dict:
                step_count_dict[final_step_number] += top_down_approach(final_step_number - step,
                                                                        steps_allowed, step_count_dict)
            else:
                step_count_dict[final_step_number] = top_down_approach(final_step_number - step,
                                                                       steps_allowed, step_count_dict)
        # print(step_count_dict)

    return step_count_dict[final_step_number]


if __name__ == "__main__":

    print(bottom_up_approach(8, [1, 3, 5]))
    print(top_down_approach(5, [1, 3, 5], {}))
