import flet as ft


# 任务（单个待办事项）
class Task(ft.Column):
    def __init__(self, task_name: str, task_delete):
        super().__init__()
        self.task_name = task_name  # 待办事项名
        self.task_delete = task_delete  # 是一个函数
        self.completed = False
        # 显示的组件
        self.display_task = ft.Checkbox(value=False, label=self.task_name, label_style=ft.TextStyle(size=20))
        self.edit_name = ft.TextField(expand=1)

        # 展示视图
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.EDIT_NOTE_ROUNDED,
                            icon_size=25,
                            icon_color=ft.Colors.BLUE_400,
                            tooltip='修改待办项',
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                            icon_size=25,
                            icon_color=ft.Colors.PINK_600,
                            tooltip='删除待办项',
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        # 编辑视图
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_ROUNDED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="更新待办项",
                    on_click=self.save_clicked,
                ),
            ],
        )

        # 使用 Container 包装内容并设置背景色
        self.content_container = ft.Container(
            content=ft.Column([self.display_view, self.edit_view]),
            bgcolor=ft.Colors.AMBER_50,
            padding=5,  # 添加内边距
            border_radius=8,  # 圆角
            margin=3,  # 添加外边距
            alignment=ft.alignment.center,
        )

        self.controls = [self.content_container]

    # 点击编辑按钮
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    # 点击保存按钮
    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    # 点击删除按钮
    def delete_clicked(self, e):
        self.task_delete(self)
