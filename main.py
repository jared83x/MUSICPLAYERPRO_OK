import flet as ft

from ui.app import MusicPlayerApp
import flet as ft


def update_visualizer():

    visualizer_view.animate()


ft.page.run_task(
    update_visualizer
)



def main(page: ft.Page):

    page.title = "MusicPlayerPro"

    page.window.width = 1400
    page.window.height = 850

    page.padding = 0

    page.theme_mode = ft.ThemeMode.DARK

    MusicPlayerApp(page)


ft.app(target=main)
