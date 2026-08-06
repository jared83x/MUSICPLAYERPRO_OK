from core.database import Session
from core.models import Favorite



class Favorites:


    def add(self,song_id):

        session = Session()


        fav = Favorite(
            song_id=song_id
        )


        session.add(fav)

        session.commit()

        session.close()



    def remove(self,song_id):

        session = Session()


        session.query(
            Favorite
        ).filter_by(
            song_id=song_id
        ).delete()


        session.commit()

        session.close()



    def exists(self,song_id):

        session = Session()


        result = session.query(
            Favorite
        ).filter_by(
            song_id=song_id
        ).first()


        session.close()


        return result is not None
