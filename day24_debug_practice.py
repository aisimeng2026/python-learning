def calculate_average(scores):
    total = 0
    for s in scores:
        total += s
    # 这里故意除以0测试报错
    average = total / len(scores)
    return average

def main():
    my_scores = [85, 90, 78, 92]
    print("准备计算平均分...")
    result = calculate_average(my_scores)
    print(f"平均分是：{result}")

if __name__ == "__main__":
    main()