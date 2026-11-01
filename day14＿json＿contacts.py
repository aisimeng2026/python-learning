import json

def load＿contacts():
    contacts = {}
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        print("第一次运行，通讯录为空，将创建新文件。")
    except json.decoder.JSONDecodeError:
        print("文件内容格式错误，将重置为空通讯录。")
    return contacts

def save＿contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as f:
        #ensure＿ascii=False保证中文正常显示，indent=4让文件缩进好看
        json.dump(contacts, f, ensure_ascii=False, indent=4)

#主程序
my＿contacts = load＿contacts()

while True:
    print("\n=== 通讯录系统 ===")
    print("1.添加  2.查看  3.退出")
    choice = input("请选择：")

    if choice == "1":
        name = input("姓名：").strip()
        phone = input("电话：").strip()
        city = input("城市：").strip()
        my＿contacts[name] = {"phone": phone, "city": city}
        save＿contacts(my＿contacts)
        print("添加成功！")

    elif choice == "2":
        if not my＿contacts:
            print("通讯录为空。")
        else:
            for name, info in my＿contacts.items():
                print(f"{name} - {info['phone']} - {info['city']}")

    elif choice == "3":
        print("退出！")
        break