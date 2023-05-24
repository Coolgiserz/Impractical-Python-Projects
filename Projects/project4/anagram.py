"""寻找单词的易位词
易位词：重新排列单词的字母顺序形成的新单词

1. 判断某个单词是否存在易位词
2. 判断某个短语是否存在易位短语

应用场景：
解谜，易位词游戏Jumble: https://www.jumble.com

advice：利用伪代码进行编码规划有助于发现程序中存在的潜在问题，越早发现问题越能节省时间
"""

from typing import List
def is_anagram(word: str, other: str)->bool:
    """判断两个单词是否互为易位词
     >>> is_anagram("stop", "pots")
     True
     >>> is_anagram("asda", "sa")
     False
     >>> is_anagram("stop", "otps")
     True
    """
    if len(word) != len(other):
        return False
    return sorted(list(word))==sorted(list(other))


from Projects.project2.module import load_dictionary
def find_anagram(word)->List[str]:
    """寻找易位词实现一
    1. 获取用户输入，对用户输入进行排序
    2. 加载词典中的所有单词到列表中
    3. 对遍历列表中每个单词，判断其是否是用户输入词的易位词
    4. 若是，输出之
    """

    word_list = load_dictionary.load(file="../../Resources/12dicts-6.0.2/International/2of4brif.txt")
    result = []
    for w in word_list:
        flag = is_anagram(word, w)
        if flag:
            result.append(w)
    if len(result) == 0:
        print("I'm sorry but...")
    return result


def main():
    word = str(input("Please input a word"))
    print(find_anagram(word))

if __name__ == "__main__":
    # 文档内联测试：无需开发或维护单独的测试套件，只需要在函数、类或者模块中组合代码测试即可
    import doctest
    doctest.testmod(verbose=True)

    main()