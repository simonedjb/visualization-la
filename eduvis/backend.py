import pandas as pd
import numpy as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import users

import V001 as view1
import V002 as view2
import V003 as view3
import V004 as view4
import V005 as view5
import V006 as view6
# import V007 as view7
import V008 as view8
# import V009 as view9
import V010 as view10
# import V011 as view11

class backend:

    user = users.users()
    instance1 = view1.V001()
    instance2 = view2.V002() 
    instance3 = view3.V003() 
    instance4 = view4.V004() 
    instance5 = view5.V005() 
    instance6 = view6.V006() 
    # instance7 = view7.V007()
    instance8 = view8.V008()
    # instance9 = view9.V009() 
    instance10 = view10.V010()
    # instance11 = view11.V011()

    def __init__(self, user,language):
        self.user = user
        self.load_views(language)

    def load_views(self,language="pt"):
        self.instance1 = view1.V001(type_result = "dash",language = language)
        self.instance1.generate_dataset(number_students = 20, number_assigns = 10)

        self.instance2 = view2.V002(type_result = "dash", language = language)
        self.instance2.generate_dataset(number_students = 20)

        self.instance3 = view3.V003(type_result = "dash", language = language)
        self.instance3.generate_dataset(number_students = 20)

        self.instance4 = view4.V004(type_result = "dash", language = language)
        self.instance4.generate_dataset(number_students = 20)

        self.instance5 = view5.V005(type_result = "dash", language = language)
        self.instance5.generate_dataset(number_students = 60)

        self.instance6 = view6.V006(type_result = "dash", language = language)
        self.instance6.generate_dataset(number_students = 60)

        # view7.V007(type_result = "dash", language = language)
        # self.instance7.generate_dataset()

        self.instance8 = view8.V008(type_result = "dash", language = language)
        self.instance8.generate_dataset(number_students=35, number_weeks=7)

        # self.instance9 = view9.V009(type_result = "dash", language = language)
        # self.instance9.generate_dataset()

        self.instance10 = view10.V010(type_result = "dash", language = language)
        self.instance10.generate_dataset(number_students=35, number_video=10)

        # self.instance11 = view11.V011(type_result = "dash", language = language)
        # self.instance11.generate_dataset()

    def get_preference_graph(self,index):
        lst_id_charts = self.user.user_graph_preference("v"+str(index)) #get id charts

        if index == 1:
            view = self.build_view(self.instance1,lst_id_charts,index)
            
        elif index == 2:
            view = self.build_view(self.instance2,lst_id_charts,index)
            
        elif index == 3:
            view = self.build_view(self.instance3,lst_id_charts,index)
            
        elif index == 4:
            view = self.build_view(self.instance4,lst_id_charts,index)
            
        elif index == 5:
            view = self.build_view(self.instance5,lst_id_charts,index)

        elif index == 6:
            view = self.build_view(self.instance6,lst_id_charts,index)

        elif index == 7:
            return html.H1(className="header center orange-text", children=["In developing..."])
            # view = self.build_view(self.instance7,lst_id_charts,index)

        elif index == 8:
            view = self.build_view(self.instance8,lst_id_charts,index)

        elif index == 9:
            return html.H1(className="header center orange-text", children=["In developing..."])
            # view = self.build_view(self.instance9,lst_id_charts,index)

        elif index == 10:
            view = self.build_view(self.instance10,lst_id_charts,index)
        
        elif index == 11:
            return html.H1(className="header center orange-text", children=["In developing..."])
            # view = self.build_view(self.instance11,lst_id_charts,index)

        return html.Div(id="v"+str(index), children=view)
    
    def build_view(self,instance,lst_id_charts,v):
        lst_chart = []
        number_opt = 0
        view = []

        for i in range(0,len(lst_id_charts)): #get id options
            lst_id_options = instance.get_option_index(lst_id_charts[i]) 

            for j in range(0,len(lst_id_options)): #get option layout
                number_opt += 1
                lst_chart.append(self.parser(instance,lst_id_options[j],"option","v"+str(v)+"@o"+str(number_opt)))

            lst_chart.append(self.parser(instance,lst_id_charts[i],"graph")) #append option layout and graph
            
            if i != len(lst_id_charts)-1 :
                lst_chart.append(html.Hr())

            lst_chart.append(html.Br())
            lst_chart.append(html.Br())

            view.append(html.Div(id="v"+str(v)+"@c"+str(i+1),children=lst_chart))
            lst_chart = []

        return view
    
    def parser(self,instance,index,type,id_ref="",values=[]):
        if (type == "graph"):
            if (index == 1):
                return instance.graph_01()
            elif (index == 2):
                return instance.graph_02()
            elif (index == 3):
                return instance.graph_03()
            elif (index == 4):
                return instance.graph_04()
            elif (index == 5):
                return instance.graph_05()
            elif (index == 6):
                return instance.graph_06()
            elif (index == 7):
                return instance.graph_07()
            elif (index == 8):
                return instance.graph_08()
            elif (index == 9):
                return instance.graph_09()
            elif (index == 10):
                return instance.graph_10()
            elif (index == 11):
                return instance.graph_11()
            elif (index == 12):
                return instance.graph_12()
            elif (index == 13):
                return instance.graph_13()
            elif (index == 14):
                return instance.graph_14()
            elif (index == 15):
                return instance.graph_15()
            elif (index == 16):
                return instance.graph_16()
            elif (index == 17):
                return instance.graph_17()
            elif (index == 18):
                return instance.graph_18()
            elif (index == 19):
                return instance.graph_19()
            elif (index == 20):
                return instance.graph_20()
            elif (index == 21):
                return instance.graph_21()
            elif (index == 22):
                return instance.graph_22()
            elif (index == 23):
                return instance.graph_23()
            elif (index == 24):
                return instance.graph_24()
            elif (index == 25):
                return instance.graph_25()
            elif (index == 26):
                return instance.graph_26()
            elif (index == 27):
                return instance.graph_27()
            elif (index == 28):
                return instance.graph_28()
            elif (index == 29):
                return instance.graph_29()
            elif (index == 30):
                return instance.graph_30()
            elif (index == 31):
                return instance.graph_31()
            elif (index == 32):
                return instance.graph_32()
            elif (index == 33):
                return instance.graph_33()
            elif (index == 34):
                return instance.graph_34()
            elif (index == 35):
                return instance.graph_35()
            elif (index == 36):
                return instance.graph_36()
            elif (index == 37):
                return instance.graph_37()
            elif (index == 38):
                return instance.graph_38()
            elif (index == 39):
                return instance.graph_39()
            elif (index == 40):
                return instance.graph_40()
            elif (index == 41):
                return instance.graph_41()
            elif (index == 42):
                return instance.graph_42()
            elif (index == 43):
                return instance.graph_43()
            elif (index == 44):
                return instance.graph_44()
            elif (index == 45):
                return instance.graph_45()
            elif (index == 46):
                return instance.graph_46()
            elif (index == 47):
                return instance.graph_47()
            elif (index == 48):
                return instance.graph_48()
            elif (index == 49):
                return instance.graph_49()
            elif (index == 50):
                return instance.graph_50()
            elif (index == 51):
                return instance.graph_51()
            elif (index == 52):
                return instance.graph_52()
            elif (index == 53):
                return instance.graph_53()
            elif (index == 54):
                return instance.graph_54()
            elif (index == 55):
                return instance.graph_55()
        
        elif (type == "option"):
            if (index == 1):
                return instance.option_01(id_ref)
            elif (index == 2):
                return instance.option_02(id_ref)
            elif (index == 3):
                return instance.option_03(id_ref)
            elif (index == 4):
                return instance.option_04(id_ref)
            elif (index == 5):
                return instance.option_05(id_ref)
            elif (index == 6):
                return instance.option_06(id_ref)
            elif (index == 7):
                return instance.option_07(id_ref)
            elif (index == 8):
                return instance.option_08(id_ref)
            elif (index == 9):
                return instance.option_09(id_ref)
            elif (index == 10):
                return instance.option_10(id_ref)
            elif (index == 11):
                return instance.option_11(id_ref)
            elif (index == 12):
                return instance.option_12(id_ref)
            elif (index == 13):
                return instance.option_13(id_ref)
            elif (index == 14):
                return instance.option_14(id_ref)
            elif (index == 15):
                return instance.option_15(id_ref)
            elif (index == 16):
                return instance.option_16(id_ref)
            elif (index == 17):
                return instance.option_17(id_ref)
            elif (index == 18):
                return instance.option_18(id_ref)
            elif (index == 19):
                return instance.option_19(id_ref)
            elif (index == 20):
                return instance.option_20(id_ref)
            elif (index == 21):
                return instance.option_21(id_ref)
            elif (index == 22):
                return instance.option_22(id_ref)
            elif (index == 23):
                return instance.option_23(id_ref)
            elif (index == 24):
                return instance.option_24(id_ref)
            elif (index == 25):
                return instance.option_25(id_ref)
            elif (index == 26):
                return instance.option_26(id_ref)
            elif (index == 27):
                return instance.option_27(id_ref)
            elif (index == 28):
                return instance.option_28(id_ref)
            elif (index == 29):
                return instance.option_29(id_ref)
            elif (index == 30):
                return instance.option_30(id_ref)
            elif (index == 31):
                return instance.option_31(id_ref)
            elif (index == 32):
                return instance.option_32(id_ref)
            elif (index == 33):
                return instance.option_33(id_ref)
            elif (index == 34):
                return instance.option_34(id_ref)
            elif (index == 35):
                return instance.option_35(id_ref)
            elif (index == 36):
                return instance.option_36(id_ref)
            elif (index == 37):
                return instance.option_37(id_ref)
            elif (index == 38):
                return instance.option_38(id_ref)
            elif (index == 39):
                return instance.option_39(id_ref)
            elif (index == 40):
                return instance.option_40(id_ref)
            elif (index == 41):
                return instance.option_41(id_ref)
            elif (index == 42):
                return instance.option_42(id_ref)
            elif (index == 43):
                return instance.option_43(id_ref)
            elif (index == 44):
                return instance.option_44(id_ref)
            elif (index == 45):
                return instance.option_45(id_ref)
            elif (index == 46):
                return instance.option_46(id_ref)
            elif (index == 47):
                return instance.option_47(id_ref)
            elif (index == 48):
                return instance.option_48(id_ref)
            elif (index == 49):
                return instance.option_49(id_ref)
            elif (index == 50):
                return instance.option_50(id_ref)
            elif (index == 51):
                return instance.option_51(id_ref)
            elif (index == 52):
                return instance.option_52(id_ref)
            elif (index == 53):
                return instance.option_53(id_ref)
            elif (index == 54):
                return instance.option_54(id_ref)
            elif (index == 55):
                return instance.option_55(id_ref)

