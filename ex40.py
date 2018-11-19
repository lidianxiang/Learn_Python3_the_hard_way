"""
获取某样东西里包含的东西的三种方法

1、字典
2、导入模块
3、类的实例化

"""
class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["There rally around the family",
                        "With poctets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
