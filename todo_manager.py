import json
import os
from todo_task import Task  # 引入我们刚写的 Task 类

class TodoManager:
    def __init__(self, filename="todo_v2.json"):
        self.filename = filename
        self.tasks = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data_list = json.load(f)
                # 重点：把读出来的字典，还原成Task对象
                return [Task(d["title"],d["priority"], d["deadline"]) for d in data_list]
                #这里用到了列表推导式，相当于把每个字典变成对象
        except Exception:
            return []

    def save_data(self):
        # 把对象列表转成字典列表，才能存JSON
        dict_list = [task.to_dict() for task in self.tasks]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(dict_list, f, ensure_ascii=False, indent=4)

    def add_task(self, title, priority, deadline):
        new_task = Task(title, priority, deadline)
        self.tasks.append(new_task)
        self.save_data()
        print(f"成功添加任务：{title},截止日期：{deadline}")


    def show_tasks(self):
        if not self.tasks:
            print("当前没有待办事项。")
            return

        print("\n--- 待办清单 ---")
        for i, task in enumerate(self.tasks):
            status = "[x]" if task.done else "[]"
            print(f"{i + 1}. {status} 优先级:{task.priority} | 截止:{task.deadline} | {task.title}")
        print("----------------")

    def mark_done(self, index):
        real_index = index - 1
        if 0 <= real_index < len(self.tasks):
            self.tasks[real_index].done = True
            self.save_data()
            print(f"任务 '{self.tasks[real_index].title}' 已标记为完成！")
        else:
            print("输入的序号有误！")

    def delete_task(self, index):
        real_index = index - 1
        if 0 <= real_index < len(self.tasks):
            deleted_title = self.tasks[real_index].title
            del self.tasks[real_index]
            self.save_data()
            print(f"任务 '{deleted_title}' 已删除！")
        else:
            print("输入的序号有误！")
