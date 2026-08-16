import flet as ft
import asyncio

from ui.app import MusicPlayerApp
from ui.visualizer_view import VisualizerView

visualizer = VisualizerView()

async def update_visualizer():
    await asyncio.sleep(2)
    #VisualizerView.animate()
    visualizer.animate()

    

'''page.run_task(
    update_visualizer
)'''


def main(page: ft.Page): # page: ft.Page

    page.title = ".::. MusicPlayerPro .::."

    page.window.width = 1400
    page.window.height = 850

    page.padding = 0

    page.theme_mode = ft.ThemeMode.DARK

    
    page.run_task(
        update_visualizer
    )

    MusicPlayerApp(page)

    


#ft.app(target=main)
ft.run(main)
