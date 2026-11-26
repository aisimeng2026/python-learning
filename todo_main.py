from todo_manager import TodoManager

def main():
    manager = TodoManager()

    while True:
        print("\n=== 待办系统 v2 ===")
        print("1. 添加任务")
        print("2. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            title = input("请输入任务内容：").strip()
            priority = input("请输入优先级（高/中/低)：").strip()
            deadline = input("请输入截止日期(如2026-12-01)：").strip()

        elif choice == "2":
            print("再见！")
            break
        else:
            print("输入无效！")



from todo_manager import TodoManager

def main():
    manager = TodoManager()

    while True:
        print("\n=== 待办系统 V2 ===")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 标记完成")
        print("4. 删除任务")
        print("5. 退出")
        choice = input("请选择：").strip()

        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            title = input("任务内容：").strip()
            priority = input("优先级(高/中/低)：").strip()
            deadline = input("截止日期(如 2026-12-01)：").strip()
            manager.add_task(title, priority, deadline)
        elif choice == "3":
            manager.show_tasks()
            try:
                num = int(input("请输入要完成的任务序号："))
                manager.mark_done(num)
            except ValueError:
                print("请输入数字序号：")
        elif choice == "4":
            manager.show_tasks()
            try:
                num = int(input("请输入要删除的任务序号："))
                manager.delete_task(num)
            except ValueError:
                print("请输入数字序号！")
        elif choice == "5":
            print("再见！")
            break
        else:
            print("输入无效！")

if __name__ == "__main__":
    main()