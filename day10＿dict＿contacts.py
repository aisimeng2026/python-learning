contacts = {"张三": {"phone": "12398760987", "city":"北京"}}

while True:
    print("\n=== 通讯录 ===")
    print("1.添加联系人")
    print("2.查找联系人")
    print("3.删除联系人")
    print("4.查看所有联系人")
    print("5.退出")

    choice = input("请选择操作（1~5）：")

    if choice == "1":
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        city = input("请输入城市：")
        #嵌套字典赋值
        contacts[name] = {"phone":phone, "city":city}
        print(f"已添加 {name}！")

    elif choice == "2":
        name = input("请输入要查找的姓名：").strip()
        #使用get（）查找，找不到返回 None
        info = contacts.get(name)
        if info:
            print(f"姓名：{name}，电话：{info['phone']}，城市：{info['city']}")
        else:
            print("查无此人！")

    elif choice == "3":
        name = input("请输入要删除的姓名：")
        if name in contacts:
            del contacts[name]
            print(f"已删除 {name}!")
        else:
            print("查无此人，无法删除！")

    elif choice == "4":
        if not contacts:
            print("通讯录为空！")
        else:
            print("--- 所有联系人 ---")
            #使用 items()遍历
            for name, info in contacts.items():
                print(f"姓名：{name}，电话：{info['phone']}，城市{info['city']}")

    elif choice == "5":
        print("退出通讯录系统，再见！")
        break
    else:
        print("输入有误，请重新输入！")