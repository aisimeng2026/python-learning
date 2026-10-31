def load＿contacts():
    contacts = {}
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()#去掉行末的换行符和空格
                if not line:
                    continue #跳过空行
                 #假设格式是：姓名，电话，城市
                parts = line.split(',')
                if len(parts) == 3:
                    name, phone, city = parts
                    contacts[name] = {"phone": phone, "city": city}
    except FileNotFoundError:
        print("第一次运行，通讯录为空，将创建新文件。")
    return contacts

def save＿contacts(contacts):
    with open('contacts.txt', "w", encoding='utf-8') as f:
        for name, info in contacts.items():
            #把字典内容拼接成字符串，用逗号隔开，最后加个换行符
            line = f"{name},{info['phone']},{info['city']}\n"
            f.write(line)

#测试运行
contacts = load＿contacts()

while True:
    print("\n=== 通讯录 ===")
    print("1. 添加  2. 查找  3. 删除  4. 查看  5. 退出")
    choice = input("请选择：")

    if choice == "1":
        name = input("姓名：")
        phone = input("电话：")
        city = input("城市：")
        contacts[name] = {"phone": phone, "city": city}
        save＿contacts(contacts) #添加后立刻保存
        print("添加成功！")

    elif choice == "4":
        for name, info in contacts.items():
            print(f"{name} - {info['phone']} - {info['city']}")

    elif choice == "5":
        print("再见！")
        break