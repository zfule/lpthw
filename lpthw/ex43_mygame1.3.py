"""更新说明：
*代码优化
"""


from textwrap import dedent

def rightkeyword():
    print("恭喜你答对啦！棒极啦。")
    print("游戏结束，")

def firstwrongkeyword():
    print("很遗憾你答错了。\n")
    print("你还有一次机会，加油！")

def lastwrongkeyword():
    print("很遗憾回答错误！游戏失败。")
    print("游戏结束。")

def zhangyixing():
    keyword = input("请输入关键字：")
    if keyword == '喝酒':
        rightkeyword()
    else:
        firstwrongkeyword()
        a_keyword = input("请再次输入关键字：")
        if a_keyword == '喝酒':
            rightkeyword()
        else:
            lastwrongkeyword()
            yixing = Drink()

def huanglei():
    keyword = input("请输入关键字：")
    if keyword == '打游戏':
        rightkeyword()
    else:
        firstwrongkeyword()
        a_keyword = input("请再次输入关键字：")
        if a_keyword == '打游戏':
            rightkeyword()
        else:
            lastwrongkeyword()

def wangxun():
    keyword = input("请输入关键字：")
    if keyword == '烧烤':
        rightkeyword()
    else:
        firstwrongkeyword()
        a_keyword = input("请再次输入关键字：")
        if a_keyword == '烧烤':
            rightkeyword()
        else:
            lastwrongkeyword()

def huangbo():
    keyword = input("请输入关键字：")
    if keyword == '按摩':
        rightkeyword()
    else:
        firstwrongkeyword()
        a_keyword = input("请再次输入关键字：")
        if a_keyword == '按摩':
            rightkeyword()
        else:
            lastwrongkeyword()

def honglei():
    keyword = input("请输入关键字：")
    if keyword == '遛弯':
        rightkeyword()
    else:
        firstwrongkeyword()
        a_keyword = input("请再次输入关键字：")
        if a_keyword == '遛弯':
            rightkeyword()
        else:
            lastwrongkeyword()

def luozhixiang():
    keyword = input("请输入关键字：")
    if keyword == '喝牛奶':
        rightkeyword()
    else:
        firstwrongkeyword()
        a_keyword = input("请再次输入关键字：")
        if a_keyword == '喝牛奶':
            rightkeyword()
        else:
            lastwrongkeyword()

def start():
    print("《《《关键字游戏》》》")

    print(dedent("""
    首先你应该选择一个人,猜他的关键字。
    请在下面六个人里选择一个，并打印出来。
    张艺兴，黄磊，王迅，黄渤，红磊，罗志祥。"""))

    name = input("你选择的人物是：")

    if name == '张艺兴':
        zhangyixing()
    elif name == '黄磊':
        huanglei()
    elif name == '王迅':
        wangxun()
    elif name == '黄渤':
        huangbo()
    elif name == '红磊':
        honglei()
    elif name == '罗志祥':
        luozhixiang()
    else:
        print("你选择了错误的名字")
        print("游戏结束。")

start()
