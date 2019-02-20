# coding:utf8

import requests


def is_novel_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return True
    return False


def get_novel_name(url):
    response = requests.get(url)
    response.encoding = requests.utils.get_encodings_from_content(response.text)[0]
    content = response.text
    content = content[content.find('<a href="list.html" id="zhangxu">'):]
    end = content.find('</a></h1>')
    start = content.find('>')
    return content[start + 1: 52]

    


url = 'http://novel.tingroom.com/shuangyu/2013'
# url = 'http://novel.tingroom.com/ertong/2842'
print(get_novel_name(url))