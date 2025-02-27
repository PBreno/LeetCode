
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        soma = 0
        soma_array = []
        for i in range (0, len(nums)):
            soma += nums[i]
            soma_array.append(soma)
        return soma_array
    
# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == "__main__":
    s = Solution()
    print (s.runningSum(([1,2,3,4],)))