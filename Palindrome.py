"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""
class Solution:
	def isPalindrome(self, x):
		digits=[number for number in str(x)]
		for i in range(len(digits)):
			if digits[i]!=digits[-(i+1)]:
				return False
			else:
				result="Palindrome"
		return True