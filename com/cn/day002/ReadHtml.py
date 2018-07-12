# -*- coding:utf-8 -*-
# 读取html文件：F:\python\file\index.html内容，并解析其中的内容
"""读取html文件：F:\python\\file\index.html内容，并解析其中的内容"""
# 读取目标文件内容
def readContentsFromHtml(file_name):
    li = [] #返回的数据
    print ">>>>>待操作的文件是：",file_name,"<<<<<"
    try:
        f = open(file_name,"r") #以只读模式打开文件
        while True:
            read_info = f.read()
            if read_info:
                li.append(read_info)
                try:
                    f.next() #指针进入下一行
                except:
                    print ">>>>>到达文件最后一行<<<<<"
                    break
            else:
                print ">>>>>无法读取到文件内容<<<<"
                break
    except IOError:
        print ">>>>>目标文件：【",file_name,"】不存在<<<<<"
    finally:
        if f:
            f.close()
    return "".join(li)