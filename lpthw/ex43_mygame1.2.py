"""更新说明：
*关键字猜测机会增加一次
*游戏名字文本更改
"""
print("""《《《关键字游戏》》》""")

print("""
首先你应该选择一个人，猜他的关键字。
请在下面六个人里选择一个，并打印出来。
张艺兴，黄磊，王迅，黄渤，红磊，罗志祥。""")
name = input(">")

if name == "张艺兴":
    print(f"好的，你选择了{name}。游戏开始啦！加油！")
    print("请输入关键字：", end = '')
    keyword = input(" ")
    if keyword == "喝酒":
        print("棒极啦！猜对啦！")
        print("游戏结束。")
    else:
        print("真遗憾！回答错误！\n")
        print("你还有一次机会，加油！")
        a_keyword = input("请输入关键字： ")
        if a_keyword == "喝酒":
            print("棒极啦！猜对啦！")
            print("游戏结束。")
        else:
            print("很遗憾关键字猜测失败，欢迎继续来玩。")
            print("游戏结束。")

elif name == "黄磊":
    print(f"好的，你选择了{name}。游戏开始啦！加油！")
    print("请输入关键字：", end = '')
    keyword = input(" ")
    if keyword == "打游戏":
        print("棒极啦！猜对啦！")
        print("游戏结束。")
    else:
        print("真遗憾！回答错误！\n")
        print("你还有一次机会，加油！")
        a_keyword = input("请输入关键字： ")
        if a_keyword == "打游戏":
            print("棒极啦！猜对啦！")
            print("游戏结束。")
        else:
            print("很遗憾关键字猜测失败，欢迎继续来玩。")
            print("游戏结束。")

elif name == "王迅":
    print(f"好的，你选择了{name}。游戏开始啦！加油！")
    print("请输入关键字：", end = '')
    keyword = input(" ")
    if keyword == "烧烤":
        print("棒极啦！猜对啦！")
        print("游戏结束。")
    else:
        print("真遗憾！回答错误！\n")
        print("你还有一次机会，加油！")
        a_keyword = input("请输入关键字： ")
        if a_keyword == "烧烤":
            print("棒极啦！猜对啦！")
            print("游戏结束。")
        else:
            print("很遗憾关键字猜测失败，欢迎继续来玩。")
            print("游戏结束。")

elif name == "黄渤":
    print(f"好的，你选择了{name}。游戏开始啦！加油！")
    print("请输入关键字：", end = '')
    keyword = input(" ")
    if keyword == "按摩":
        print("棒极啦！猜对啦！")
        print("游戏结束。")
    else:
        print("真遗憾！回答错误！\n")
        print("你还有一次机会，加油！")
        a_keyword = input("请输入关键字： ")
        if a_keyword == "按摩":
            print("棒极啦！猜对啦！")
            print("游戏结束。")
        else:
            print("很遗憾关键字猜测失败，欢迎继续来玩。")
            print("游戏结束。")

elif name == "红磊":
    print(f"好的，你选择了{name}。游戏开始啦！加油！")
    print("请输入关键字：", end = '')
    keyword = input(" ")
    if keyword == "遛弯":
        print("棒极啦！猜对啦！")
        print("游戏结束。")
    else:
        print("真遗憾！回答错误！\n")
        print("你还有一次机会，加油！")
        a_keyword = input("请输入关键字： ")
        if a_keyword == "遛弯":
            print("棒极啦！猜对啦！")
            print("游戏结束。")
        else:
            print("很遗憾关键字猜测失败，欢迎继续来玩。")
            print("游戏结束。")

elif name == "罗志祥":
    print(f"好的，你选择了{name}。游戏开始啦！加油！")
    print("请输入关键字：", end = '')
    keyword = input(" ")
    if keyword == "喝牛奶":
        print("棒极啦！猜对啦！")
        print("游戏结束。")
    else:
        print("真遗憾！回答错误！\n")
        print("你还有一次机会，加油！")
        a_keyword = input("请输入关键字： ")
        if a_keyword == "喝牛奶":
            print("棒极啦！猜对啦！")
            print("游戏结束。")
        else:
            print("很遗憾关键字猜测失败，欢迎继续来玩。")
            print("游戏结束。")

else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")
