class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        for val in range(len(s)):
            while s[val] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[val])
            max_length = max(max_length, val - left + 1)
        return max_length