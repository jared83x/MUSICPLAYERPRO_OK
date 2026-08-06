import os

from core.lyrics_parser import LyricsParser


class LyricsManager:


    def __init__(self):

        self.lines=[]

        self.parser = (
            LyricsParser()
        )



    def load(self,path):

        lrc = (
            os.path.splitext(path)[0]
            +
            ".lrc"
        )


        if not os.path.exists(lrc):

            self.lines=[]

            return



        with open(
            lrc,
            "r",
            encoding="utf-8"
        ) as file:

            content=file.read()



        self.lines = (
            self.parser
            .parse(content)
        )



    def current(self,time):

        current=""


        for line in self.lines:

            if time >= line["time"]:

                current=line["text"]

            else:

                break


        return current
