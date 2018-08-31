'''
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

Subscribe to see which companies asked this question

Runtime: 772 ms
'''
class Solution(object):
    def permute(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res
            
if __name__=="__main__":
    nums = [1,2,3,4,5]
    print Solution().permute(nums)
    print "total permutation: ", len(Solution().permute(nums)) # 5!
