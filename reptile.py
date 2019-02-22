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
    print('Preparing gather type of: ' + t + '.......')
    while True:
        print('---------------------')
        if novel_num > max_novel:
            print("Max novel over on " + str(max_novel) + ", finish this type of " + t)
            break
        if t + "_" + str(novel_num) in used.keys():
            sp = used[t + "_" + str(novel_num)].split('|||')
            title = sp[0]
            url = sp[1]
            print("This novel has been gathered, skip it, title is: " + title + ', url is: ' + url)
            continue
        url = 'http://' + host + '/' + t + '/' + str(novel_num)
        response = func.is_effective_page(url)
        if response:
            title = func.get_novel_name_by_response(response)
            print("Found a active page, title is: " + title + ', url: ' + url + ', preparing gather it.')
            chapters = func.get_chapter_list(url + '/list.html')
            for chapter in chapters.keys():
                print('Preparing gather chapter: ' + chapter + ' of novel: ' + title + '......')
                content = func.get_content(url + '/' + chapters[chapter])
                f_name = func.write_to_file(content, title, chapter)
                print(title + "'s chapter: " + chapter + ' is already writed to file: ' + f_name)
                print('Go to next.......')
        novel_num += 1
    print('Type of ' + t + ' has already gathered. Go to next type.......')
print('All type are already gathered.')
