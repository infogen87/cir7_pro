#leet code question 9 Palindrome Number

class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        divisor = 1
        while x // divisor >= 10:
            divisor *= 10

        while x > 0:
            left_digit = x // divisor
            right_digit = x % 10

            if left_digit != right_digit:
                return False

            x = (x % divisor) // 10
            divisor //= 100
        return True 