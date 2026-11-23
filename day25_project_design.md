# 待办事项系统 (To-Do List) 设计文档

## 一、 功能需求
1. 查看任务：按优先级或状态显示。
2. 添加任务：包含任务名称、优先级（高/中/低）、允许用户手动输入截至时间。
3. 完成任务：标记某个任务为已完成。
4. 删除任务：将任务从列表中移除。
5. 数据持久化：保存到 `todo_v2.json`。

## 二、 数据结构设计 (JSON 格式)
[
    {
        "title": "学习Python",
        "priority": "高",
        "deadline": "用户输入的日期",  <-- 这里标明是动态输入的
        "done": false
    }
]

## 三、 类的设计 (面向对象)
我们需要两个类：

### 1. Task 类 (代表单个任务)
- 属性：title（名字）、priority（优先级）、deadline(截止时间)、done（是否完成）
- 方法：to_dict() -> 把对象转换成字典，方便存进 JSON。

### 2. TodoManager 类 (代表管理器)
- 属性：filename（文件名）、tasks（Task对象列表）
- 方法：
  - load_data()
  - save_data()
  - add_task()
  - show_tasks()
  - mark_done()
  - delete_task() # 新增

## 四、 主程序菜单
1. 查看任务
2. 添加任务
3. 标记完成
4. 删除任务
5. 退出