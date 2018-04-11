class Solution:
     def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(j) for j in J)

sol = Solution()
count = sol.numJewelsInStones('aAb', 'aAAbbb')
print(count)