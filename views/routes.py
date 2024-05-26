from views.Router import Router
from views.index_view import IndexView
from views.settings_view import SettingsView
from views.screen_lock import Screen_lock
from views.register import Register
from views.home import Home_page

router = Router()

router.routes = {
  "/screen_lock": Screen_lock,
  "/home": Home_page,
  "/": IndexView,
  "/settings": SettingsView,
  "/register": Register,

}