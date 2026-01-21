class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {')': '(', '}':  '{', ']':  '['}

        for i in s:
            if i in pairs.values():
                st.append(i)
            elif i in pairs:
                if not st or st[-1] != pairs[i]:
                    return False
                st.pop()
        return len(st)== 0

         