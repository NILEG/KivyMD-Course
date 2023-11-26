from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.screen import MDScreen

class Tile(MDSmartTile):
    txt=StringProperty()
    img=StringProperty()
class Interface(MDScreen):
    def check_favourite(self):
        self.ids.stacklayout2.clear_widgets()
        tiles=self.ids.stacklayout1.children
        for tile in tiles:
            if tile.ids.iconbutton.icon=="heart":
                self.ids.stacklayout2.add_widget(Tile(txt=tile.txt, img=tile.img))
class ImglstApp(MDApp):
    pass

ImglstApp().run()