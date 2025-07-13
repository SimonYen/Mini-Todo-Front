import flet as ft
from task import Task


# noinspection PyCallingNonCallable
class TodoApp(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        # 待办事项输入框
        self.new_task = ft.TextField(hint_text='新的待办事项~', expand=True)
        # 代办事项，每个独占一行
        self.tasks = ft.ListView(spacing=10, padding=20, width=500, auto_scroll=True)
        self.tasks_view = ft.Container(
            content=self.tasks,
            bgcolor=ft.Colors.GREY_50,
        )
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tab_changed,
            tabs=[ft.Tab(text='所有的'), ft.Tab(text='进行中'), ft.Tab(text='已完成')],
            width=300,
            tab_alignment=ft.TabAlignment.CENTER,
        )
        self.width = 600
        self.page: ft.Page = page
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked),
                ],
            ),
            ft.Container(
                content=self.filter,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.BLUE_50,
            ),
            ft.Container(
                content=self.tasks_view,
                alignment=ft.alignment.center,
            ),
        ]

    # 重载
    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text  # 获取当前tab的文本
        for task in self.tasks.controls:
            task.visible = (
                    status == '所有的'
                    or (status == '进行中' and task.completed == False)
                    or (status == '已完成' and task.completed)
            )

    # 更换tab
    def tab_changed(self, e):
        self.update()

    # 新建一个待办事项
    def add_clicked(self, e):
        # 如果文字不为空
        if len(self.new_task.value.strip()) == 0:
            # 创建SnackBar实例并设置到page
            self.page.open(ft.SnackBar(ft.Text('标题不能为空！'), duration=1000))
            self.page.update()
            return
        self.tasks.controls.append(Task(self.new_task.value, self.delete_clicked))
        # 清空
        self.new_task.value = ''
        self.update()

    # 删除一个待办事项
    def delete_clicked(self, task: Task):
        self.tasks.controls.remove(task)
        self.page.open(ft.SnackBar(ft.Text(f"删除{task.task_name}"), duration=1000))
        self.update()
