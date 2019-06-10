"""
   这有六个人，在玩一个叫'关键字游戏'。游戏玩法及规则：六个人
都有一个关键字，谁猜到关键字说出来，被猜到的人会有基于其关
键字的惩罚哦。
"""
#* player
#* scene
#    * wine
#    * game
#    * bbq
#    * massage
#    * walk
#    * milk



print("""》》》关键字游戏""")

print("""
首先你应该选择一个人，猜他的关键字。
请在下面六个人里选择一个，并打印出来。
张艺兴，黄磊，王迅，黄渤，红磊，罗志祥。""")
name = input(">")


print(f"好的，你选择了{name}。游戏开始啦！加油！")

print("请输入关键字：", end = '')
keyword = input("> ")

if name == "张艺兴" and keyword == "喝酒":
    print("棒极啦！猜对啦！")
    print("游戏结束。")
else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")

if name == "黄磊" and keyword == "打游戏":
    print("棒极啦！猜对啦！")
    print("游戏结束。")
else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")

if name == "王迅" and keyword == "烧烤":
    print("棒极啦！猜对啦！")
    print("游戏结束。")
else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")

if name == "黄渤" and keyword == "按摩":
    print("棒极啦！猜对啦！")
    print("游戏结束。")
else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")

if name == "红磊" and keyword == "遛弯":
    print("棒极啦！猜对啦！")
    print("游戏结束。")
else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")

if name == "罗志祥" and keyword == "喝牛奶":
    print("棒极啦！猜对啦！")
    print("游戏结束。")
else:
    print("很遗憾关键字猜测失败，欢迎继续来玩。")
    print("游戏结束。")
