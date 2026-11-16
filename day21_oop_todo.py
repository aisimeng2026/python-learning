import json
import os

class TodoManager:
    def __init__(self, filename="todo.json"):
        self.filename = filename
        self.tasks = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f,ensure_ascii=False, indent=4)

    def add_task(self, task_name):
        # 每个任务是一个字典
        new_task = {"task": task_name, "done": False}
        self.tasks.append(new_task)
        self.save_data()
        print(f"成功添加任务：{task_name}")

    def show_tasks(self):
        if not self.tasks:
            print("当前没有待办事项。")
            return

        print("\n--- 待办清单 ---")
        for i, t in enumerate(self.tasks):
            # 如果 done 是 Ture，打印[x]，否则打印[ ]
            status = "[x]" if t["done"] else "[]"
            print(f"{i + 1}. {status}{t['task']}")
        print("----------------")

    def mark_done(self, index):
        #用户输入的序号是从1开始的，列表索引是从0开始的
        real_index = index -1
        if 0 <= real_index < len(self.tasks):
            self.tasks[real_index]["done"] = True
            self.save_data()
            print("任务已标记完成！")
        else:
            print("输入的序号有误！")


#=== 主程序 ===
if __name__ == "__main__":
    manager = TodoManager()

    while True:
        print("\n=== To-Do List ===")
        print("1. 查看任务  2. 添加任务  3. 完成特定任务  4. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            task = input("请输入要添加的任务内容：").strip()
            if task:
                manager.add_task(task)
        elif choice == "3":
            manager.show_tasks()
            try:
                num = int(input("请输入要标记完成的任务序号："))
                manager.mark_done(num)
            except ValueError:
                print("请输入数字！")
        elif choice == "4":
            break
        else:
            print("输入无效，请重试。")

