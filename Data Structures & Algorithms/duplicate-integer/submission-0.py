class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=1
            elif dic[i]>1:
                return True
            dic[i]=dic[i]+1
        return False
        