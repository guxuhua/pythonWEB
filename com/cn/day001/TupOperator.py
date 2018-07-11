# -*- coding:utf-8 -*-
# 操作元祖的API，继承自DataOperator
import DataOperator
da = DataOperator.DataOperator
class TupOperator(da): #继承自类：DataOperator
    def __init__(self,li):
        print ">>>>>初始化元祖操作API<<<<<"
        da.__init__(self,li) # 子类调用父类的方法，需要带上self参数
    # 展示元祖中的元素
    def showListInfo(self):
        print ">>>>>展示元祖中的元素<<<<<"
        da.showListInfo(self) # 子类调用父类的方法，需要带上self参数