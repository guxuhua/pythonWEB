# -*- coding:utf-8 -*-
# 调用模块ReadHtml.py中的内容
"""调用模块ReadHtml.py"""
import ReadHtml as rh
print rh.__doc__
# 待操作的文件
file_name = "F:\python\\file\index.html"
out_data = rh.readContentsFromHtml(file_name)
print ">>>>>得到的内容类型是：",type(out_data),"<<<<<"
print out_data