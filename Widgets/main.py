from kivy.properties import DictProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import RiseInTransition

class Screen_1(MDScreen):
    pass

class Screen_2(MDScreen):
    pass

class Screen_3(MDScreen):
    pass
class Interface_3(MDBoxLayout):
    def back(self):
        print("Back Action")
    def right_action(self, x):
        print(x.icon)
class CustomTextField(MDRelativeLayout):
    pass
class Intercae_2(MDFloatLayout):
    data=DictProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data={"Copy": ["content-copy", "on_press", lambda x: self.copying()], "Printer": ["printer", "on_press", lambda x: self.printing()], "Share": ["share-variant", "on_press", lambda x: self.share()]}
    def copying(self):
        print("Copying")
    def printing(self):
        print("Printing")
    def share(self):
        print("Sharing")
class Interface(MDFloatLayout):
    pass
class WidgetsApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Amber"
        self.theme_cls.accent_palette="Gray"
        self.theme_cls.accent_hue="900"
        self.theme_cls.material_style="M2"
        self.theme_cls.theme_style="Dark"

WidgetsApp().run()