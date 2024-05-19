from views.Router import Router, DataStrategyEnum
from views.index_view import IndexView
from views.settings_view import SettingsView

from views.screen_lock import Screen_lock
router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/screen_lock": Screen_lock,
  # "/home": Screen_lock,
  "/": IndexView,
  "/settings": SettingsView
}