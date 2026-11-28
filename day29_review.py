# 题目1
num = int(input("请输入一个整数："))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 题目2
total = 0
for i in range(1, 101):
    total += i
print(f"1到100的和是：{total}")

# 题目3
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 题目4
correct_pwd = "Python123"
for i in range(3):
    pwd = input("请输入密码：")
    if pwd == correct_pwd:
        print("登录成功！")
        break
else: #注意：for-else是Python的特性，如果循环没有被break打断，就执行else
    print("账号已锁定")

# 题目5
for i in range(1, 6):
    #打印空格+打印星星
    print(" "*(5 - i) + "*" * (2 * i -1))