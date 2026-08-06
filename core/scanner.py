import os

from core.database import Session
from core.models import Song
from core.metadata import get_metadata


FORMATS = (

    ".mp3",
    ".flac",
    ".wav",
    ".ogg",
    ".m4a",
    ".aac"

)


class Scanner:


    def scan(self, folder):

        session = Session()


        for root, dirs, files in os.walk(folder):

            for file in files:


                if not file.lower().endswith(FORMATS):
                    continue


                path = os.path.join(
                    root,
                    file
                )


                exists = (
                    session.query(Song)
                    .filter_by(path=path)
                    .first()
                )


                if exists:
                    continue



                data = get_metadata(
                    path
                )


                if not data:
                    continue



                song = Song(

                    title=data["title"],

                    artist=data["artist"],

                    album=data["album"],

                    genre=data["genre"],

                    year=data["year"],

                    path=path
                )


                session.add(
                    song
                )


        session.commit()

        session.close()
