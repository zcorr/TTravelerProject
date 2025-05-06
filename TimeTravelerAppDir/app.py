# app.py
# ------
import tkinter as tk
from constants import *
from data import *
from pages import (make_add_new_page, traveler_form,
                   trip_form, companion_form, placeholder)

class TravelersApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Time Travelers App")
        self.configure(bg=MENU_BG)
        self.minsize(820, 520)

        # Ensure radiobuttons honour MENU_FONT (macOS / Aqua quirk)
        self.option_add("*Radiobutton.font", MENU_FONT)

        self.selected_menu = tk.StringVar(value=MENU_LABELS[0])

        self._build_menu_bar()
        self._build_pages()
        self._show_page(MENU_LABELS[0])

    # -- Menu bar --------------------------------------------------
    def _build_menu_bar(self):
        bar = tk.Frame(self, bg=MENU_BG); bar.pack(side="top", fill="x")

        tk.Label(bar, text="TRAVELERS APP",
                 font=TITLE_FONT, bg=MENU_BG, fg="black").pack(side="left", padx=(12,30))

        for lbl in MENU_LABELS:
            rb = tk.Radiobutton(
                bar, text=lbl,
                variable=self.selected_menu, value=lbl,
                indicatoron=0, bd=2, relief="ridge",
                bg=MENU_BUTTON_BG, selectcolor=MENU_SELECTED_BG,
                fg="black", width=12,
                command=lambda l=lbl: self._show_page(l)
            )
            rb.pack(side="left", padx=5, pady=6)

        tk.Frame(self, height=2, bg="black").pack(fill="x")

    # -- Page stack ------------------------------------------------
    def _build_pages(self):
        stack = tk.Frame(self, bg="white"); stack.pack(expand=True, fill="both")
        stack.grid_rowconfigure(0, weight=1); stack.grid_columnconfigure(0, weight=1)

        self.pages = {
            "ADD NEW"      : make_add_new_page(
                                stack,
                                on_trip      = lambda: self._show_page("ADD TRIP"),
                                on_traveler  = lambda: self._show_page("ADD TRAVELER"),
                                on_companion = lambda: self._show_page("ADD COMPANION")
                             ),
            "ADD TRAVELER" : traveler_form(stack),
            "ADD TRIP"     : trip_form(stack, TRAVELERS),
            "ADD COMPANION": companion_form(stack, TRAVELERS),
            "EDIT"         : placeholder(stack, "EDIT"),
            "VIEW"         : placeholder(stack, "VIEW"),
            "EXPORT"       : placeholder(stack, "EXPORT"),
        }

        for p in self.pages.values():
            p.grid(row=0, column=0, sticky="nsew")

    # -- Page switcher --------------------------------------------
    def _show_page(self, key):
        self.selected_menu.set(key)
        self.pages[key].tkraise()
