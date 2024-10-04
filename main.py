from tkinter import *
from para import paras  # Assuming 'para' is a module you've defined elsewhere
import random
from tkinter import messagebox

timer = None
word = 0
sec = 30


def check_word(event):
    global word
    typed_word = ent.get().strip()  # Strip leading and trailing spaces from the typed word
    sample_word = sample_text.split()[word].strip()  # Strip leading and trailing spaces from the sample word
    if typed_word == sample_word:
        ent.config(bd=1)
        print("Correct word typed:", typed_word)
        ent.delete(0, END)
        word += 1
    else:
        print("Incorrect word typed:", typed_word)
        print("Expected word:", sample_word)
        # Set border color to red
        ent.config(highlightcolor="#e7305b", bd=2)


def start_timer():
    time_lab.config(fg='#e7305b')
    count_down(sec)


def count_down(count):
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        time_lab.config(text=f"time: {count} Seconds")  # Update the time label with the countdown value
    else:
        time_lab.config(text="Time's up!", fg="red")
        messagebox.showinfo(title="Test Finish", message=f"Your words per minutes are :{word*2}")


window = Tk()
sample_text = random.choice(paras)
window.title("Typing Test")
window.config(height=500, width=800, background='#CB9D06', padx=50, pady=50)
sample_lab = Label(text=sample_text, background='#CB9D06', font=('Comic Sans MS', 10))
sample_lab.grid(row=1, column=1, columnspan=3)

time_lab = Label(text=f"time :{sec} Seconds", background="#CB9D06")
time_lab.grid(row=0, column=3)
ent = Entry(highlightcolor="#e7305b")
ent.grid(row=3, column=2)
ent.bind("<KeyRelease-space>", check_word)  # Bind to KeyRelease-space event
ent.focus_set()
start_timer()  # Start the timer countdown

window.mainloop()
