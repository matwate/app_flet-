from typing import Callable, Any
import flet as ft
from enum import Enum



class Router:
    def __init__(self):
        self.data = dict()
        self.routes = {}
        self.body = ft.Container(
            alignment=ft.alignment.center,
            expand=True,bgcolor="yellow")

    def set_route(self, stub: str, view: Callable):
        self.routes[stub] = view
    
    def set_routes(self, route_dictionary: dict):
        """Sets multiple routes at once. Ex: {"/": IndexView }"""
        self.routes.update(route_dictionary)

    def route_change(self, route):
        _page = route.route.split("?")[0]

        self.body.content = self.routes[_page](self)
        self.body.update()

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def get_query(self, key):
        return self.data.get(key)

