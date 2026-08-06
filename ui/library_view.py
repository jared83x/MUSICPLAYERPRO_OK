import flet as ft

from core.library import Library
from ui.song_card import SongCard


class LibraryView(ft.Container):


    def __init__(self, player):

        super().__init__()


        self.player = player

        self.library = Library()


        self.expand=True


        self.search = ft.TextField(

            hint_text="Buscar música...",

            prefix_icon=ft.Icons.SEARCH,

            on_change=self.search_music

        )


        self.list = ft.ListView(

            expand=True,

            spacing=8

        )


        self.content = ft.Column(

            controls=[

                self.search,

                self.list

            ]

        )


        self.load_songs()



    def load_songs(self):


        self.list.controls.clear()


        for song in self.library.songs():


            self.list.controls.append(

                SongCard(

                    song,

                    self.play_song

                )

            )



    def play_song(self, song):

        self.player.play_song(
            song.path
        )



    def search_music(self,e):


        text=e.control.value


        self.list.controls.clear()


        songs = (

            self.library.search(text)

            if text

            else self.library.songs()

        )


        for song in songs:


            self.list.controls.append(

                SongCard(

                    song,

                    self.play_song

                )

            )


        self.update()
