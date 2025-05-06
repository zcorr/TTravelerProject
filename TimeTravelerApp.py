import tkinter as tk

class TravelersApp(tk.Tk):
    # --- tweak this one line and every menu-button will follow ---
    MENU_FONT   = ("Comic Sans MS", 16, "bold")          # try: ("Comic Sans MS", 11, "normal")
    MENU_LABELS = ("ADD NEW", "EDIT", "VIEW", "EXPORT")

    def __init__(self):
        super().__init__()
        self.title("Travelers App")
        self.configure(bg="white")
        self.minsize(820, 520)

        # ***** one line that makes the font change actually stick *****
        self.option_add("*Radiobutton.font", self.MENU_FONT)   # on Aqua, overrides the default


        self.selected_menu = tk.StringVar(value="ADD NEW")

        companions_string = "Bob, Alice, Charlie, Dave, Eve, Frank, Grace, Heidi, Ivan, Judy"
        companions_list = companions_string.split(", ")
        self.companions    = companions_list

        travelers_string = "First Doctor, Second Doctor, Third Doctor, Fourth Doctor, Fifth Doctor, Sixth Doctor, Seventh Doctor, Eighth Doctor, Ninth Doctor, Tenth Doctor"
        travelers_list = travelers_string.split(", ")
        self.travelers = travelers_list

        self._build_menu_bar()
        self._build_pages()
        self._show_page("ADD NEW")            # <-- landing page

    # ───────────────────────── top bar ─────────────────────────
    def _build_menu_bar(self):
        bar = tk.Frame(self, bg="white")
        bar.pack(side="top", fill="x")

        tk.Label(bar, text="TRAVELERS APP",
                 font=("Comic Sans MS", 14, "bold"),   # just this one heading
                 bg="white", fg="black").pack(side="left", padx=(12, 30))

        self.menu_btns = {}
        for lbl in self.MENU_LABELS:
            rb = tk.Radiobutton(
                bar,
                text=lbl,
                variable=self.selected_menu,
                value=lbl,
                indicatoron=0,           # draw like a button
                bd=2, relief="ridge",
                bg="white",              # un-selected colour
                selectcolor="#b9f3ff",   # selected colour
                fg="black",
                width=12,
                command=lambda l=lbl: self._show_page(l)
            )
            rb.pack(side="left", padx=5, pady=6)
            self.menu_btns[lbl] = rb

        tk.Frame(self, height=2, bg="black").pack(fill="x")  # separator

    # ──────────────────────── page stack ───────────────────────
    def _build_pages(self):
        stack = tk.Frame(self, bg="white")
        stack.pack(expand=True, fill="both")
        stack.grid_rowconfigure(0, weight=1)
        stack.grid_columnconfigure(0, weight=1)

        self.pages = {
            "ADD NEW"      : self._make_add_new_page(stack),
            "ADD TRAVELER" : self._traveler_form(stack),
            "ADD TRIP"     : self._trip_form(stack),
            "ADD COMPANION": self._companion_form(stack),
            "EDIT"         : self._placeholder(stack, "EDIT"),
            "VIEW"         : self._placeholder(stack, "VIEW"),
            "EXPORT"       : self._placeholder(stack, "EXPORT"),
        }

        for p in self.pages.values():
            p.grid(row=0, column=0, sticky="nsew")

    # ─────────── landing page ───────────
    def _make_add_new_page(self, parent):
        page = tk.Frame(parent, bg="white")
        tk.Label(page, text="Add a new ...",
                 font=("Comic Sans MS", 16, "bold"),
                 bg="white", fg="black").pack(pady=(25, 10))

        btn_box = tk.Frame(page, bg="white")
        btn_box.pack(pady=10)

        big = dict(font=("Comic Sans MS", 20, "bold"),
                   width=12, height=6, bd=3, relief="raised")
        tk.Button(btn_box, text="TRIP",     **big,
                  command=lambda: self._show_page("ADD TRIP")).pack(side="left", padx=30)
        tk.Button(btn_box, text="TRAVELER", **big,
                  command=lambda: self._show_page("ADD TRAVELER")).pack(side="left", padx=30)
        tk.Button(btn_box, text="COMPANION", **big,
                  command=lambda: self._show_page("ADD COMPANION")).pack(side="left", padx=30)
        return page

    # ───────── generic form (traveler / trip) ─────────
    def _generic_form(self, parent, title):
        frame = tk.Frame(parent, bg="white")
        tk.Label(frame, text=title,
                 font=("Comic Sans MS", 16, "bold"),
                 fg="#d02bff", bg="white").pack(pady=(25, 15))

        form = tk.Frame(frame, bg="white")
        form.pack()

        def row(r, label):
            tk.Label(form, text=label, bg="white", fg="black", anchor="w"
                     ).grid(row=r, column=0, sticky="w", pady=6)

        # Name
        row(0, "Name")
        tk.Entry(form, width=40).grid(row=1, column=0, pady=(0, 10))

        # Companion
        row(2, "Select Companion")
        cmp_var = tk.StringVar(value=self.companions[0])
        tk.OptionMenu(form, cmp_var,
                      *self.companions).grid(row=3, column=0, sticky="we", pady=(0, 10))

        # Location
        row(4, "Location")
        tk.Entry(form, width=40).grid(row=5, column=0, pady=(0, 10))

        # Trip Date
        row(6, "Trip Date")
        tk.Entry(form, width=40).grid(row=7, column=0, pady=(0, 10))

        return frame


    # traveler form, name, age, birth location
    def _traveler_form(self, parent):
        frame = tk.Frame(parent, bg="white")
        tk.Label(frame, text="ADD A NEW TRAVELER",
                 font=("Comic Sans MS", 16, "bold"),
                 fg="#d02bff", bg="white").pack(pady=(25, 15))

        form = tk.Frame(frame, bg="white")
        form.pack()

        def row(r, label):
            tk.Label(form, text=label, bg="white", fg="black", anchor="w"
                     ).grid(row=r, column=0, sticky="w", pady=6)


        # Name
        row(0, "Name")
        tk.Entry(form, width=40).grid(row=1, column=0, pady=(0, 10))

        # Age
        row(2, "Age")
        tk.Entry(form, width=40).grid(row=3, column=0, pady=(0, 10))

        # Birth Location
        row(4, "Birth Location")
        tk.Entry(form, width=40).grid(row=5, column=0, pady=(0, 10))

        return frame



    # trip form, location, date, image_file
    def _trip_form(self, parent):
        frame = tk.Frame(parent, bg="white")
        tk.Label(frame, text="ADD A NEW TRIP",
                 font=("Comic Sans MS", 16, "bold"),
                 fg="#d02bff", bg="white").pack(pady=(25, 15))

        form = tk.Frame(frame, bg="white")
        form.pack()

        def row(r, label):
            tk.Label(form, text=label, bg="white", fg="black", anchor="w"
                     ).grid(row=r, column=0, sticky="w", pady=6)


        # Traveler Dropdown
        row(0, "Select Traveler")
        traveler_var = tk.StringVar(value=self.travelers[0])
        tk.OptionMenu(form, traveler_var,
                      *self.travelers).grid(row=1, column=0, sticky="we", pady=(0, 10))

        # Trip Date
        row(2, "Trip Date")
        tk.Entry(form, width=40).grid(row=3, column=0, pady=(0, 10))

        # Location
        row(4, "Location")
        tk.Entry(form, width=40).grid(row=5, column=0, pady=(0, 10))

        # Image File
        row(6, "Image File")
        tk.Entry(form, width=40).grid(row=7, column=0, pady=(0, 10))

        return frame
    def _companion_form(self,parent):
        frame = tk.Frame(parent, bg="white")
        tk.Label(frame, text="ADD A NEW COMPANION",
                 font=("Comic Sans MS", 16, "bold"),
                 fg="#d02bff", bg="white").pack(pady=(25, 15))

        form = tk.Frame(frame, bg="white")
        form.pack()

        def row(r, label):
            tk.Label(form, text=label, bg="white", fg="black", anchor="w"
                     ).grid(row=r, column=0, sticky="w", pady=6)


        # Traveler Dropdown
        row(0, "Select Traveler")
        traveler_var = tk.StringVar(value=self.travelers[0])
        tk.OptionMenu(form, traveler_var,
                      *self.travelers).grid(row=1, column=0, sticky="we", pady=(0, 10))


        # Name
        row(2, "Name")
        tk.Entry(form, width=40).grid(row=3, column=0, pady=(0, 10))

        # Age
        row(4, "Age")
        tk.Entry(form, width=40).grid(row=5, column=0, pady=(0, 10))

        # Original Location
        row(6, "Original Location")
        tk.Entry(form, width=40).grid(row=7, column=0, pady=(0, 10))
        return frame

    # ───────── simple placeholder pages ─────────
    @staticmethod
    def _placeholder(parent, label):
        f = tk.Frame(parent, bg="white")
        tk.Label(f, text=f"{label} PAGE",
                 font=("Comic Sans MS", 20, "bold"),
                 bg="white", fg="black").pack(expand=True)
        return f

    # ───────── page switcher ─────────
    def _show_page(self, key):
        self.pages[key].tkraise()


if __name__ == "__main__":
    TravelersApp().mainloop()



# companionsString = "Bob, Alice, Charlie, Dave, Eve, Frank, Grace, Heidi, Ivan, Judy"
#         companionsList = companionsString.split(", ");