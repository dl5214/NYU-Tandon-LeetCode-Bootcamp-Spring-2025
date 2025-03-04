from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]
        answer = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            j = len(nums) - i - 1
            suffix[j] = nums[j+1] * suffix[j+1]
        for k in range(len(nums)):
            answer[k] = prefix[k] * suffix[k]
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))