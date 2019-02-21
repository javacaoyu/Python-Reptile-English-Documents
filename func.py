# coding:utf8

import requests


def is_effective_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response
    return False


def get_novel_name_by_response(response):
    response.encoding = requests.utils.get_encodings_from_content(response.text)[0]
    content = response.text
    content = content[content.find('<a href="list.html" id="zhangxu">'):]
    end = content.find('</a></h1>')
    start = content.find('>')
    return content[start + 1: 52]

def get_novel_name_by_url(url):
    response = requests.get(url)
    return get_novel_name_by_response(response)


def get_chapter_list(url):
    response = requests.get(url)
    response.encoding = requests.utils.get_encodings_from_content(response.text)[0]
    content = response.text
    for line in content.split('\n'):
        if line.__contains__('title=') and line.__contains__('<li>'):
            href = line[line.find('href=') + 6:]
            href = href[:href.find('"')]
            title = line[line.find('title=') + 7:]
            title = title[:title.find('"')]
            print(href, title)
    # chapters = list()
    # while True:
    #     if content.find('title=') == -1:
    #         break
    #     content = content.find('title=')


url = 'http://novel.tingroom.com/shuangyu/2013/list.html'
# url = 'http://novel.tingroom.com/ertong/2842'
print(get_chapter_list(url))