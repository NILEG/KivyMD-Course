from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox

class CustomRightItem2(IRightBodyTouch, MDBoxLayout):
    pass
class CustomRightItem(IRightBodyTouch, MDCheckbox):
    pass
class Interface(MDScreen):
    def close(self):
        print("Closing")
    def print_text(self, obj):
        print(obj.text)
class CompApp(MDApp):
    pass

CompApp().run()