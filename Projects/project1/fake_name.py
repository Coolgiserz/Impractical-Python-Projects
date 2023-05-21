"""
生成假名.

给定姓、名，随机组合成姓名
"""
import random
import sys

first_names = ("赵", "钱", "孙", "李", "张", "廖")
second_names = ("灵儿", "中达", "四喜", "益达", "光前")

class NameGenerator():
    """
    姓名生成器.
    """
    name_set = set()
    @staticmethod
    def generate_name():
        """
        随机生成一个姓名
        :return:
        """
        first_name = random.choice(first_names)
        second_name = random.choice(second_names)
        return f"{first_name}{second_name}"

    @staticmethod
    def run(time_=100):
        """批量生成姓名"""
        for _ in range(time_):
            name = NameGenerator.generate_name()

            if name not in NameGenerator.name_set:
                NameGenerator.name_set.add(name)
                print(NameGenerator.generate_name(), file=sys.stderr)
            else:
                continue

# __name__是一个特殊的内置变量，用于判断程序是独立运行（此时__name__等于__main__)还是以导入其他程序的方式运行
if __name__ == "__main__":
    NameGenerator.run(20)
