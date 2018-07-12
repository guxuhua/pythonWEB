# -*- coding:utf-8 -*-
# 调用模块FileDemo02.py
# 文件
file_name = "F:\python\html\index.html"
import FileDemo02 as f2
# readLines读取
f2.getContensByLines(file_name)
# read读取
f2.getContentByRead(file_name)