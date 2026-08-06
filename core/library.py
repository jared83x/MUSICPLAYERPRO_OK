from core.database import Session
from core.models import Song



class Library:


    def songs(self):

        session = Session()

        result = (
            session.query(Song)
            .order_by(
                Song.artist
            )
            .all()
        )

        session.close()

        return result



    def search(self,text):

        session = Session()


        result = (

            session.query(Song)

            .filter(

                Song.title.contains(text)

            )

            .all()

        )


        session.close()


        return result
