from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.list import OneLineListItem
from kivymd.uix.relativelayout import MDRelativeLayout

Builder.load_string("""
<CustomProgressBar>:
    id: pb
    size_hint_y:None
    height: dp(20)
    canvas:
        BorderImage:
            border:0,0,0,0
            pos: pb.x, pb.center_y-root.bgBarHeight/2
            size: self.width, root.bgBarHeight
            source: root.background_image
        BorderImage:
            pos: pb.x, pb.center_y - root.fgBarHeight/2
            border:0,0,0,0
            size: pb.width * (pb.value / float(pb.max)), root.fgBarHeight
            source: root.foreground_image
    Label:
        text: str(int(pb.value))+"%" if root.showProgress else ""
        pos: pb.center_x-self.texture_size[0]/2,pb.center_y-self.texture_size[1]/2
        size: self.texture_size
        color:root.textColor
        font_size: root.fontSize
<Custom_ProgressBar>:
    size_hint_y:None
    height: progressbar.height
    MDProgressBar:
        id: progressbar
        size_hint_y:None
        height: dp(20)
        color: app.theme_cls.primary_light
        value: root.progress_value
    MDLabel:
        size_hint_y:None
        height: self.texture_size[1]
        halign: "center"
        text: root.label_text
        bold: True
        
        
<CustomTextField>:
    size_hint_y:None
    height: textfield.height
    MDTextField:
        id: textfield
        hint_text:root._hint
        password: True
    MDIconButton:
        pos_hint: {"right":1, "center_y":0.5}
        icon: "eye-off"
        theme_icon_color:"Custom"
        icon_color: app.theme_cls.primary_color
        on_press:
            self.icon = "eye" if self.icon=="eye-off" else "eye-off"
            textfield.password=False if self.icon=="eye" else True
<DCard>:
    size_hint:None,None
    size: dp(120), dp(150)
    MyAnchorLayout:
        elevation: 1
        size_hint:None, None
        size: dp(100), dp(110)
        pos_hint: {"center_x":0.5}
        md_bg_color: "white"
        anchor_x:"center"
        anchor_y:"center"
        MDIcon:
            icon: root.icon_name
            font_size: '72sp'
            color: app.theme_cls.primary_color
    MyAnchorLayout:
        elevation: 1
        size_hint_y:None
        height: dp(40)
        pos_hint: {"top":1}
        md_bg_color: app.theme_cls.primary_color
        radius: dp(5)
        MDLabel:
            halign: "center"
            text: root.name
            theme_text_color: "Custom"
            text_color: "white"
            bold: True
    
        

""")
class CustomTextField(MDRelativeLayout):
    _hint=StringProperty()

class Custom_ProgressBar(MDRelativeLayout):
    progress_value=NumericProperty(0)
    label_text=StringProperty("0")
class CustomProgressBar(ProgressBar):
    background_image = StringProperty("") #Background Image used as Color
    foreground_image = StringProperty("")#Foreground Image used as Color
    bgBarHeight = NumericProperty(dp(10))#Height of background Image
    fgBarHeight = NumericProperty(dp(10))#Height of foreground Image
    fontSize=NumericProperty(dp(10))#Font Size of Progress Text
    showProgress=BooleanProperty(False)#Progress Text will be visible only if showProgress Property is true
    textColor=ListProperty([0,0,0,1])#Color of the Progress Text

class MyAnchorLayout(CommonElevationBehavior, MDAnchorLayout):
    pass
class DCard(ButtonBehavior, MDRelativeLayout):
    name=StringProperty()
    icon_name=StringProperty()

class CustomItem(OneLineListItem):
    entry_id=NumericProperty()

