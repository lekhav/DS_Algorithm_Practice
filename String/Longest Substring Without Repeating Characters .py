class Solution:
    # BRUTEFORCE TLE
    # Time: O[N*N*N] 
    # Space: O[26] for set

    def lengthOfLongestSubstring(self, s):
        maxLen = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i:j]
                if self.isValid(substring):
                    maxLen = max(maxLen, len(substring))
        return maxLen

    def isValid(self, substring):
        visited = set()
        for i in range(len(substring)):
            if substring[i] in visited:
                return False
            visited.add(substring[i])
        return True



    # -------------------------------------------------------------
    # OPTIMIZED - SLIDING WINDOW APPROACH
    # O[N] Time; O[N] Sapce for HashMap

    # initiate a SLOW and FAST pointer, move FAST pointer untill you can make a window of all unique ch
    # ---------DUPLICATE is Found---------
    # MOVE SLIDING WINDOW, by moving the SLOW and FAST pointer
    # check for other possibilites by taking in the current FAST element 
    # as we have seen the case with the previous duplicate element, 
    # ---- SLOW should move to include the current fast character in our window ----


    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0
        maxLen = 0
        d = {}
        slow = 0
        for fast in range(len(s)):
            if s[fast] not in d:
                d[s[fast]] = fast
            else:
                slow = max(slow, d[s[fast]]+1)
                d[s[fast]] = fast
            maxLen = max(maxLen, fast+1-slow)
        return maxLen