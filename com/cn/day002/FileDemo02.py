# -*- coding:utf-8 -*-
# 读取目标文件：F:\python\html\index.html
if __name__ == "__main__":
    print ">>>>>模块：FileDemo02.py由自身调用<<<<<"
else:
    print ">>>>>模块：FileDemo02.py被外部调用<<<<<"

#读取每一行数据并输出
def getContensByLines(file_name):
    # 打开文件，需抓取异常：文件不存在
    print ">>>>>待操作的文件名是：【",file_name,"】<<<<<"
    try:
        f = open(file_name,"r") # 只读模式打开
        li = f.readlines()
        for i in li:
            print i
    except:
        print ">>>>>文件不存在<<<<<"
    finally:
        if f:
            f.close()


# 按行读取文件：read()方法
def getContentByRead(file_name):
    print ">>>>>按行读取文件：【",file_name,"】<<<<<"
    try:
        f = open(file_name,"r")
        while True:
            con = f.read()
            if con:
                print con
                # next()需要抓起IO异常
                try:
                    f.next()
                except:
                    print ">>>>>读取到文件末尾了<<<<<"
                    break
            else:
                break
    except:
        print ">>>>>文件：【",file_name,"】不存在<<<<<"
    finally:
        if f:
            f.close()