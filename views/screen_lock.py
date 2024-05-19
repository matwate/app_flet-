from typing import Union
import flet as ft
from views.Router import Router, DataStrategyEnum
from State import global_state, State
import threading
import math

def Screen_lock(router_data: Union[Router, str, None] = None):
    # def animate(e):
    #     c.content = c2 if c.content == c1 else c1
    #     c.update()
    def change_page():
        router_data.page.go("/")
        # router_data.body.update()
        # router_data.page.window_destroy()
        # router_data.page.update()

    timer = threading.Timer(2, change_page)

# Inicia el temporizador
    timer.start()

    
    conteiner = ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.Alignment(0.8, 1),
                colors=[
                    "0xff1f005c",
                    "0xff5b0060",
                    "0xff870160",
                    "0xffac255e",
                    "0xffca485c",
                    "0xffe16b5c",
                    "0xfff39060",
                    "0xffffb56b",
                ],
                tile_mode=ft.GradientTileMode.MIRROR,
                rotation=math.pi / 3,
            ),
            width=150,
            height=150,
            border_radius=5,
        )
    
  
    router_data.page.title = "screen_lock"
    # router_data.page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    return conteiner