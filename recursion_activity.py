def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


def find_largest(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty")
    if len(arr) == 1:
        return arr[0]

    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    return largest_rest


def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    return count_number(arr[1:], target)


print("1. Sum the Array")
print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4]))
print(sum_array([-2, 5, -3, 6]))

print("\n2. Find the Largest Number")
print(find_largest([8]))
print(find_largest([9, 2, 5, 12, 4]))
print(find_largest([1, 3, 7, 10]))
print(find_largest([-5, -2, -9, -1]))

print("\n3. Count a Chosen Number")
print(count_number([], 5))
print(count_number([2, 5, 5, 3, 5, 1], 5))
print(count_number([1, 2, 3, 4], 7))
