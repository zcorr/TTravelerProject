# pages.py
# --------
import tkinter as tk
from constants import *

def make_add_new_page(parent, on_trip, on_traveler, on_companion):
    page = tk.Frame(parent, bg=MENU_BG)
    tk.Label(page, text="Add a new ...",
             font=HEADER_FONT,
             bg=MENU_BG, fg="black").pack(pady=(25, 10))

    box = tk.Frame(page, bg=MENU_BG)
    box.pack(pady=10)

    btn_opts = dict(font=BIG_BTN_FONT, width=12, height=6,
                    bd=3, relief="raised")
    tk.Button(box, text="TRIP", **btn_opts, command=on_trip).pack(side="left", padx=30)
    tk.Button(box, text="TRAVELER", **btn_opts, command=on_traveler).pack(side="left", padx=30)
    tk.Button(box, text="COMPANION", **btn_opts, command=on_companion).pack(side="left", padx=30)
    return page


def traveler_form(parent):
    from constants import HEADER_FONT
    frame = tk.Frame(parent, bg=PAGE_BG)
    tk.Label(frame, text="ADD A NEW TRAVELER",
             font=HEADER_FONT,
             fg="black",bg=MENU_BG).pack(pady=(25, 15))

    form = tk.Frame(frame, bg=MENU_BG)
    form.pack()

    def row(r, text):
        tk.Label(form, text=text, bg=MENU_BG, fg="black", anchor="w").grid(row=r, column=0, sticky="w", pady=6)

    row(0, "Name");          tk.Entry(form, width=40).grid(row=1, column=0, pady=(0,10))
    row(2, "Age");           tk.Entry(form, width=40).grid(row=3, column=0, pady=(0,10))
    row(4, "Birth Location");tk.Entry(form, width=40).grid(row=5, column=0, pady=(0,10))
    return frame


def trip_form(parent, travelers):
    from constants import HEADER_FONT
    frame = tk.Frame(parent, bg=PAGE_BG )
    tk.Label(frame, text="ADD A NEW TRIP",
             font=HEADER_FONT, fg="black", bg=MENU_BG).pack(pady=(25, 15))

    form = tk.Frame(frame, bg=MENU_BG); form.pack()

    def row(r, text):
        tk.Label(form, text=text, bg=MENU_BG, fg="black", anchor="w").grid(row=r, column=0, sticky="w", pady=6)

    # Traveler dropdown
    row(0, "Select Traveler")
    var = tk.StringVar(value=travelers[0])
    tk.OptionMenu(form, var, *travelers).grid(row=1, column=0, sticky="we", pady=(0,10))

    row(2, "Trip Date"); tk.Entry(form, width=40).grid(row=3, column=0, pady=(0,10))
    row(4, "Location");  tk.Entry(form, width=40).grid(row=5, column=0, pady=(0,10))
    row(6, "Image File");tk.Entry(form, width=40).grid(row=7, column=0, pady=(0,10))
    return frame


def companion_form(parent, travelers):
    from constants import HEADER_FONT
    frame = tk.Frame(parent, bg=MENU_BG)
    tk.Label(frame, text="ADD A NEW COMPANION",
             font=HEADER_FONT, fg="black", bg=MENU_BG).pack(pady=(25, 15))

    form = tk.Frame(frame, bg=MENU_BG); form.pack()

    def row(r, text):
        tk.Label(form, text=text, bg=MENU_BG, fg="black", anchor="w").grid(row=r, column=0, sticky="w", pady=6)

    # Traveler dropdown
    row(0, "Select Traveler")
    tvar = tk.StringVar(value=travelers[0])
    tk.OptionMenu(form, tvar, *travelers).grid(row=1, column=0, sticky="we", pady=(0,10))

    row(2, "Name");             tk.Entry(form, width=40).grid(row=3, column=0, pady=(0,10))
    row(4, "Age");              tk.Entry(form, width=40).grid(row=5, column=0, pady=(0,10))
    row(6, "Original Location");tk.Entry(form, width=40).grid(row=7, column=0, pady=(0,10))
    return frame


def placeholder(parent, label):
    from constants import HEADER_FONT
    f = tk.Frame(parent, bg="white")
    tk.Label(f, text=f"{label} PAGE",
             font=HEADER_FONT, bg="white", fg="black").pack(expand=True)
    return f
