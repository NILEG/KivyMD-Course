from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from database import Database
Builder.load_string("""
#:import CustomTextField customwidgets
<Signup>:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(50)
        MDBoxLayout:
            size_hint_y:0.25
            MDLabel:
                text: "Opto App"
                halign: "center"
                font_size: '64sp'
                font_name: "stylish_font.ttf"
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
        MDAnchorLayout:
            anchor_x:"center"
            anchor_y: "top"
            MDBoxLayout:
                orientation: "vertical"
                adaptive_size: True
                MDTextField:
                    id: name
                    hint_text: "Name"
                    size_hint_x: None
                    width: dp(300)
                MDTextField:
                    id: email
                    hint_text: "Email"
                    size_hint_x: None
                    width: dp(300)
                    validator: "email"
                    error_color: app.theme_cls.primary_light
                CustomTextField:
                    id: password
                    _hint: "Password"
                    size_hint_x: None
                    width: dp(300)
                CustomTextField:
                    id: cpassword
                    _hint: "Confirm Password"
                    size_hint_x: None
                    width: dp(300)
                MDBoxLayout:
                    padding: [0,dp(20),0,0]
                    pos_hint: {"right":1}
                    adaptive_size: True
                    MDRaisedButton:
                        text: "Sign up"
                        on_press: root.signup()
        
""")
class Signup(MDScreen):
    def signup(self):
        name=self.ids.name.text
        email=self.ids.email.text
        password=self.ids.password.ids.textfield.text
        cpassword=self.ids.cpassword.ids.textfield.text
        if(Database.is_Valid(email) and password==cpassword and password!=""):
            Database.insert_into_user(email, password, name)