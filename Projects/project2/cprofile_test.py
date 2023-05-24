"""
通过CProfile测试find_palindrome的性能
cProfile（一个C语言扩展程序）适合对长时间运行的程序进行性能分析
"""
import cProfile
import find_palindrome
cProfile.run("find_palindrome.find_palindrome()")