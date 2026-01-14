class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # My notes:
        # We have a string
        # Possibilities: all the same letters
        # O(n) attempt (Go through entire string once):
        """
        L = len(s)
        n = 3
        if L % 2 == 0:  #Substring repeated either odd or even times
            a = s[0: (L / 2)]  # For substing repeated even no. of times
            b = s[1: (L / 2)]  # accounts for odd no. of repititions
            return (a * 2 == s) or (b * 2 == s[1: -1])

        if L == 1:
            return False
        while L / n > 2:
            if L % n == 0 and s[:(L / n)] * n == s:
                return True
            n += 2
        return False
        """
        # Note to self, the above code doesn't actually pass all testcases
        """ Upon using AI to analyze this code, I've found that although the 
        complexity of this is O(n) x number of factors, it is significantly
        closer to O(n^2). A for loop would likely be a better choice """

        # New attempt: 

        L = len(s)
        if L % 2 == 0 and (s[: (L//2)] * 2 == s):
            return True
        for i in range(1, L, 2):
            if L % (i + 2) == 0 and s[:(L // (i + 2))] * (i + 2) == s:
                return True
        return False
        # This works! and according to leetcode, it's O(N) complexity!
        
