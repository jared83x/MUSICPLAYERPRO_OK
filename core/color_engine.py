from PIL import Image


class ColorEngine:


    def extract_color(self,path):

        image = Image.open(path)

        image.thumbnail(
            (50,50)
        )


        colors = (
            image
            .getcolors(
                2500
            )
        )


        colors.sort(
            reverse=True
        )


        return colors[0][1]
