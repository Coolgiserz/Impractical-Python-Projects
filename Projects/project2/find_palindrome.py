"""
寻找文件中的回文单词
    sos
    nan
    mom
    sees
    radar
伪代码：
1. 以列表形式将文件中的单词加载到内存中
2，数据预处理（统一转小写/大写）
3. 遍历单词列表，判断其是否是回文单词；若是，添加到结果列表中。
4. 输出回文单词列表

"""

from module import load_dictionary

def is_palindrome(word):
    return word==word[::-1]

def find_palindrome():
    words = load_dictionary.load("../../Resources/12dicts-6.0.2/International/2of4brif.txt")
    result = []
    for word in words:
        if len(word)>1 and is_palindrome(word):
            result.append(word)
    # print(f"find {len(result)} palindrome.")
    # sep参数设置数据之间的分隔符，默认是" "
    print(*result, sep="\n")

def is_palindrome_recursion(word):
    wlen = len(word)
    if wlen <=1 :
        return True
    if word[0] == word[wlen-1]:
        return is_palindrome_recursion(word[1:wlen-1])
    else:
        return False
