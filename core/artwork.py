from mutagen import File
from mutagen.id3 import APIC
import hashlib
import os


COVER_FOLDER = "assets/covers"


def get_cover(path):

    os.makedirs(
        COVER_FOLDER,
        exist_ok=True
    )


    filename = (
        hashlib.md5(
            path.encode()
        ).hexdigest()
        + ".jpg"
    )


    cover_path = os.path.join(
        COVER_FOLDER,
        filename
    )


    if os.path.exists(cover_path):

        return cover_path



    try:

        audio = File(path)


        if audio.tags:

            for tag in audio.tags.values():

                if isinstance(tag, APIC):

                    with open(
                        cover_path,
                        "wb"
                    ) as f:

                        f.write(tag.data)


                    return cover_path


    except Exception:

        pass


    return None
