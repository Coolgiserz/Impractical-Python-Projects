"""
寻找异位短语

交互型程序：根据用户输入的短语及词典支持的单词数，让用户选择易位短语的构造
"""
import sys
from collections import Counter
from Projects.project2.module.load_dictionary import load


def process_choice(name: str)->(str, str):
    """
    处理用户选择
    """
    while True:
        # 让用户选择一个可用单词
        choice = input("please choose a name.")
        if len(choice) > len(name):
            print(f"{len(choice)} exceeds limit {len(name)}")
            print("Make anathor choice.")
        elif choice == "":
            main()
        elif choice == "#":
            sys.exit()
        #     剩余的可选列表
        left_over_list = list(name)
        candidate = list(choice.lower())
        for char in candidate:
            if char in left_over_list:
                left_over_list.remove(char)
        name = ''.join(left_over_list)
        return choice, name

def find_anagrams(word: str, word_dict: [str]):
    """在字典里寻找异位短语"""
    word_letter_count = Counter(word.lower())
    anagrams = []
    for w in word_dict:
        w_letter_count = Counter(w.lower())
        remain_str_choices = ""
        for letter in w:
            # 若一个单词的所有字母出现频次都小于word中该字符出现频次，则该单词加入候选词中
            if w_letter_count[letter] <= word_letter_count[letter]:
                remain_str_choices += letter
        if w_letter_count == Counter(remain_str_choices):
            anagrams.append(w)
    print(*anagrams, sep="\n")
    print(f"Remaining letter choices: {word}")
    print(f"Optional anagrams: {len(anagrams)}")

def main():
    print("寻找异位短语")
    stop = False
    # 加载字典
    word_dict = load("../../Resources/12dicts-6.0.2/International/2of4brif.txt")
    # 用户输入一个名字
    name_init = input("Please enter a name:")

    name_limit = len(name_init)
    name = "".join(name_init.lower().split())
    print("name: ", name)
    result = ""
    while not stop:
        # 从字典里寻找可选用的单词、剩余可用字符数、可用字符
        find_anagrams(name, word_dict)

        print(f"Optional anagrams length limit: {name_limit}")
        # 处理用户选择
        choice, name= process_choice(name)
        result += choice
        name_limit = name_limit - len(choice)
        if name_limit <= 0:
            stop = True
            print(f"Result: {result}")

if __name__ == "__main__":
    main()

