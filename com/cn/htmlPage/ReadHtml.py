# -*- coding:utf-8 -*-
# 读取指定的html文件内容
class MyHtmlReader():
    """读取指定html文件内容"""
    def __init__(self):
        self.contens = [] #保存读取的文件内容

    # 校验给定的文件是否存在
    def __validFile(self,file_name):
        is_exit = False
        print ">>>>>校验文件：【",file_name,"】是否存在<<<<<"
        try:
            f = open(file_name,"r")
            is_exit = True
        except:
            print ">>>>>给定文件：【",file_name,"】不存在<<<<<"
            is_exit = False
        finally:
            if f:
                f.close()
        return is_exit

    def readContext(self,file_name):
        # 判断文件是否存在
        is_exit = self.__validFile(file_name) #调用同类的其他方法需要带上self
        if is_exit:
            # 执行读取
            f = open(file_name,"r")
            while True:
                read_content = f.read()
                if read_content:
                    self.contens.append(read_content)
                    try:
                        f.next()
                    except:
                        print ">>>>>读取到文件最后一行<<<<<"
                        break
                else:
                    break
            f.close()
        else:
            print ">>>>>文件不存在<<<<<"
        return "".join(self.contens) # 返回读取到的内容

if __name__ == "__main__":
    print ">>>>>模块：ReadHtml.py被自身执行调用<<<<<"
    mhr = MyHtmlReader()
    file_name = "F:\python\\file\index.html"
    out_data = mhr.readContext(file_name)
    print out_data