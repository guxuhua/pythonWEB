# -*- coding:utf-8 -*-
# 将文件：F:\python\html\index.html 复制到 F:\python\file\index.html下
# 按行读取文件内容，并将结果返回到列表中
def readFileAsLine(file_name):
    print ">>>>>复制的源文件是：",file_name,"<<<<<"
    li = []
    try:
        f = open(file_name,"r") # 只读模式打开
        line_content = f.read()
        while True:
            if line_content:
                li.append(line_content)
                try:
                    f.next()
                except:
                    print ">>>>>读取到文件：【", file_name, "】最后一行<<<<<"
                    break
            else:
                break
    except:
        print ">>>>>文件：【",file_name,"】不存在<<<<<"
    finally:
        if f:
            f.close()
    return li
# 将读取到的文件内容写入到待操作的文件目录
def writeContenToFile(li,file_name):
    print ">>>>>等待写入的文件名称是：【",file_name,"】<<<<<"
    try:
        f = open(file_name,"a")
        for i in li:
            f.write(i)
    except:
        print ">>>>>文件：【",file_name,"】不存在<<<<<"
    finally:
        if f:
            f.close()

# 待操作的文件
file_name = "F:\python\html\index.html"
# 读取文件内容
li = readFileAsLine(file_name)
for i in li:
    print i
# 待写入的文件
desc_file = "F:\python\\file\index.html"
# 操作写入
writeContenToFile(li,desc_file)