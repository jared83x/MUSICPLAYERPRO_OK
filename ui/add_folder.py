import flet as ft

from core.scanner import Scanner


class AddFolder:


    def __init__(self,page):

        self.page=page

        self.scanner=Scanner()


        self.picker=ft.FilePicker(
            on_result=self.result
        )


        page.overlay.append(
            self.picker
        )



    def open(self,e):

        self.picker.get_directory_path()



    def result(self,e):

        if e.path:

            self.scanner.scan(
                e.path
            )
