"""
通过CProfile测试find_palindrome的性能
"""
import cProfile
import find_palindrome
cProfile.run("find_palindrome.find_palindrome()")