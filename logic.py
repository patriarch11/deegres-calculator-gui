import tkinter as tk
from tkinter import ttk


class Logic_for_widgets:

    MAX_COUNT_MINUTES_SECONDS = 60.0

    def clear(self):
        temp = self.result_lab_frame.winfo_children()
        if len(temp) > 0:
            for i in range(len(temp)):
                temp[i].destroy()

    def values_audit(self, audit_list, type_audit):
        if type_audit == 'type':
            for i in range(len(audit_list)):
                try:
                    p = float(audit_list[i])
                except:
                    ttk.Label(
                        self.result_lab_frame,
                        text=f'type error',
                        background='red').pack(side=tk.LEFT)
                    break
        elif type_audit == 'values':
            for i in range(len(audit_list)-1):
                if float(audit_list[i+1]) >= self.MAX_COUNT_MINUTES_SECONDS:
                    ttk.Label(
                        self.result_lab_frame,
                        text='minutes/seconds can\'t be 60 and bigger',
                        background='red').pack(side=tk.LEFT)
                    return False
            return True

    def count_deegres(self):

        # udpade result label
        self.clear()
        # get values lists
        firts_values_list = [self.values1_frame.winfo_children()[0].get(),
                             self.values1_frame.winfo_children()[1].get(),
                             self.values1_frame.winfo_children()[2].get()]
        second_values_list = [self.values2_frame.winfo_children()[0].get(),
                              self.values2_frame.winfo_children()[1].get(),
                              self.values2_frame.winfo_children()[2].get()]
        # type audit
        self.values_audit(firts_values_list, 'type')
        self.values_audit(second_values_list, 'type')
        # values audit
        if self.values_audit(firts_values_list, 'values') and \
                self.values_audit(second_values_list, 'values') == True:
            # conver to float for calculation
            deegres1 = float(firts_values_list[0])
            minutes1 = float(firts_values_list[1])
            seconds1 = float(firts_values_list[2])
            deegres2 = float(second_values_list[0])
            minutes2 = float(second_values_list[1])
            seconds2 = float(second_values_list[2])

            res_deegres = 0
            res_minutes = 0
            res_seconds = 0

            # calculating
            if self.operation_box.current() == 0:
                res_deegres = deegres1 + deegres2
                res_minutes = minutes1 + minutes2
                res_seconds = seconds1 + seconds2
                if res_minutes > 60:
                    res_minutes -= 60
                    res_deegres += 1
                if res_seconds > 60:
                    res_seconds -= 60
                    res_minutes += 1
            elif self.operation_box.current() == 1:
                if minutes1 < minutes2:
                    deegres1 -= 1
                    minutes1 += 60
                if seconds1 < seconds2:
                    minutes1 -= 1
                    s1 += 60
                res_deegres = deegres1 - deegres2
                res_minutes = minutes1 - minutes2
                res_seconds = seconds1 - seconds2

            res_list = [res_deegres, res_minutes, res_seconds]
            # packing result
            for i in range(len(res_list)):
                ttk.Label(self.result_lab_frame,
                          text=f'{res_list[i]}{self.SYMBOLS_LIST[i]}').pack(side=tk.LEFT)
