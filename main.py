import flet as ft 
from db import main_db


def main(page: ft.Page):
    pass


if __name__ == "__main__":
    main_db.init_db()
    ft.app(main)