import tkinter as tk
import sys
from tkinter import CENTER, LEFT, ttk
from configure_widgets import Conf_widgts as Cw
from logic import Logic_for_widgets as lfw
import pyperclip as pc


class App(tk.Tk, Cw, lfw):

    SYMBOLS_LIST = ['°', "'", "''"]

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title('Куркулятор градусів')

        self.set_ui()

    def set_ui(self):

        # exit button
        exit_btn = ttk.Button(self, text='Exit', command=self.stop_app)
        exit_btn.pack(fill=tk.X)

        # 1-st frame of values
        self.values1_frame = ttk.LabelFrame(
            self, text='Input 1-st value')
        self.values1_frame.pack(fill=tk.X)
        # from configure_widgets
        self.generate_value_entry(self.values1_frame)

        # frame of operations
        self.operation_lab = ttk.LabelFrame(self, text='choose the operation')
        self.operation_lab.pack(fill=tk.X)

        self.operation_box = ttk.Combobox(self.operation_lab, values=[
                                          '+', '-'], state='readonly',
                                          width=9)
        self.operation_box.current(0)
        self.operation_box.pack(anchor=tk.CENTER)

        # 2-nd frame of values
        self.values2_frame = ttk.LabelFrame(
            self, text='Input 2-nd value')
        self.values2_frame.pack(fill=tk.X)
        # from configure_widgets
        self.generate_value_entry(self.values2_frame)

        # math button
        self.math_btn = ttk.Button(
            self, text='Math!', command=self.count_deegres)
        self.math_btn.pack(anchor=tk.CENTER)

        # result labelframe
        self.result_lab_frame = ttk.LabelFrame(self, text='Result')
        self.result_lab_frame.pack(fill=tk.X)

        # window mode frame, mode buttons, window mode's
        self.window_lab = ttk.LabelFrame(self, text='Window mode(manual)')
        self.window_lab.pack(fill=tk.X)
        self.mode_box = ttk.Combobox(self.window_lab, values=[
                                     'hide', "don't hide"],
                                     state='readonly')
        self.mode_box.current(1)
        self.mode_box.pack(side=tk.LEFT)
        ttk.Button(self.window_lab, text='move',
                   command=self.configure_win).pack(side=tk.LEFT)
        ttk.Button(self.window_lab, text='copy result',
                   command=self.copy_result).pack(side=tk.LEFT)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)

    def stop_app(self):
        self.destroy()
        sys.exit()

    def enter_mouse(self, event):
        if self.mode_box.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.mode_box.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def copy_result(self):
        pc.copy(self.result_lab_frame.winfo_children()[0].cget('text') +
                self.result_lab_frame.winfo_children()[1].cget('text') +
                self.result_lab_frame.winfo_children()[2].cget('text'))


if __name__ == '__main__':
    root = App()
    root.mainloop()
