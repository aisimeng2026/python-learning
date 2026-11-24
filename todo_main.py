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

if __name__ == "__main__":
    main()