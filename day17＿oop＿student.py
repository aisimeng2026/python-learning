# 1. 定义类（类的名字首字母通常大写）
class Student:

    #2. 初始化方法
    def __init__(self,name,score):
        self.name = name     #把传进来的 name 绑定到对象身上
        self.score = score   #把传进来的 score 绑定到对象身上

    #3. 展示信息的方法
    def show＿info(self):
        print(f"我叫 {self.name}，我的成绩是 {self.score} 分。")

    #4. 加分的方法
    def upgrade(self, points):
        self.score += points
        print(f"{self.name} 加分成功！新成绩：{self.score} 分。")

#5. 实例化测试（不要缩进，要在类的外面）
s1 = Student("张三", 85)
s2 = Student("李四", 92)

#6. 调用方法
s1.show＿info()
s2.show＿info()

s1.upgrade(10)    #张三加10分
s2.upgrade(5)     #李四加5分