'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def count_unival_trees(node):
    if node.left and node.right:
        # has child nodes
        left_bool, left_tree, left_count = count_unival_trees(node.left)
        right_bool, right_tree, right_count = count_unival_trees(node.right)

        if left_bool and right_bool and node.value == left_tree and node.value == right_tree:
            return True, node.value, left_count + right_count + 1
        else:
            return False, node.value, left_count + right_count

    else:
        return True, node.value, 1

if __name__ == '__main__':
    l3 = Node(1, None, None)
    r3 = Node(1, None, None)
    l2 = Node(1, l3, r3)
    r2 = Node(0, None, None)
    r1 = Node(0, l2, r2)
    l1 = Node(1, None, None)
    n0 = Node(0, l1, r1)

    print(count_unival_trees(n0)[2])