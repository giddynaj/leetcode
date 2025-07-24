def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ptr1, ptr2 = 0, 0
    while ptr1 < len(nums):
        ptr2 = ptr1 + 1
        while ptr2 < len(nums):
            ptrSum = nums[ptr1] + nums[ptr2]
            if ptrSum == target:
                return [ptr1, ptr2]
            ptr2 += 1
        ptr1 += 1
    return 'No target found'

if __name__ == "__main__":
    nums = [5,4,1,55]
    target = 60
    print(twoSum(nums, target))
