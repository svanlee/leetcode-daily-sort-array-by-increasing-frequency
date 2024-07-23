from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        frequency_count = {}
        for num in nums:
            frequency_count[num] = frequency_count.get(num, 0) + 1

        # Sort the numbers by frequency and value
        sorted_numbers = sorted(nums, key=lambda x: (frequency_count[x], -x))

        return sorted_numbers