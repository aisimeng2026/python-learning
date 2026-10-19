# # 面向对象基础
# # 1.面向对象和面向过程的区别
# # 面向过程：分析步骤，并用函数实现，再依次调用
# # 面向对象：找人帮做
# # 2.类和对象
# #   开发中，先有类，再有对象
# # 2.1 类的三要素
# # 2.1.1.类名
# # 2.1.2.属性
# # 2.1.3.方法
# # 2.2 定义类
# class Washer:
#     height=800
# # 查看类属性：类名.属性名
# print(Washer.height)
# # 新增类属性：类名.属性名=值
# Washer.width=450
# print(Washer.width)
# # 2.3 创建对象
# wa=Washer()
# print(wa)   #显示对象在内存中的地址
# #第二次实例化
# wa2=Washer()
# print(wa2)
# # 内存地址不同，说明是不同对象，可以实例化多个对象
# #2.4实例方法和属性
# #2.4.1实例方法
# class Washer:
#     height=800    #类属性
#     def wash(self):
#         print("我会洗衣服")
# #实例化对象
# #wa.Washer()
# print("wa:",wa)
# #类对象调用方法
# #wa.wash()
# wa2=Washer()
# print("wa2:",wa2)
# wa2.wash()
# #2.4.2实例属性
# class Person:
#     name="bingbing"
#     def introduction(self):
#         print("我是实例方法")
#         print(f"{Person.name}的年龄:{self.age}")
# pe=Person()
# pe.age=18
# pe.introduction()
# pe2=Person()
# pe2.sex="女"
# print(pe2.sex)   #给pe对象新增的实例属性，其他对象依然没有这个属性
# #3.构造函数__init__()
# #class Test:
# #    def __init__(self):   #实例方法
# #        print("这是__init__（）函数")
# #te = Test()
# class Person:
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=18
#         self.height=183
#     def play(self):
#         print(f'{self.name}在打王者荣耀')
#     def introduction(self):
#         print(f"{self.name}的年龄是{self.age}，身高是{self.height}cm")
# #实例化对象
# pe=Person('bingbing',18,183)
# pe.introduction()
# pe.play()
# pe.introduction()
# #实例化第二个对象
# pe2=Person('ziyi',18,168)
# pe2.play()
# pe2.introduction()
# #4.析构函数__del__()
# class Person:
#     def __init__(self):
#         print("我是__int__()")
#     def __del__(self):
#         print("被销毁了")
# pe=Person()
# print("这是最后一行代码")
# #正常运行时，不会调用__del__()，执行结束后，系统会自行调用
#
#
# #5.封装
# class Person:
#     name='bingbing'
# pe=Person()
# print(pe.name)
# Person.name='ziyi'
# print(Person.name)
# #5.1隐藏属性
# class Person:
#     name='bingbing'
#     __age=18
# pe=Person()
# print(pe.name)
# print(pe.__age)
# #5.2私有属性_xxx
# class Person:
#     name='bingbing'
#     __age=18
#     _sex='女'
# pe=Person()
# print(pe.name)
# print(pe.Person__age)
# print(pe._sex)
# #5.4私有方法
# class Girl:
#     def _buy(self):
#         print("整体买买买")
# gril=Girl()
# gril._buy()
#
#
#
# #6.继承class 类名(父类名)
# #6.1单继承
# class Person:
#     def eat(self):
#         print("我会吃饭")
#     def sing(self):
#         print("唱歌小能手")
# class Girl(Person):
#     pass   #占位符，代码里面类下面不写任何东西，会自动跳过，不会报错，没有会报错
# class BOY(Person):
#     pass
# gril=Girl()
# gril.eat()
# gril.sing()
# #6.2继承的传递（多重继承）
# class Father:
#     def eat(self):
#         print("吃饭")
#     def sleep(self ):
#         print("睡觉")
# class Son(Father):
#     pass
# class Grandson(Son):
#     pass
# son=Son()
# son=Son()
# son.eat()
# son.sleep()
# grandson=Grandson()
# grandson.eat()
# grandson.sleep()
#
#
#
# #7.方法的重写
# #7.1覆盖父类的方法
# class Person:
#     def money(self):
#         print("一百万")
# class Man(Person):
#     def money(self):
#         print("自己一千万")
# man=Man()
# man.money()
# #7.2对父类方法进行拓展：继承父类的方法，子类也可以增加自己的功能
# class Person:
#     def money(self):
#         print("一百万")
#     def sleep(self):
#         print("睡觉啦")
# class Man(Person):
#     def money(self):
#         Person.money(self)
#         print("自己一千万")
#         super().sleep()#可以调用父类中的其他方法
#         super(Man,self).money()
# man=Man()
# man.money()
#
#
#
# #8.新式类写法
# class Animal:
#     def walk(self):
#         print("我会走路")
# class Dog(Animal):
#     name='富贵'
# #8.2多继承
# class Father(object):    #父类1
#     def money(self):
#         print('拥有一百万')
# class Mother(object):    #父类2
#     def appearance(self):
#         print("绝世容颜")
# class Son(Father, Mother):
#     pass
# son=Son()
# son.money
# son.appearance()
#
#
# #9.多态
# print(10+10)
# class Animal(object):
#     def shout(self):
#         print("动物会叫")
# class Cat(Animal):
#     def shout(self):
#         print("喵喵")
# class Dog(Animal):
#     def shout(self):
#         print("旺旺")
# cat=Cat()
# cat.shout()
# dog = Dog()
# dog.shout()
# #9.1多态性
# class Animal(object):
#     def eat(self):
#         print("我会干饭")
# class Dog(Animal):
#     def eat(self):
#         print("狗粮")
# class Pig(Animal):
#     def eat(self):
#         print("猪饲料")
# #多态性：定义一个统一的接口，一个接口多种实现
# def test(obj):
#     obj.eat()
# animal=Animal()
# pig=Pig()
# dog=Dog()
# test(animal)
# test(dog)
# test(pig)
#
# #10.静态方法
# class Person(object):
#     @staticmethod
#     def study():
#         print("人类会学习")
# pe=Person()
# pe.study()
# Person.study()
#
#
# #11.类方法    一般配合类属性使用
# class Person(object):
#     @classmethod
#     def sleep(cls):
#         print("cls:",cls)
#         print("人类在睡觉")
# Person.sleep()
#
#
# #12.__new__(Person)
# class Test(object):
#     def __int__(self):
#         print("这是__int__()")
#     def __new__(self,cls):
#         print("我是__new__()")
#         print(cls)
#         res=super().__new__(cls)    #方法重写，res里面保存的是实例对象的引用,__new__()是静态方法，形参里面有cls，实参就是cls
#         return res
# te=Test()
# print(te)
#
#
# #13.单例模式
# class A(object):
#     pass
# a1=A()
# print(a1)
# a2=A()
# print(a2)
# #内存地址发生变化说明是不同对象
# #实现单例模式   对象的内存地址都是一样的，只有一个对象
# #13.1重写__new__()实现单例模式
# #流程
# #①定义一个类属性，初始值为None，用来记录单例对象的引用
# #②重写__new__()方法
# #③进行对象判断，如果类属性是None，把__new__()返回对象引用保存进去
# #④返回类属性中记录的对象引用
# class Singleton(object):   #记录第一个被创建的对象的引用
#     obj=None
#     def __new__(cls, *args, **kwargs):
#         print("这是__new__()方法")
#         cls.obj=super().__new__(cls)
#         return cls.obj
#     def __int__(self):
#         print("我是__int__()")
# s=Singleton()
# print("s:",s)
# s2=Singleton()
# print("s2:",s2)
# #13.2导入模块实现单例模式
# #模块就是天然的单例模式
# #13.3应用场景
# #回收站对象；音乐播放器（一个音乐软件负责播放的对象只有一个）；开发游戏软件；数据库配置
#
#
#
# #14.魔法方法
# #14.1__doc__()：类的描述信息
#
#
#
# #图片复制'rb'
# #读取图片
# #with open("位置\图片.png","rb") as f:
# #    img=fild.read(f)
# #    print(img)
# # 将读取的内容写入到当前文件
# #with open('位置\\图片.jpg','wb') as f:
# #    f.write(img)
# #
# #



# #四则运算器
# #用户输入值
# #input（）接收到的默认为字符串，所以要用int()把他们转换成数字
# print("===四则运算器===")
# num1=int(input("请输入第一个数字："))
# operator=input("请输入运算符号(+,-,*,/):")
# num2=int(input("请输入第二个数字："))
# #分别进行四种运算，并打印结果
# #这里四种结果都会打印出
# print("加法结果：",num1,"+",num2,"=",num1+num2)
# print("减法结果：",num1,"-",num2,"=",num1-num2)
# print("乘法结果：",num1,"*",num2,"=",num1*num2)
# print("除法结果：",num1,"/",num2,"=",num1/num2)





# #成绩等级判断
# #1.输入成绩，并转为浮点数
# score=float(input("请输入你的成绩："))
# #使用if/elif/else进行等级判断
# if score>=90:
#     print("成绩等级：A（优秀）")
# elif score>=80:
#     print("成绩等级：B（良好）")
# elif score>=70:
#     print("成绩等级：C（中等）")
# elif score>=60:
#     print("成绩等级：D（及格）")
# elif score>=0:
#     print("成绩等级：E（不及格）")
# else:   #处理小于0的异常输入
#     print("错误：成绩不能小于0")





# #外层循环：控制行数（1-9）
# for i in range(1,10):
# #内层循环：控制列数
#     for j in range(1,i+1):
#         #end=""表示打印完后不换行，而是加一个空格
#         print(f"{j}*{i}={j*i}",end="")
# #内循环结束后，必须换行，才能进入下一行
# print()




# #外层循环：控制行数（1-9）
# for i in range(1,10):
# #内层循环：控制列数
#     for j in range(1,i+1):
#         #end=""表示打印完后不换行，而是加一个空格
#         print(f"{j}*{i}={j*i}")
# #内循环结束后，必须换行，才能进入下一行
# print()





# todo＿list=[]
# todo＿list.append("学习Python列表")
# todo＿list.append("清理C盘垃圾")
# print("你的待办列表")
# for task in todo＿list:
#     print("-"+task)
#
# done＿task=input("请输入你已完成的任务：")
# if done＿task in todo＿list:
#     todo＿list.remove(done＿task)
#     print(f"你太棒了！‘{done＿task}'已从完成列表中删除")
# else:
#     print("列表没有这个任务哦")
#
# for index,task in enumerate(todo＿list,start=1):
#     print(f"{index}. {task}")



#
# #创建一个初始通讯录字典
# contacts={
#     "张三":"138000000111",
#     "李四":"13899999999"
# }
# #添加联系人（字典增/改）
# def add＿contacts():
#     name=input("请输入姓名：")
#     phone=input("请输入电话号码：")
#     contacts[name]=phone#如果名字已存在，会更新号码；不存在则新增
#     print(f"成功添加/更新联系人:{name}\n")
# #查找联系人（字典查找）
# def search＿contacts():
#     name=input("请输入要查找的名字：")
#     if name in contacts:
#         print(f"{name}的电话是：{contacts[name]}")
#     else:
#         print("抱歉，通讯录里没有这个人。\n")
# #删除
# def delete＿contacts():
#     name=input("请输入要删除的姓名：")
#     if name in contacts:
#         del contacts[name]
#         print(f"成功删除：{name}\n")
#     else:
#         print("找不到。\n")
# #显示所有联系人(字典遍历）
# def show＿all():
#     print("当前通讯录列表：")
#     for name,phone in contacts.items():
#         print(f"-{name}:{phone}")
#     print("-"*20+"\n")
# #简单的交互菜单
# while True:
#     print("1.添加联系人")
#     print("2.查找联系人")
#     print("3.删除所有联系人")
#     print("4.查看所有联系人")
#     print("5.退出")
#     choice=input("请选择操作")
#
#     if choice=="1":
#         add＿contacts()
#     elif choice=="2":
#         search＿contacts()
#     elif choice=="3":
#         delete＿contacts()
#     elif choice=="4":
#         show＿all()
#     elif choice=="5":
#         print("再见")
#         break
#     else:
#         print("无效输入，重新选择")





# import random
# from mimetypes import guess_type
#
# #字典：{单词：提示词}
# word＿dict={
#     "python":"一种流行的编程语言",
#     "apple":"一种红色水果",
#     "pycharm":"你正在使用的开发工具"
# }
# #随机获取一个键值对
# target＿word,hint = random.choice(list(word＿dict.items()))
# print("欢迎来到猜字游戏")
# print(f"提示:{hint}")
# #简单的猜测逻辑
# guess=input("猜猜这个词：").lower()
# if guess == target＿word:
#     print("恭喜，你猜对了")
# else:
#     print(f"你猜错了，答案是：{target＿word}")




