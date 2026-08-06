from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    LargeBinary
)

from sqlalchemy import Boolean, ForeignKey


class Playlist(Base):

    __tablename__ = "playlists"


    id = Column(
        Integer,
        primary_key=True
    )


    name = Column(
        String
    )



class PlaylistSong(Base):

    __tablename__ = "playlist_songs"


    id = Column(
        Integer,
        primary_key=True
    )


    playlist_id = Column(
        Integer,
        ForeignKey(
            "playlists.id"
        )
    )


    song_id = Column(
        Integer,
        ForeignKey(
            "songs.id"
        )
    )



class Favorite(Base):

    __tablename__ = "favorites"


    id = Column(
        Integer,
        primary_key=True
    )


    song_id = Column(
        Integer,
        ForeignKey(
            "songs.id"
        )
    )


Base = declarative_base()


class Song(Base):

    __tablename__ = "songs"


    id = Column(
        Integer,
        primary_key=True
    )


    title = Column(
        String
    )


    artist = Column(
        String
    )


    album = Column(
        String
    )


    genre = Column(
        String
    )


    year = Column(
        String
    )


    duration = Column(
        Float
    )


    path = Column(
        String,
        unique=True
    )


    cover = Column(
        LargeBinary
    )
