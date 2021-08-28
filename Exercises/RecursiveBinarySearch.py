import random

def binary_search(nums, key):
    return binary_search_helper(nums, key, 0, len(nums))
    
def binary_search_helper(nums, key, start_idx, end_idx):
    middle_idx = (start_idx + end_idx) // 2
    if start_idx == end_idx:
        return False
    if nums[middle_idx] > key:
        return binary_search_helper(nums, key, start_idx, middle_idx)
    elif nums[middle_idx] < key:
        return binary_search_helper(nums, key, middle_idx + 1, end_idx)
    else:
        return True


if __name__ == '__main__':
    list_size = int(input('how big is the list '))
    target = int(input('Which number do you want to find? '))

    list = sorted([random.randint(0, 100) for i in range(list_size)])

    result = binary_search(list, target)

    print(list)
    print(f'the element {target} {"is" if result else "is not"} in the list ')