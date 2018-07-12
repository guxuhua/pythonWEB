# -*- coding:utf-8 -*-
# 读取文件：F:\python\html\index.html
if __name__ == "__main__":
    print ">>>>>模块FileDemo01.py自身调用<<<<<"
else:
    print ">>>>>模块FileDemo01.py被外部调用"

# 读取文件:需要处理文件不存在的异常
file_name = "F:\python\html\index.html"
try:
    f = open(file_name,"r")
    li = f.readlines() # 按行读取
    for i in li:
        print i
    # 一次读取一行
    print ">>>>>>一次只读取一行文件<<<<<"
    while True:
        read_info = f.read()
        print ">>>>>每次读取一行的内容是：",read_info,"<<<<<"
        if read_info:
            print read_info
            f.next()
        else:
            break

except:
    print ">>>>>文件：",file_name,"不存在<<<<<"
finally:
    f.close()
