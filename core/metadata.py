from mutagen import File


def get_metadata(path):

    audio = File(
        path,
        easy=True
    )


    if not audio:
        return None


    return {

        "title":
            audio.get(
                "title",
                ["Desconocido"]
            )[0],


        "artist":
            audio.get(
                "artist",
                ["Desconocido"]
            )[0],


        "album":
            audio.get(
                "album",
                ["Desconocido"]
            )[0],

        "genre":
            audio.get(
                "genre",
                [""]
            )[0],

        "year":
            audio.get(
                "date",
                [""]
            )[0]

    }
