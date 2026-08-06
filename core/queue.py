import random


class PlaybackQueue:


    def __init__(self):

        self.items = []

        self.index = -1

        self.shuffle = False

        self.repeat = False



    def add(self,song):

        self.items.append(song)



    def add_next(self,song):

        self.items.insert(
            self.index + 1,
            song
        )



    def current(self):

        if self.index >= 0:

            return self.items[
                self.index
            ]

        return None



    def next(self):

        if not self.items:

            return None


        if self.shuffle:

            self.index = random.randint(
                0,
                len(self.items)-1
            )


        else:

            self.index += 1



        if self.index >= len(self.items):

            if self.repeat:

                self.index = 0

            else:

                return None



        return self.current()



    def previous(self):

        if self.index > 0:

            self.index -= 1

        return self.current()
