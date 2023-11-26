from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
import json
from result import Result
from database import Database
from login import Login
Builder.load_string("""
#:import Custom_ProgressBar customwidgets
<QuestionPage>:
    MDLabel:
        pos_hint: {"center_x":0.5, "top":0.9}
        adaptive_size: True
        text: "Opto App"
        font_size: '64sp'
        font_name: "stylish_font.ttf"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    MDAnchorLayout:
        anchor_x: "center"
        anchor_y: "center"
        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            size_hint_x:0.7
            spacing: dp(10)
            MDLabel:
                id: label
                text: "Are the headache uniliteral or Bilaterial?"
                font_size: '18sp'
                theme_text_color: "Custom"
                text_color: app.theme_cls.primary_color
                height: dp(100)
                size_hint_y:None
            MDRaisedButton:
                id: option1
                elevation: 2
                text: "Option 1"
                padding: [dp(100),0,dp(100),0]
                md_bg_color: app.theme_cls.accent_color
                pos_hint: {"center_x":0.5}
                on_press: root.option_selection(self.text)
            MDRaisedButton:
                id: option2
                elevation: 2
                text: "Option 2"
                padding: [dp(100),0,dp(100),0]
                md_bg_color: app.theme_cls.accent_color
                pos_hint: {"center_x":0.5}
                on_press: root.option_selection(self.text)
    CustomProgressBar:
        id:progressbar
        size_hint_x:0.8
        pos_hint: {"center_x":0.5, "y":0.05}
        background_image: "gray.png"
        foreground_image: "pink.png"
        bgBarHeight: dp(15)
        fgBarHeight: dp(15)
        showProgress:True
        fontSize: '15sp'
        textColor: [0,0,0,0.6]
        value:0
""")
class QuestionPage(MDScreen):
    data=dict()
    questions=list()
    counter=0
    lst=list()
    result=list()
    @staticmethod
    def set_file(filename):
        file=open(filename)
        QuestionPage.data=json.load(file)
        QuestionPage.questions=QuestionPage.data["Questions"]
        QuestionPage.counter=0
        QuestionPage.lst=[]
    def on_pre_enter(self, *args):
        self.next_question()
    def next_question(self):
        question=QuestionPage.questions[QuestionPage.counter]
        keys=list(QuestionPage.data[question].keys())
        self.ids.label.text=question
        self.ids.option1.text=keys[0]
        self.ids.option2.text = keys[1]
        self.ids.progressbar.value=int((QuestionPage.counter/len(QuestionPage.questions))*100)
    def option_selection(self, key):
        value=QuestionPage.data[self.ids.label.text][key]
        QuestionPage.lst+=value
        if(QuestionPage.counter<len(QuestionPage.questions)-1):
            QuestionPage.counter+=1
            self.next_question()
        else:
            self.calculate_result()
            Result.set_result(QuestionPage.result)
            self.save_history()
            self.manager.current="result"
    def calculate_result(self):
        uniques=set(QuestionPage.lst)
        for unique in uniques:
            percentage=f"{round((QuestionPage.lst.count(unique)/len(QuestionPage.lst))*100, 2)}%"
            QuestionPage.result.append((unique, percentage))
        print(QuestionPage.result)
    def save_history(self):
        Database.insert_into_entries(Login.email, QuestionPage.data["Name"])
        entry_id=Database.get_last_entry_id(Login.email)[0]
        for item in QuestionPage.result:
            Database.insert_into_data_table(entry_id, Login.email, item[0], item[1])
