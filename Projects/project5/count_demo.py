"""

Counter类，统计数据项出现的次数
"""
from collections import Counter

test_list = ["牛奶", "咖啡", "白糖", "红酒", "符号", "书面文化", "咖啡"]
count = Counter(test_list)
print(count)

# Counter({'咖啡': 2, '牛奶': 1, '白糖': 1, '红酒': 1, '符号': 1, '书面文化': 1})