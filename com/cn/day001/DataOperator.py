# -*- coding:utf-8 -*-
# 一个包含列表操作常用方法的模块
class DataOperator:
    """列表操作的常用方法"""
    def __init__(self,li):
        print ">>>>>初始化操作API<<<<<"
        self.li=li
    # 循环获取列表信息
    def showListInfo(self):
        print ">>>>>展示列表中的元素<<<<<"
        count = 0
        for i in self.li:
            print ">>>>>第：【",(count+1),"】元素是：",i,"<<<<<"
            count = count+1
    # 过滤列表元素：返回其中的int类型元素
    def filterForInteger(self):
        print ">>>>>过滤列表中的int类型元素<<<<<"
        return [element for element in self.li if isinstance(element,int)]
    # 过滤列表中元素长度大于指定长度的元素
    def filterForFilterLen(self,l):
        print ">>>>>过滤列表中元素长度大于：",l,"的元素<<<<<"
        # 使用lambda函数过滤
        g = lambda x :not isinstance(x,int) and len(x)>l
        return [element for element in self.li if g(element)]
    # 过滤列表中元素长度等于指定长度的元素信息
    def filterForEqualLen(self,l):
        print ">>>>>过滤列表中的元素长度等于：",l,"的元素<<<<<"
        return [element for element in self.li if not isinstance(element,int) and len(element)==l]