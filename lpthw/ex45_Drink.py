from textwrap import dedent

class Drink(object):

    print("这是你的惩罚哦！")
    print(dedent("""
    这是一个关于酒的惩罚。中国是一个酒文化十分深厚的国家。
    关于酒的故事与人的历史相当，今天我们就来看看中华诗词
    里那些关于酒的诗句。（亲😙，肚子里的墨水要倒出来了哦。
    """))

    a = 0
    while a < 10:

        poem = input(">>>>请在下一行输入诗句\n")
        a += 1

        if '酒' in poem:
            print("你真棒！继续加油。")

            if a < 10:
                print(f"还有{10-a}句就要成功啦，坚持。")

            else:
                print("恭喜你，完成此次惩罚挑战。")

        else:

            if a < 3:
                print("欸，小学背的唐诗宋词都交给老师了吧。")
                print("恭喜你，挑战失败。")
                exit(0)

            elif 3 <= a <= 7:
                print("真遗憾，回答错误。快去找找唐诗三百首吧。")
                exit(0)

            else:
                print(f"真的好遗憾，你离成功只剩下{10-a}步之遥！")
                exit(0)
