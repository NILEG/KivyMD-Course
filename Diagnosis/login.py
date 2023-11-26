from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from database import Database
Builder.load_string("""
<Login>:
#:import CustomTextField customwidgets
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(75)
        padding: dp(50)
        MDBoxLayout:
            size_hint_y:0.35
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
                    id: email
                    size_hint_x:None
                    width: dp(300)
                    hint_text: "Email"
                    validator: "email"
                    error_color: app.theme_cls.primary_light
                CustomTextField:
                    id: password
                    size_hint_x:None
                    width: dp(300)
                    _hint: "Password"
                MDBoxLayout:
                    adaptive_size: True
                    pos_hint: {"right":1}
                    padding: [0,dp(20),0,0]
                    spacing: dp(20)
                    MDFlatButton:
                        text: "Signup"
                        on_press: root.move_to_signup()
                    MDRaisedButton:
                        text: "Login"
                        on_press: root.login()
                
""")

class Login(MDScreen):
    email=""
    def move_to_signup(self):
        self.manager.current="signup"
    def login(self):
        email=self.ids.email.text
        password=self.ids.password.ids.textfield.text
        if(Database.is_Exsist(email, password)):
            Login.email=email
            self.manager.current="home"
        else:
            print("Failed")