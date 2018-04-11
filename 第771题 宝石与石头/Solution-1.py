class Solution:
     def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        charDict = {}
        num = 0
        for index in range(len(S)):
            if S[index] in charDict:
                charDict[S[index]] += 1
                continue
            charDict[S[index]] = 1

        for index in range(len(J)):
            if J[index] in charDict:
                num += charDict[J[index]]
        
        return num

sol = Solution()
sol.numJewelsInStones('aA', 'aAAbbb')