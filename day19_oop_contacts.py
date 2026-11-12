import json
import os

class Contact:
    def __init__(self, filename="contacts_oop.json"):
        self.filename = filename
        #创建对象时，自动加载数据
        self.contacts = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
                return {}  # 文件不存在就返回空字典

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f,ensure_ascii=False, indent=4)

    def add(self, name, phone, city):
        self.contacts[name] = {"phone": phone, "city": city}
        self.save_data() #加完立刻保存
        print(f"成功添加联系人：{name}")

    def show_all(self):
        if not self.contacts:
            print("通讯录空空如也。")
            return
        for name, contact in self.contacts.items():
            print(f"{name} - {contact['phone']} - {contact['city']}")

# === 主程序 ===
if __name__ == "__main__":
    #实例化一个通讯录管理器
    manager = Contact()

    while True:
        print("\n=== oop通讯录 ===")
        print("1.添加  2.查看  3.退出")
        choice = input("请选择：")

        if choice == "1":
            name = input("姓名：").strip()
            phone = input("电话：").strip()
            city = input("城市：").strip()
            #调用管理器的方法
            manager.add(name, phone, city)
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            break
