# coding:utf-8 -*-
# 调用模块User.py
import User as u
# 初始化用户对象
user = u.User("JAVA",29,"男","JAVA")
# 展示用户信息
user.showUserInfo()
# 录入用户信息
userInfo = user.getUserInfo()
print userInfo
# 打印用户信息
user.showUserInfo()