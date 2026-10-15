class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicat = set()
        result = False
        for i in nums:
            if i in duplicat:
                return True
            else:
                duplicat.add(i)
        return False