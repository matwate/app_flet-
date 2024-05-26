import flet as ft


def NavBar(page):
    NavBar = ft.AppBar(
            leading_width=40,
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.HOME_WORK, on_click=lambda _: page.go('/Tareas')),
                ft.IconButton(ft.icons.INVENTORY, on_click=lambda _: page.go('/Inventario'))
            ]
        )
    
    # NavBar = ft.Container(
    #         content = ft.AppBar(
    #                 leading_width=40,
    #                 center_title=False,
    #                 bgcolor=ft.colors.SURFACE_VARIANT,
    #                 actions=[
    #                     ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
    #                     ft.IconButton(ft.icons.HOME_WORK, on_click=lambda _: page.go('/Tareas')),
    #                     ft.IconButton(ft.icons.INVENTORY, on_click=lambda _: page.go('/Inventario'))
    #                 ]
    #             ),
            
    #     )

    return NavBar
