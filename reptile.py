# coding:utf8
import requests
import func

__author__ = 'CaoYu'

host = 'novel.tingroom.com'
types = ['jingdian', 'shuangyu', 'mingren', 'lizhi', 'duanpian', 'kehuan', 'ertong']
used = dict()
page_num = 1
max_page = 1000000
novel_num = 1
max_novel = 100000

# Init used
for t in types: used[t] = list()


# Start
for t in types:
    while True:
        if novel_num > max_novel:
            print("Max novel over on " + str(max_novel) + ", finish this type of " + t)
            break
        




        novel_num += 1
    
