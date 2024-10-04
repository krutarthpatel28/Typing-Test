import tkinter as tk
from tkinter import messagebox
import time
import random


class TypingSpeedTracker:
    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Tracker")

        self.sentence_label = tk.Label(master, text="Type the following sentence:")
        self.sentence_label.pack()

        self.sentence_display = tk.Label(master, text="")
        self.sentence_display.pack()

        self.answer_label = tk.Label(master, text="Your Answer:")
        self.answer_label.pack()

        self.answer_entry = tk.Entry(master, width=50)
        self.answer_entry.pack()

        self.start_button = tk.Button(master, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack()

        self.typing_speed_label = tk.Label(master, text="")
        self.typing_speed_label.pack()

        self.accuracy_label = tk.Label(master, text="")
        self.accuracy_label.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_typing_test)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)

        self.typing_started = False
        self.start_time = 0
        self.total_chars = 0
        self.correct_chars = 0
        self.sentence_to_type = ""

    def generate_sentence(self):
        words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        sentence = ' '.join(random.sample(words, len(words)))
        return sentence

    def start_typing_test(self):
        self.sentence_to_type = self.generate_sentence()
        self.sentence_display.config(text=self.sentence_to_type)

        self.typing_started = True
        self.total_chars = 0
        self.correct_chars = 0
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.answer_entry.config(state=tk.NORMAL)

    def stop_typing_test(self):
        if self.typing_started:
            end_time = time.time()
            total_time = end_time - self.start_time
            typing_speed = (self.correct_chars / total_time) * 60  # Characters per minute
            accuracy = (self.correct_chars / self.total_chars) * 100
            self.typing_speed_label.config(text=f"Your typing speed: {typing_speed:.2f} characters per minute")
            self.accuracy_label.config(text=f"Your accuracy: {accuracy:.2f}%")
            self.typing_started = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.answer_entry.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Info", "You haven't started typing yet!")

    def on_key_press(self, event):
        if self.typing_started:
            typed_char = event.char
            correct_char = self.sentence_to_type[self.total_chars]

            if typed_char == correct_char:
                self.correct_chars += 1

            self.total_chars += 1

            if self.total_chars == len(self.sentence_to_type):
                self.stop_typing_test()


def main():
    root = tk.Tk()
    typing_speed_tracker = TypingSpeedTracker(root)
    root.bind("<KeyPress>", typing_speed_tracker.on_key_press)
    root.mainloop()


if __name__ == "__main__":
    main()