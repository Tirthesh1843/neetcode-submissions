class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicat = []
        result = False
        for i in nums:
            if i in duplicat:
                return True
            duplicat.append(i)
        return result