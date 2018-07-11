# -*- coding:utf-8 -*-
# 用户类：包含姓名、年龄、性别和职业属性
# 包含初始化、展示个人信息、录入信息函数
class User:
    if __name__ == "__main__":
        print ">>>>>自身开始调用<<<<<"

    def __init__(self,username,age,sex,job):
        info = ">>>>>初始化调用用户对象<<<<<"
        print info
        self.username = username
        self.age = age
        self.sex = sex
        self.job = job

    # 录入用户信息
    def getUserInfo(self):
        info = ">>>>>录入用户信息<<<<<"
        print info
        username = raw_input(">>>>>请输入您的姓名：")
        self.username = username
        try:
            age = int(raw_input(">>>>>请输入您的年龄："))
        except:
            print ">>>>>年龄输入非法<<<<<"
            age = 20
        if age>99 or age <0:
            print ">>>>>年龄输入非法，设置为初始年龄20<<<<<"
            age = 20
        self.age = age
        sex = raw_input(">>>>>请输入您的性别(男或者女)：")
        if sex != "男" and sex != "女":
            print ">>>>>性别输入非法,设置为默认的男<<<<<"
            sex = "男"
        self.sex = sex
        job = raw_input(">>>>>请输入您的职业：")
        self.job = job
        return {"username":username,"age":age,"sex":sex,"job":job}

    # 展示用户信息
    def showUserInfo(self):
        info = ">>>>>展示用户信息<<<<<"
        print info
        print """>>>>>用户的姓名是：【""",self.username,"】，用户的年龄是：【",self.age,"】，性别是：【",self.sex,"】，职业是：【",self.job,"】<<<<<"

# 初始化
#user = User("guxh",29,"男","IT")
# 打印
#user.showUserInfo()
# 重新获取用户信息
#user.getUserInfo()
# 打印
#user.showUserInfo()