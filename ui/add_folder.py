import flet as ft
import asyncio
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



    '''def open(self): #def open(self,e)

        self.picker.get_directory_path()'''

    #@staticmethod  
    async def open(self):
        path = await self.picker.get_directory_path("Seleccione un directorio.")

    
    def result(self,e):

        if e.path:

            self.scanner.scan(
                e.path
            )
