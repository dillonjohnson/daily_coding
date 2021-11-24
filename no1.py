"""
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


# Easy solution
def find_matched_sum(li_nums, goal_num):
    for i in li_nums:
        for j in li_nums:
            if i + j == goal_num:
                return True
    return False


def find_matched_sum_single(li_nums, goal_num):
    visited = set()
    for i in li_nums:
        if goal_num - i in visited:
            return True
        visited.add(i)
    return False


if __name__ == '__main__':
    assert find_matched_sum([10, 15, 3, 7], 17)
    assert find_matched_sum_single([10, 15, 3, 7], 17)
    assert not find_matched_sum([10, 15, 3, 7], 27)
    assert not find_matched_sum_single([10, 15, 3, 7], 27)
