import json
import csv


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

# === 今天新加的方法 ===
    def export_csv(self):
        if not self.contacts:
            print("没有数据可以导出。")
            return

        with open("contacts_export.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            #1.写入表头
            writer.writerow(["姓名", "电话", "城市"])
            #2.写入数据
            for name, contact in self.contacts.items():
                writer.writerow([name, contact["phone"], contact["city"]])
        print("导出成功！请查看 contacts_export.csv 文件。")


# ===主程序 ===
if __name__ == "__main__":
    manager = Contact()
    #加上看看电脑到底认出了哪些方法
    print("【诊断】 当前对象拥有的方法：", dir(manager))

    while True:
        print("\n=== oop通讯录 ===")
        print("1. 添加  2. 查看  3. 导出CVS  4. 退出")
        choice = input("请选择：")

        if choice == "1":
            name = input("姓名：").strip()
            phone = input("电话：").strip()
            city = input("城市：").strip()
            manager.add(name, phone, city)
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            manager.export_csv()
        elif choice == "4":
            break