from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.screen import MDScreen

class CardSwipe(MDCardSwipe):
    def delete(self, obj):
        MDApp.get_running_app().root.ids.gridlayout.remove_widget(obj)
class Interface(MDScreen):
    def create(self):
        card=CardSwipe()
        self.ids.gridlayout.add_widget(card)


class CardApp(MDApp):
    pass

CardApp().run()