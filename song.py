import sys
from time import sleep
import time
import tkinter as tk


def display_lyrics_gui():
  
    window = tk.Tk()
    window.title("Lirik Lagu")

   
    window.geometry("500x300")
    window.resizable(False, False)

    label = tk.Label(window, text="", font=("Helvetica", 14), anchor="center", justify="center", wraplength=400)
    label.pack(expand=True)

  
    def start_lyrics():
    
        start_button.config(state="disabled")

        lines = [
            ("It's been 3 years and six whole months", 0.08),
            ("Since i saw your face that night", 0.10),
            ("It took five seconds to fall in love", 0.08),
            ("And two more to make you mine", 0.08),
            ("Now it's four in the morning, sun's set and", 0.07),
            ("Seven minutes with you and it's haven", 0.08),
            ("Ain't an hour that rolls by", 0.09),
            ("I love you 24/7/365", 0.09),
            ("Give you my name, if you wanted to", 0.10),
            ("Key to my heart, if you want it too", 0.10),
            ("And i hope and pray that you'll stay right here", 0.09),
            ("Till we're old and gray in our last few years", 0.08),
            ("Im on a knee, i just need a Yes", 0.09),
            ("A couple kids and a picked fance", 0.07),
            ("Share the memories like an open book", 0.09),
            ("Every page i read it still got me hooked", 0.10),
            ("And im fine", 0.07),
            ("Spending my whole live", 0.07),
            ("On everything you like", 0.07),
            ("Is it obvious that all of this is right?", 0.08),
            ("Cause it's been", 0.07),
            ("Three years and six whole months", 0.08),
            ("Since i saw your face that night", 0.08),
            ("It took five seconds to fall in love", 0.09),
            ("And two more to make you mine", 0.10),
            ("Now it's four in the morning, sun's set and", 0.10),
            ("Seven minutes with you and it's heaven", 0.09),
            ("Ain't hour that rolls by", 0.08),
            ("I love you 24/7/365", 0.09),
            ("I'll share the last bite of every meal", 0.07),
            ("I'll wipe your tears when you're in your feels", 0.09),
            ("And i'll hold you close through a thunderstrom", 0.10),
            ("When it's cold at night, know i'll keep you warm", 0.09),
            ("And im fine", 0.07),
            ("Spending my whole life", 0.07),
            ("On everything you like", 0.07),
            ("Is it obvious that all of this is right?", 0.08),
            ("Cause it's been", 0.07),
            ("Three years and six whole months", 0.08),
            ("since i saw your face that night", 0.08),
            ("It took five seconds to fall in love", 0.09),
            ("and two more to make you mine", 0.08),
            ("Now it's four in the morning sun's set and", 0.09),
            ("Seven minutes with you and it's heaven", 0.10),
            ("Ain't hour that rolls by", 0.09),
            ("I love you 24/7/365", 0.10),
           
        ]

        delays = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 7]

        def show_lyrics(line, char_delay, line_delay, idx):
            if idx >= len(lines):
                return
            text, char_delay = lines[idx]

            current_text = ""
            for char in text:
                current_text += char
                label.config(text=current_text)
                window.update()
                sleep(char_delay)

            sleep(line_delay)

            window.after(0, lambda: show_lyrics(*lines[idx + 1], delays[idx + 1], idx + 1))

        show_lyrics(*lines[0], delays[0], 0)

    start_button = tk.Button(window, text="Press", font=("Helvetica", 14), command=start_lyrics)
    start_button.pack(pady=10)

    window.mainloop()


display_lyrics_gui()
