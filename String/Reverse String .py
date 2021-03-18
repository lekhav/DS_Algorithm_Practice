class Solution:
    def reverseString1(self, s):
        # O(2N) time; O(N) space
        # Append all characters to a stack; Pop them and add them to result
        res = []           # EXTRA SPACE SOLUTION
        l = len(s)
        for i in range(l):
            res.append(s.pop())

        return res


    def reverseString2(self, s):
        # 2 Pointer Approach, 
        # O(N) time ; O(1) space
        l = 0
        r = len(s)-1
        while l < r:
            # temp = s[l]  
            # s[l] = s[r]
            # s[r] = temp
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

        return s

    def reverseString3(self, s):
        # Recursive stack approach
        # O[N] Time, O[N] Stack-Space
        return self.helper(s, [])
    def helper(self, s, result):
        if len(s) == 0:
            return result
        result += [s[-1]]
        self.helper(s[:len(s)-1], result)

        



obj = Solution()
print(obj.reverseString1(s= ['h', 'e', 'l', 'l', 'o']))
print(obj.reverseString2(s= ['h', 'e', 'l', 'l', 'o']))
print(obj.reverseString3(s= ['h', 'e', 'l', 'l', 'o']))