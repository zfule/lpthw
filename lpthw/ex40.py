class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])


song_of_tiger = Song(["1 2 3 4 5", "上山打老虎", "老虎没打着", "打着小松鼠"])

x = "你是风儿我是傻子"
song_of_wind = Song([f"1 2 3 开始唱：{x}"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

song_of_wind.sing_me_a_song()

song_of_tiger.sing_me_a_song()
