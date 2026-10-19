"""
猜数字游戏 - Python基础语法练手项目
对应教程：BV1rpWjevEip 基础语法阶段
涉及知识点：random模块、while循环、if-elif-else、输入输出、异常处理
"""

import random


def get_user_guess(min_num, max_num):
    """获取用户输入，并进行有效性验证"""
    while True:
        try:
            guess = input(f"请输入一个 {min_num} 到 {max_num} 之间的数字：")
            guess = int(guess)
            if min_num <= guess <= max_num:
                return guess
            else:
                print(f"⚠️ 数字超出范围！请输入 {min_num} 到 {max_num} 之间的数字。")
        except ValueError:
            print("❌ 输入无效！请输入一个整数。")


def check_guess(guess, target):
    """判断猜测结果并返回提示信息"""
    if guess > target:
        return "📉 太大了！再小一点试试。"
    elif guess < target:
        return "📈 太小了！再大一点试试。"
    else:
        return "🎉 恭喜你，猜对了！"


def play_round(min_num=1, max_num=100):
    """进行一轮猜数字游戏"""
    target = random.randint(min_num, max_num)
    attempts = 0
    max_attempts = 7  # 最多允许猜7次

    print("=" * 50)
    print("🎮 欢迎来到猜数字游戏！")
    print(f"🤖 我已经想好了一个 {min_num} 到 {max_num} 之间的数字。")
    print(f"💡 你有 {max_attempts} 次机会来猜中它！")
    print("=" * 50)

    while attempts < max_attempts:
        print(f"第 {attempts + 1}/{max_attempts} 次猜测:")
        guess = get_user_guess(min_num,max_num)
        attempts += 1,

        result = check_guess(guess, target)
        print(result)

        if guess == target:
            print(f"🏆 太厉害了！你用了 {attempts} 次就猜中了！")
            if attempts == 1:
                print("⭐ 运气爆棚！一次命中！")
            elif attempts <= 3:
                print("⭐⭐ 高手！思维非常敏锐！")
            elif attempts <= 5:
                print("⭐ 不错！掌握了一些技巧。")
            return True
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"⏳ 还剩 {remaining} 次机会。")
            else:
                print(f"💔 机会用完了！正确答案是：{target}")
                return False

    return False


def show_stats(wins, losses, total_attempts, rounds):
    """显示游戏统计信息"""
    print("" + "=" * 50)
    print("📊 游戏统计")
    print("=" * 50)
    print(f"🎮 总游戏次数：{rounds}")
    print(f"🏆 胜利次数：{wins}")
    print(f"💔 失败次数：{losses}")
    if rounds > 0:
        win_rate = (wins / rounds) * 100
        avg_attempts = total_attempts / rounds
        print(f"📈 胜率：{win_rate:.1f}%")
        print(f"🎯 平均每轮猜测次数：{avg_attempts:.1f}")
    print("=" * 50)


def select_difficulty():
    """选择游戏难度"""
    print("请选择难度：")
    print("1. 简单模式 (1-50，10次机会)")
    print("2. 普通模式 (1-100，7次机会)")
    print("3. 困难模式 (1-200，8次机会)")
    print("4. 地狱模式 (1-1000，10次机会)")

    while True:
        choice = input("请输入选项 (1-4)：").strip()
        if choice == "1":
            return 1, 50, 10
        elif choice == "2":
            return 1, 100, 7
        elif choice == "3":
            return 1, 200, 8
        elif choice == "4":
            return 1, 1000, 10
        else:
            print("❌ 无效选项，请重新输入。")


def main():
    """游戏主函数"""
    print("🎲" * 25)
    print("        Python 猜数字游戏")
    print("🎲" * 25)

    wins = 0
    losses = 0
    total_attempts = 0
    rounds = 0

    while True:
        print("📋 主菜单")
        print("1. 开始游戏")
        print("2. 查看统计")
        print("3. 退出")

        choice = input("请选择 (1-3)：").strip()

        if choice == "1":
            min_num, max_num, max_attempts = select_difficulty()
            # 临时修改全局max_attempts（通过传参实现）
            # 这里重新封装一下play_round支持自定义参数

            target = random.randint(min_num, max_num)
            attempts = 0

            print("=" * 50)
            print("🎮 欢迎来到猜数字游戏！")
            print(f"🤖 我已经想好了一个 {min_num} 到 {max_num} 之间的数字。")
            print(f"💡 你有 {max_attempts} 次机会来猜中它！")
            print("=" * 50)

            won = False
            while attempts < max_attempts:
                print(f"\n第 {attempts + 1}/{max_attempts} 次猜测：")
                guess = get_user_guess(min_num, max_num)
                attempts += 1

                result = check_guess(guess, target)
                print(result)

                if guess == target:
                    print(f"\n🏆 太厉害了！你用了 {attempts} 次就猜中了！")
                    if attempts == 1:
                        print("⭐ 运气爆棚！一次命中！")
                    elif attempts <= 3:
                        print("⭐⭐ 高手！思维非常敏锐！")
                    elif attempts <= max_attempts // 2:
                        print("⭐ 不错！掌握了一些技巧。")
                    won = True
                    break
                else:
                    remaining = max_attempts - attempts
                    if remaining > 0:
                        print(f"⏳ 还剩 {remaining} 次机会。")
                    else:
                        print(f"\n💔 机会用完了！正确答案是：{target}")

            rounds += 1
            total_attempts += attempts
            if won:
                wins += 1
            else:
                losses += 1

        elif choice == "2":
            show_stats(wins, losses, total_attempts, rounds)

        elif choice == "3":
            print("\n👋 感谢游玩！再见！")
            if rounds > 0:
                show_stats(wins, losses, total_attempts, rounds)
            break

        else:
            print("❌ 无效选项，请重新输入。")


if __name__ == "__main__":
    main()



