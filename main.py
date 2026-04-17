import flet as ft 
from db import main_db


def main(page: ft.Page):
    page.title = 'ToDoList'
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=20)


    def load_tasks():
        task_list.controls.clear()
        for task_id, task, completed in main_db.get_tasks():
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task))
            page.update()


    def view_tasks(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)

        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True
            page.update()
        
        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)
        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        return ft.Row([
            task_field,
            edit_button,
            save_button
        ])

    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            task_id = main_db.add_task(task=task_text)
            print(f'Задача с ID {task_id}. Успешна записана!')
            task_list.controls.append(view_tasks(task_id=task_id, task_text=task_text))
            task_input.value = None
            page.update()

    task_input = ft.TextField(label='Введите задачу', expand=True, on_submit=add_task_db)
    add_task_button = ft.ElevatedButton('ADD', on_click=add_task_db, icon=ft.Icons.ADD)

    main_object = ft.Row([task_input, add_task_button]) 

    filter_buttons = ft.Row([
        ft.ElevatedButton('Все задачи', on_click=None),
        ft.ElevatedButton('В работе', on_click=None),
        ft.ElevatedButton('Готово ✅', on_click=None)
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    page.add(main_object, filter_buttons, task_list)
    load_tasks()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(main)