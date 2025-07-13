import flet as ft
from todo import TodoApp


# 主页面
def main(page: ft.Page):
    page.title = "MiniTodo"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp(page)
    page.add(todo)


if __name__ == '__main__':
    ft.app(main)
