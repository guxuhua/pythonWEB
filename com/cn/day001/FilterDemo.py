# -*- coding:utf-8 -*-
# 列表过滤和使用lambda函数过滤
if __name__ == "__main__":
    info = """>>>>>用来演示普通方式过滤列表和使用lambda函数过滤<<<<<"""
    print info
# 使用普通列表过滤
def filterForLi(li):
    info = ">>>>>使用普通过滤列表<<<<<"
    print info
    out_data = [element for element in li if not isinstance(element,int) and len(element)>5] #int类型没有长度，所以需要首先排除
    print out_data
# 使用lambda函数过滤
def filterByLambda(li):
    info = ">>>>>使用lambda函数进行列表信息过滤<<<<<"
    print info
    # 定义一个lambda函数:int类型没有长度，所以需要首先排除
    g = lambda x : not isinstance(x,int) and len(x)>5
    out_data = [element for element in li if g(element)]
    print out_data
# 定义一个列表
li = [1,2,3,4,5,"a","b","c","apple","banana","orange","juice"]
# 分别调用两个函数:结果应该一样才准确
# 普通过滤
filterForLi(li)
# lambda函数过滤
filterByLambda(li)
