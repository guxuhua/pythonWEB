# -*- coding:utf-8 -*-
# 解析出文件：F:\python\\file\index.html的标题头，和a标签和img标签的属性内容
from ReadHtml import MyHtmlReader
from ParseHtml import MyHtmlParser
# 文件名称
file_name = "F:\python\\file\index.html"
# 获取出文件的内容
mhr = MyHtmlReader()
file_contents = mhr.readContext(file_name)
# 获取title、a标签的href属性、img标签的src属性
mhp = MyHtmlParser()
mhp.feed(file_contents)
mhp.close()
# 标题头
print ">>>>>标题是：",mhp.title
print ">>>>>a标签的href属性是：",mhp.HrefValues
print ">>>>>img标签的src属性是：",mhp.ImgValues