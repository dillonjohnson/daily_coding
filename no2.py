'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''


def transform(arr):
    # could either divide by the one at i
    # Or we can multiply all except the one, O(n^2)
    out = []
    for idx, item in enumerate(arr):
        product = 1
        for idx2, j in enumerate(arr):
            if idx != idx2:
                product *= j
        out.append(product)
    return out


if __name__ == '__main__':
    inp = [1, 2, 3, 4, 5]
    print(transform(inp))
