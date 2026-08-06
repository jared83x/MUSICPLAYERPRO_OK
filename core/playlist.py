from core.database import Session
from core.models import Playlist


class PlaylistManager:


    def create(self,name):

        session = Session()


        playlist = Playlist(
            name=name
        )


        session.add(
            playlist
        )


        session.commit()

        session.close()



    def all(self):

        session = Session()


        playlists = (
            session.query(
                Playlist
            )
            .all()
        )


        session.close()


        return playlists
