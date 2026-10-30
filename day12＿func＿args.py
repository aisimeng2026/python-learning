#任务 A： *args 练习
def sum＿all(*args):
    # args 是一个元组，例如（1，2，3）
    total = 0
    for num in args:
        total += num
    return total

print("测试A：", sum＿all(1,2,3,4,5,6,7,8,9,10))

#任务B： **kwargs 练习
def create＿user(**kwargs):
    #kwargs 是一个字典，例如{'name': '小明'， 'age': 18}
    print("--- 用户信息 ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create＿user(name="zhangsan", age=36, city="北京")

#任务C：默认参数
def power(base, exponet=2):
    return base ** exponet

print("测试 C1：", power(3))
print("测试 C2：", power(2, 3))