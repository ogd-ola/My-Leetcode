class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if they're not the same length, early return False
        # Create two separate lists consisting of all the characters in 
        # each of the words
        # Sort the lists, if anything is unequal, early return False
        # return True
        if len(s) != len(t):
            return False
        sList = []
        tList = []
        for char in s:
            sList.append(char)
        for char in t:
            tList.append(char)
        sList.sort()
        tList.sort()
        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False
        return True
        
        
        