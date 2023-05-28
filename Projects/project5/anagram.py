"""可以借助Counter类实现寻找易位词
两个易位词构造的Counter对象逻辑相等（各字符出现频率一样，是一个相等的字典对象）
Counter的__eq__方法
"""
from collections import Counter
def is_anagram(word1, word2)->bool:
    """
    判断两个单词是否互为易位词
    """
    if len(word1)!=len(word2):
        return False
    return Counter(word1)==Counter(word2)

if __name__ == "__main__":
    cases = [
        ("good", "oodg"),
        ("power", "enger"),
        ("operw", "power")
    ]

    for case in cases:
        print(is_anagram(case[0], case[1]))