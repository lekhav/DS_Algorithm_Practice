class Solution:
    def calculate(self, s):
        res = 0
        st = []
        num, sign = 0, +1

        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == '+':
                res += sign*num
                num, sign = 0, +1
            elif ch == '-':
                res += sign*num
                num, sign = 0, -1
            elif ch == '(':
                st.append(res)
                st.append(sign)
                res = 0
                sign = +1
            elif ch == ')':
                res += sign*num
                res *= st.pop()
                res += st.pop()
                num, sign = 0, +1
        return res+(sign*num)
