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
