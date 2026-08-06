import re


class LyricsParser:


    def parse(self,text):

        lines=[]


        pattern = (
            r"\[(\d+):(\d+\.\d+)\](.*)"
        )


        for match in re.findall(
            pattern,
            text
        ):

            minutes = int(
                match[0]
            )

            seconds = float(
                match[1]
            )


            timestamp = (
                minutes * 60
                +
                seconds
            )


            lyric = match[2]


            lines.append(
                {
                    "time":timestamp,
                    "text":lyric
                }
            )


        return sorted(
            lines,
            key=lambda x:x["time"]
        )
