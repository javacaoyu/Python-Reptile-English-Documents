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
    return content[start + 1: end]

def get_novel_name_by_url(url):
    response = requests.get(url)
    return get_novel_name_by_response(response)


def get_chapter_list(url):
    chapter = dict()
    response = requests.get(url)
    response.encoding = requests.utils.get_encodings_from_content(response.text)[0]
    content = response.text
    for line in content.split('\n'):
        if line.__contains__('title=') and line.__contains__('<li>'):
            href = line[line.find('href=') + 6:]
            href = href[:href.find('"')]
            title = line[line.find('title=') + 7:]
            title = title[:title.find('"')]
            if is_include_Chinese(title):
                continue
            chapter[title] = href
    return chapter
    # chapters = list()
    # while True:
    #     if content.find('title=') == -1:
    #         break
    #     content = content.find('title=')



def is_pass(line):
    for i in passs:
        if line.__contains__(i):
            return True
    return False

passs = ['<script ', '<div ']
endis = '<table'
replaces = ['&quot;', '&nbsp;', '<div>', '</div>', '<br type="_moz" />', '</script>',
            """<br />\r""", """class="text" id="tt_text">  \r""", """\r""", """\ue4d1 """, 
            """.""", """?""", """,""", """:""", '"', '!', '<br><br>', '-', ')', '(', 
            """<p>""", """</p>"""]

def get_content(url):
    content = list()
    response = requests.get(url)
    try:
        response.encoding = requests.utils.get_encodings_from_content(response.text)[0]
    except IndexError as e:
        print(e)
        print("Get response charset has error, skip this chapter.")
        return content

    text = response.text
    text = text[text.find('class="text" id="tt_text"'):]
    comment_start = False
    for line in text.split('\n'):
        if is_pass(line): continue
        if line.__contains__('<!--'):
            comment_start = True
        if comment_start:
            if line.__contains__('-->'):
                comment_start = False
            continue
        if line.find(endis) >= 0:
            # line = line[:line.find('<')]
            # line = line.lower()
            # for s in replaces:
            #     line = line.replace(s, '')
            # content.append(line)
            # content.append('xczxcsagfasfasgfafasfasfadsfasfasfasfasfasfasdfasdfasfsdasdfasfasaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            break
        line = line.lower()
        line = line.lstrip()
        for s in replaces:
            line = line.replace(s, '')
        if line.__eq__(''):
            continue
        content.append(line)
        
    return content


def write_to_file(content, title, chapter):
    title = title.replace(' ', '_')
    chapter = chapter.replace(' ', '_')
    f_name = 'novel/' + title + '-----' + chapter + '.txt'
    with open(f_name, 'w') as f:
        for line in content:
            f.write(line)
            f.write('\n')
        f.flush()
    return f_name


def is_include_Chinese(title):
    for i in range(0, len(title)):
        if title[i] >= u'\u4e00' and title[i] <= u'\u9fa5':
            return True
    
    return False

# url = 'http://novel.tingroom.com/shuangyu/2013/57362.html'
# # url = 'http://novel.tingroom.com/ertong/2842'
# print(get_content(url))