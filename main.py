from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout

class ThemeInterface(MDBoxLayout):
    pass
class LayoutInterface(MDBoxLayout):
    pass
class Interface(MDFloatLayout):
    pass
class TestApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Orange"
        self.theme_cls.accent_palette="Gray"
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.primary_dark_hue="900"
        self.theme_cls.primary_light_hue="200"

TestApp().run()
