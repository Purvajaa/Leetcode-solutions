class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sett=set()
        for i in nums:
            sett.add(i)
        if len(sett)==len(nums):
            return False
        else:
            return True
        