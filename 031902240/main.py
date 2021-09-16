# !/usr/bin/env python
# -*- coding:utf-8 -*-
import re

path1 = input()
path2 = input()
path3 = input()
total = 0
file = open(path2, 'rt', encoding='utf-8')
answer = open(path3, 'wt', encoding='utf-8')
answer.write('                                                           \n')


def write_to_ans(data_list, num, line):  # 将每行读出的敏感词答案写到列表中
    global total
    for item in data_list:
        total = total + 1
        answer.write("Line:" + str(num) + " <" + item + "> " + item + '\n')
    return line


def start_to_find(path):  # 将单词文档读入到列表当中
    with open(path, 'rt', encoding='utf-8') as file1:
        word_list = list()
        for line in file1.readlines():
            if line is not None:
                word_list.append(line.strip('\n'))
    return word_list


def english(line, item, num):
    if item.islower():  # 判断所有字符都是小写
        s = item[0].upper()
        data_list1 = re.findall(s + ".+?" + item[-1], line)  # 大写小写型
        if data_list1:
            line = write_to_ans(data_list1, num, line)
        s = item[-1].upper()
        data_list2 = re.findall(item[0] + ".?" + s, line)  # 小写大写型
        if data_list2:
            line = write_to_ans(data_list2, num, line)
        data_list3 = re.findall(item[0].upper() + ".?" + item[-1].upper(), line)  # 大写大写型
        if data_list3:
            line = write_to_ans(data_list3, num, line)
    return line


def instr(item, line_num, line):  # 中间有字符串的情况
    global total
    data_list = re.findall(item[0] + ".+?" + item[-1], line)
    if data_list:
        for case1 in data_list:
            total = total + 1
            num_str = str(line_num)
            answer.write("Line:" + num_str + " <" + item + "> " + case1 + '\n')

    return line


def directly(item, line_num, line):  # 直接删除有对应的单词
    global total
    data_list = re.findall(item, line)
    line = re.sub(item, "", line)  # 找到相匹配的单词并且删
    if data_list:
        for case in data_list:
            total = total + 1
            num_str = str(line_num)
            answer.write("Line:" + num_str + " <" + item + "> " + case + '\n')
    return line


def serach_sensitive_word(path5):  # 寻找敏感词
    word_list = start_to_find(path5)
    line_num = 0
    for line in file:  # 每行的读取
        line_num = line_num + 1
        for item in word_list:
            line = directly(item, line_num, line)
            line = instr(item, line_num, line)
            if item.encode('UTF-8').isalpha():  # 判断中英文单词
                line = english(line, item, line_num)


def main():
    serach_sensitive_word(path1)
    answer.seek(0)
    s1 = str(total)
    answer.write("Total: " + s1)


if __name__ == '__main__':
    main()
file.close()
answer.close()
