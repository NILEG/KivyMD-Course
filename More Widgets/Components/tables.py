from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen


class Interface(MDScreen):
    price=0
    def __init__(self, **kwargs):
        super(Interface, self).__init__(**kwargs)
        column_data=[("Serial #",dp(30)),("Status", dp(30)), ("Product", dp(30)), ("Category", dp(30)), ("Seller",dp(30)), ("Price($$)", dp(30))]
        row_data=[("001",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"),"Mouse", "Electronics", "JK Computers", "20"),
                  ("002",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"),"Mouse", "Electronics", "JK Computers", "30"),
                  ("003",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"), "Mouse", "Electronics", "JK Computers", "50"),
                  ("004",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"), "Mouse", "Electronics", "JK Computers", "20"),
                  ("005",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"), "Mouse", "Electronics", "JK Computers", "20"),
                  ("006",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"), "Mouse", "Electronics", "JK Computers", "20"),
                  ("007",("checkbox-blank-circle-outline", [0.5,0,0.5,1], "Unchecked"), "Mouse", "Electronics", "JK Computers", "20")]
        self.data_table=MDDataTable(column_data=column_data, row_data=row_data, size_hint=(None,None), size=(dp(600), dp(300)),
                               pos_hint={"center_x":0.5, "center_y":0.5},elevation=2,
                               background_color_selected_cell="e4514f",
                               rows_num=10)
        self.data_table.bind(on_row_press=self.row_press)
        self.add_widget(self.data_table)
    def row_press(self, table, row_item):
        #print(row_item.text)
        index=row_item.index//6
        data=self.data_table.row_data[index]
        if(data[1][0]=="checkbox-blank-circle-outline"):
            self.data_table.update_row(data, [data[0],("checkbox-marked-circle-outline", [0.5, 0, 0.5, 1], "Checked"),data[2], data[3], data[4], data[5]])
            Interface.price+=int(data[5])
        else:
            self.data_table.update_row(data, [data[0], ("checkbox-blank-circle-outline", [0.5, 0, 0.5, 1], "Unchecked"),
                                              data[2], data[3], data[4], data[5]])
            Interface.price -= int(data[5])
        self.ids.label.text=str(Interface.price)
class TableApp(MDApp):
    pass

TableApp().run()