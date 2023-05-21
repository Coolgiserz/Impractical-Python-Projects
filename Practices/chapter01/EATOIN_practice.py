"""
简单条形图.

pprint: 美化打印，https://docs.python.org/zh-cn/3/library/pprint.html
"""
import string
from collections import defaultdict
import pprint
def get_char_bar_chart(sentence: str):
    """
    统计输入句子中各字母的出现次数，按字母表顺序打印字母个数，以“条形图”效果展示出来.
    :param sentence:
    :return:
    """
    result = defaultdict(list)

    for char in sentence:
        if char.lower() in string.ascii_lowercase:
            result[char.lower()].append(char.lower())

    return result

if __name__ == "__main__":
    r = get_char_bar_chart("Like the castle in its corner in a medieval game, I foresee terrible trouble and I stay here just"
                           " the same.")
    # print(r)

    # 使用pprint会在输出之前为字典按键进行排序
    pprint.pprint(r)
    # pprint.pprint(sorted(r.items(), key=lambda x: x[0]))
