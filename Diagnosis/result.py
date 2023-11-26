from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<Result>:
    MDTopAppBar:
        pos_hint: {"top":1}
        md_bg_color: app.theme_cls.accent_light
        left_action_items: [["arrow-left-bold", lambda x: root.back()]]
        specific_text_color: app.theme_cls.primary_color
        elevation: 0
    MDLabel:
        text: "Opto App"
        adaptive_size: True
        pos_hint: {"center_x":0.5, "top":0.9}
        font_size: '64sp'
        font_name: "stylish_font.ttf"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
    MDBoxLayout:
        id: placeholder
        orientation: "vertical"
        padding: [dp(30),dp(30),dp(30),dp(100)]
        spacing: dp(10)
        MDLabel:
            text: "Results"
            adaptive_size: True
            pos_hint: {"center_x":0.5}
            font_size: '18sp'
            bold: True
""")
class Result(MDScreen):
    result=[]
    @staticmethod
    def set_result(result):
        Result.result=result
    def on_pre_enter(self, *args):
        childs=self.ids.placeholder.children
        if(len(childs)>1):
            self.ids.placeholder.remove_widget(childs[0])
        column_data=[("Name", dp(40)), ("Percentage", dp(30))]
        data_table = MDDataTable(column_data=column_data, row_data=Result.result, size_hint=(None, None),
                                 size=(dp(350), dp(300)),
                                 pos_hint={"center_x": 0.5}, elevation=2,
                                 background_color_header="#E91E63",
                                 rows_num=15)
        self.ids.placeholder.add_widget(data_table)
    def back(self):
        self.manager.current="home"