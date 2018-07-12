# -*- coding:utf-8 -*-
# 读取html文件内容:获取a标签和img标签的属性内容
from HTMLParser import HTMLParser
class MyHtmlParser(HTMLParser):
    """自定义html文件解析器：解析指定的a标签和img标签的属性内容"""
    def __init__(self):
        HTMLParser.__init__(self) #调用父类方法，需要带上self
        self.HrefValues = [] #存放所有a标签的href属性值
        self.ImgValues = [] #存放所有img标签src属性值
        self.title = "" #html文件的标题
        self.isTile = False
    # 重写父类的handle_starttag()函数
    def handle_starttag(self, tag, attrs):
        # a标签
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (attr,attrVal) in attrs:
                    if attr == "href":
                        self.HrefValues.append(attrVal)
        # img标签
        if tag == "img":
            if len(attrs) == 0:
                pass
            else:
                for (attr,attrVal) in attrs:
                    if attr == "src":
                        self.ImgValues.append(attrVal)
        # title标签
        if tag == "title":
            self.isTile = True
    # 重写父类的handle_endtag方法：将设置为title 的标识符重置为false
    def handle_endtag(self, tag):
        if tag == "title":
            self.isTile = False
    # 重写父类的handle_data()
    def handle_data(self, data):
        if self.isTile:
            self.title = data
# 调用测试
if __name__ == "__main__":
    print ">>>>>自身调用测试<<<<<"
    HTML_CODE = """
                    <a href="#" class="btn-open"><img src="images/btn-open.png" /></a>
                    <img src="images/white-bottom.jpg" class="white-bottom-img" />
                    <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
                    <title>中国移动</title>
                    """
    mhp = MyHtmlParser()
    mhp.feed(HTML_CODE)
    mhp.close()
    print ">>>>>得到的所有的a标签的属性内容是：",mhp.HrefValues,"<<<<<"
    print ">>>>>所有的image标签属性内容是：",mhp.ImgValues,"<<<<<"
    print ">>>>>文件的标题是：",mhp.title[0],"<<<<<"