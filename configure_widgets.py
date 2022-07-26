import tkinter as tk
from tkinter import ttk


class Conf_widgts:

    ENRTY_WIDTH = 3
    ENTRY_FONT = 2

    # generate entry window for values of deegres, minutes, seconds
    def generate_value_entry(self, frameLabName):

        self.list_entrys = []
        self.list_lab_symbols = []

        for i in range(3):
            self.list_entrys.append(
                ttk.Entry(frameLabName, justify=tk.LEFT, width=self.ENRTY_WIDTH))

        for i in range(len(self.list_entrys)):
            self.list_lab_symbols.append(
                ttk.Label(frameLabName, text=f'{self.SYMBOLS_LIST[i]}', font=self.ENTRY_FONT))

        for i in range(len(self.list_entrys)):
            self.list_entrys[i].pack(side=tk.LEFT)
            self.list_lab_symbols[i].pack(side=tk.LEFT)

    # command for window mode buttons
    def configure_win(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()
