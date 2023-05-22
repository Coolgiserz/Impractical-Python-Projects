"""
以列表形式加载一个文本文件

参数：文本文件的名字

异常：若没有找到文件，则报告IOError类型的异常

返回值：一个包含文本文件中所有单词小写形式的列表

"""
import sys

def load(file):
    try:
        with open(file, "r") as fin:
            content = fin.read().strip().split("\n")
            # 列表推导：List Comprehension，将列表或其他可迭代对象快速转换为另一个列表的方法
            content = [w.lower() for w in content]
            return content
    except IOError as e:
        print(f"open {file} error with exception {e}")
        # 若遇到IO异常，通过sys.exit命令终止程序
        sys.exit(1)
        