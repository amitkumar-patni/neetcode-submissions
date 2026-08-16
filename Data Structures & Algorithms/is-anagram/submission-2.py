class Solution:
    def WordCount(self,s,t):
        s_count = {}
        t_count = {}
        for i in s:
            if i in s_count:
                s_count[i] += 1
            else:
                s_count[i] = 1
        for j in t:
            if j in t_count:
                t_count[j] += 1
            else:
                t_count[j] = 1
        if s_count == t_count:
            return True
        else:
            return False

    def isAnagram(self, s: str, t: str) -> bool:
        word_count = self.WordCount(s,t)
        if len(s) == len(t) and set(s) == set(t) and word_count:
            return True
        else:
            return False
