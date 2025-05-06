#!/usr/bin/env python3
"""
Font Families Browser

Click on any font name to copy a Tkinter font specification
to the clipboard, e.g. font=('Arial', 12).
"""

import tkinter as tk
from tkinter import font as tkfont

def populate(frame, fonts, root):
    """Populate the frame with font family labels."""
    for i, item in enumerate(fonts):
        lbl = tk.Label(frame, text=item, font=(item, 16))
        lbl.grid(row=i, sticky="w", padx=5, pady=2)
        lbl.bind("<Button-1>", lambda e, item=item: copy_to_clipboard(item, root))

def copy_to_clipboard(item, root):
    """Copy the selected font specification to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(f"font=('{item.lstrip('@')}', 12)")

def on_frame_configure(canvas):
    """Reset the scroll region to encompass the inner frame."""
    canvas.configure(scrollregion=canvas.bbox("all"))

def main():
    root = tk.Tk()
    root.title('Font Families')

    # Get and sort available font families
    fonts = sorted(tkfont.families())

    # Create canvas with vertical scrollbar
    canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
    frame = tk.Frame(canvas, background="#ffffff")
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    # Bind configuration to update scroll region
    frame.bind("<Configure>", lambda e: on_frame_configure(canvas))

    # Populate the frame with font labels
    populate(frame, fonts, root)

    root.mainloop()

if __name__ == "__main__":
    main()
