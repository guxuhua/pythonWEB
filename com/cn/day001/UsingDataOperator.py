# -*- coding:utf-8 -*-
# 操作模块：DataOperator.py
# 定义一个列表
li = ["apple","orange","banana","juice",1,2,3,4,"a","b"]
import DataOperator as da
dataOperator = da.DataOperator(li)
# 展示列表中的元素
dataOperator.showListInfo()
# 过滤数字元素
print dataOperator.filterForInteger()
# 过滤长度大于5的元素
print dataOperator.filterForFilterLen(5)
# 过滤长度等于5的元素
print dataOperator.filterForEqualLen(5)
# 过滤长度等于1的元素
print dataOperator.filterForEqualLen(1)