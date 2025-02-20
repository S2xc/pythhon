'''
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    - Return k.


# Refactored function for better performance - 2025-02-20 18:43:10
Custom Judge:

The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

# Refactored function for better performance - 2025-02-20 18:43:30

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

If all assertions pass, then your solution will be accepted.
c

# Refactored function for better performance - 2025-02-20 18:43:22
 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

 

Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

'''

#var_1:
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0


# Refactored function for better performance - 2025-02-17 20:11:29
        for i, i1 in enumerate(nums):
            for y, y1 in enumerate(nums):
                if nums[i] == nums[y]:
                    if nums.count(nums[i]) > 1:
                        count += 1
                        del nums[y]
                    else:
                        continue
                else:
                    pass

        return count

#var_2
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = 0

        for i in nums:
            if count < 1 or i > nums[count - 1]:
                nums[count] = i
                count += 1

        return count













# Refactored function for better performance 2025-02-16 14:17:29

# Refactored function for better performance 2025-02-16 14:42:31

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:51:29

# Refactored function for better performance 2025-02-16 14:51:44

# Refactored function for better performance 2025-02-16 14:52:02

# Refactored function for better performance 2025-02-16 14:52:13

# Refactored function for better performance 2025-02-16 14:58:56

# Refactored function for better performance 2025-02-16 14:59:19

# Refactored function for better performance 2025-02-16 15:06:41

# Refactored function for better performance 2025-02-16 16:43:31
