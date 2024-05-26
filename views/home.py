from typing import Union
import flet as ft
from views.Router import Router
# from State import global_state, State


def Home_page(router_data: Union[Router, str, None] = None):
    
    container  = ft.Container(
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True,
            # bgcolor="#000000",
            # padding=20,
            width=480,
            height=800,
            # clip_behavior=ft.ClipBehavior.HARD_EDGE,
            controls=[
                ft.Text("Bienvenido nombre!", style=ft.TextThemeStyle.HEADLINE_LARGE, color="#C9C9C9"),
                ft.Text(
                    "Como te encuentras el dia de hoy?",
                    style=ft.TextThemeStyle.HEADLINE_LARGE,
                    color="#C9C9C9",
                    
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                            ft.Container(
                                content = 
                                    ft.ElevatedButton(
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=50),
                                        bgcolor="#ADF7B6",
                                        padding=ft.Padding(20, 20, 20, 20),
                                    ),
                                ),
                                width=100,
                                height=100,
                                border_radius=50,
                            ),
                        ft.Container(
                            content = 
                                ft.ElevatedButton(
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=50),
                                    bgcolor="#F56767",
                                    padding=ft.Padding(20, 20, 20, 20),
                                ),
                            ),
                            width=100,
                            height=100,
                            bgcolor="#F56767",
                            border_radius=50,
                        ),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Container(
                                    content = 
                                        ft.ElevatedButton(
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=50),
                                            bgcolor="#A0CED9",
                                            padding=ft.Padding(20, 20, 20, 20),
                                        ),
                                    ),
                                    width=100,
                                    height=100,
                                    bgcolor="#A0CED9",
                                    border_radius=50,
                                ),
                                
                                ft.Container(
                                    content = 
                                        ft.ElevatedButton(
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=50),
                                            bgcolor="#E8DFF5",
                                            padding=ft.Padding(20, 20, 20, 20),
                                        ),
                                    ),
                                    width=100,
                                    height=100,
                                    bgcolor="#E8DFF5",
                                    border_radius=50,
                                ),

                            ]
                        ),
                        ft.Container(
                                    content = 
                                        ft.ElevatedButton(
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=50),
                                            bgcolor="#FCF5C7",
                                            padding=ft.Padding(20, 20, 20, 20),
                                        ),
                                    ),
                                    width=100,
                                    height=100,
                                    bgcolor="#FCF5C7",
                                    border_radius=50,
                                ),
                    ]
                ),
                
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        # ft.Text("Tareas", style=ft.TextThemeStyle.HEADLINE_MEDIUM, color="#FFFFFF"),
                        ft.FilledButton(text="Filled button", on_click=lambda _: router_data.page.go("/")),
                        ft.FilledButton(text="Register", on_click=lambda _: router_data.page.go("/register")),
                        
                        # ft.AppBar(
                        #     leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
                        #     leading_width=40,
                        #     title=ft.Text("Flet Router"),
                        #     center_title=False,
                        #     bgcolor=ft.colors.SURFACE_VARIANT,
                        #     actions=[
                        #         ft.IconButton(ft.icons.HOME, on_click=lambda _: router_data.go('/')),
                        #         ft.IconButton(ft.icons.PERSON_ROUNDED, on_click=lambda _: router_data.go('/profile')),
                        #         ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: router_data.go('/settings'))
                        #     ]
                        # )
                    ],
                ),
            ],
        ),
    )
  
    router_data.page.title = "Home"
    
    return container