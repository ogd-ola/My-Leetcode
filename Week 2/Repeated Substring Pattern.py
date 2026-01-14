class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Intuition:
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
        # Approach:
        """ Given a string s, first check if one half is equal to the other and return True if so
        If not, then the only condition that would result in returning True is where the valid 
        substring is repeated an odd number of times. So I'd like to have a way to keep track of this.
        So I store len(s) in L, and I use a for loop that runs on the condition that L is divisible by i 
        and that multiplying the first ith of the string by i gives s. 
        """
        L = len(s)
        if L % 2 == 0 and (s[: (L//2)] * 2 == s):
            return True
        for i in range(1, L, 2):
            if L % (i + 2) == 0 and s[:(L // (i + 2))] * (i + 2) == s:
                return True
        return False
        # This works! and according to leetcode, it's runtime is of O(N) complexity (8ms) and beats 45%
        # of solutions

        # In terms of memory, this (referring to New attempt only) has O(1) complexity and beats
        # 76.08% of solutions. Already made great progress from when I first started out
        
