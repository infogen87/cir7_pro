#leetcode 3042. Count Prefix and Suffix Pairs I

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        n = len(words)
        ans = 0
        for i in range(n):
            s1 = words[i]
            length_s1 = len(s1)
            for j in range(i + 1, n):
                s2 = words[j]
                if len(s2) >= length_s1 and s2.startswith(s1) and s2.endswith(s1):
                    ans += 1
        return ans