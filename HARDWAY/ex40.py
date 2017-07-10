# _*_ coding:utf-8 _*_


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



Taiji = Song(["난 내 삶에 끝을 본적이 있어",
                "내 가슴속은 답답해 졌어",
                "내 삶에 끝을 막은것은",
                "나의 내일에 대한 두려움"])

myLyrics = ["난 내 삶에 끝을 본적이 있어",
                "내 가슴속은 답답해 졌어",
                "내 삶에 끝을 막은것은",
                "나의 내일에 대한 두려움"]


Taiji2 = Song(myLyrics)
Taiji2.sing_me_a_song()

