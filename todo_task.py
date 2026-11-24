class Task:
    def __init__(self, title, priority, deadline):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.done = False

    # 昨天设计文档里要求的：把对象转成字典，方便存JSON
    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline,
            "done": self.done
        }