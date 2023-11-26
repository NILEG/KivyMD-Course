from kivy.clock import Clock
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

class Header(MDBoxLayout):
    pass
class Interface(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_menu)
    def create_menu(self, *args):
        menu_item = [{"viewclass": "OneLineListItem", "height": dp(54), "text": "Account",
                      "on_press": lambda x="Account": self.item_click(x)},
                     {"viewclass": "OneLineListItem", "height": dp(54), "text": "Settings",
                      "on_press": lambda x="Settings": self.item_click(x)},
                     {"viewclass": "OneLineListItem", "height": dp(54), "text": "Purchases",
                      "on_press": lambda x="Purchases": self.item_click(x)}]
        self.menu = MDDropdownMenu(header_cls=Header(), caller=self.ids.topappbar, items=menu_item, width_mult=4, max_height=dp(120))
    def item_click(self, item):
        print(f"{item} Clicked")
    def show_menu(self, obj):
        self.menu.open()
class MenApp(MDApp):
    pass


MenApp().run()