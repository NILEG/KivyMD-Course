from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineAvatarListItem, OneLineIconListItem
from kivymd.uix.snackbar import Snackbar


class Content(MDBoxLayout):
    pass
class CustomItem(OneLineIconListItem):
    my_text=StringProperty()
    my_icon=StringProperty()
class DiaInterface(MDFloatLayout):
    def getData(self, obj):
        name=self.dialog.content_cls.ids.name.text
        email=self.dialog.content_cls.ids.email.text
        self.dialog.dismiss()
        Snackbar(text=name+" "+email,snackbar_x="10dp", snackbar_y="10dp", size_hint_x=None, width=dp(400), pos_hint={"center_x":0.5}, buttons=[MDFlatButton(text="Undo")]).open()
    def hide_dialog(self, obj):
        self.dialog.dismiss()
    def quit(self, obj):
        MDApp.get_running_app().stop()
    def show_dialog(self):
        #self.dialog=MDDialog(title="Quit App", text="Are you sure?", buttons=[MDFlatButton(text="Yes", on_press=self.quit), MDRaisedButton(text="No", on_press=self.hide_dialog)])
        #self.dialog=MDDialog(title="Lists",type="simple", items=[CustomItem(my_text="This is the list", my_icon="android"),CustomItem(my_text="This is the list", my_icon="pencil"),CustomItem(my_text="This is the list", my_icon="language-python")])
        self.dialog=MDDialog(title="Information", type="custom",content_cls=Content(), buttons=[MDRaisedButton(text="Submit",on_press=self.getData)])
        self.dialog.open()
class DiaApp(MDApp):
    pass

DiaApp().run()