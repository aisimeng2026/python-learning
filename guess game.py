import random

def guess＿number(low=1, high=100, max＿tries=7):
    answer = random.randint(low, high)
    print(f"我想了一个 {low}-{high} 的数字，你有 {max＿tries} 次机会。")

    for i in range(1, max＿tries + 1):
        try:
            guess = int(input(f"第 {i} 次猜："))
        except ValueError:
            print("请输入整数")
            continue

        if not (low <= guess <= high):
            print(f"请输入 {low} 到 {high} 之间的数。")

        if guess == answer:
            print(f"恭喜！你用了{i}次猜对了。")
            return True
        elif guess > answer:
            print("大了。")
        else:
            print("小了。")

    print(f"机会用完了，答案是{answer}。")
    return False

if __name__ == "__main__":
    guess＿number()