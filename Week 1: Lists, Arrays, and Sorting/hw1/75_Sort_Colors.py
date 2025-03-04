from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                ones += 1
            else:
                twos += 1
        for j in range(zeros):
            nums[j] = 0
        for j in range(zeros, zeros + ones):
            nums[j] = 1
        for j in range(zeros + ones, zeros + ones + twos):
            nums[j] = 2


if __name__ == "__main__":
    solution = Solution()
    array1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(array1)
    array2 = [2, 0, 1]
    solution.sortColors(array2)
    print(array1)
    print(array2)
