import tkinter as tk
from tkinter import scrolledtext
def change_text():
    # Update the label’s text
    label.config(text="Button clicked!")

root = tk.Tk()
root.title("Time Traveler App")

# Initial text


label = tk.Label(
    root,
    text="Hello, World!",
    wraplength=250,   # wrap after ~250 pixels
    justify="left"    # (optional) text alignment inside the label
)

root = tk.Tk()
root.title("Scrollable text demo")

# ScrolledText acts like a Text widget with a built-in scrollbar
label_like = scrolledtext.ScrolledText(
    root,
    wrap="word",       # same as wraplength in a Label
    width=40,          # approximate character width
    height=4,          # visible lines before scrolling
    borderwidth=0,     # flat look, like a Label
    highlightthickness=0
)

# insert your message and make it read-only
label_like.insert("end", "Hello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, "
                         "World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, "
                         "World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!"
                         "\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\nHello, World!\n")
label_like.config(state="disabled")   # prevent user edits
label_like.pack(fill="both", expand=True, padx=20, pady=10)

label.pack(padx=20, pady=10)
#
# label = tk.Label(root, text="Hello, World!")
# label.pack(padx=20, pady=10)

# Button that triggers the change_text() callback
button = tk.Button(root, text="Click me", command=change_text)
button.pack(pady=(0, 20))

# Entry widget for user input
entry = tk.Entry(root, justify ="left")
entry.pack(padx=200, pady=(0, 10))
# Function to get the text from the entry widget
def get_entry_text():
    entry_text = entry.get()
    label.config(text=f"You entered: {entry_text}")
# Button to get the entry text
entry_button = tk.Button(root, text="Get Entry Text", command=get_entry_text)
entry_button.pack(pady=(0, 20))




root.mainloop()


