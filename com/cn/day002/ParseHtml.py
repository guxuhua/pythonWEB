# -*- coding:utf-8 -*-
# 解析html文件
"""解析给定的html文件"""
# 单独处理：handle_starttag( tag, attrs)、handle_startendtag( tag, attrs)、handle_endtag( tag)
from HTMLParser import HTMLParser
class MyHtmlParse(HTMLParser): #继承自HTMLParser
    def __init__(self):
        HTMLParser.__init__(self)
        self.link = [] # 存放所有的链接

    def handle_starttag(self, tag, attrs):
        print ">>>>>开始处理开始标签<<<<<"
        if tag == "a":
            if len(attrs)==0:
                pass
            else:
                for (variable,value) in attrs:
                    if variable == "href":
                        self.link.append(value)

if __name__ == "__main__":
    print ">>>>>自身开始执行<<<<<"
    html_code = """
        <a href="www.google.com"> google.com</a>
        <A Href="www.pythonclub.org"> PythonClub </a>
        <A HREF = "www.sina.com.cn"> Sina </a>
        """
    mp = MyHtmlParse()
    mp.feed(html_code)
    mp.close()
    print mp.link
