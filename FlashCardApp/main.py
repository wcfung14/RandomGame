import os
import sys
import tkinter as tk
import pandas as pd
import random
from functools import partial

os.chdir(os.path.dirname(sys.argv[0]))

class FlashCard():
    def __init__(self):
        # CONSTANTS
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.CANVAS_WIDTH = 800
        self.CANVAS_HEIGHT = 526

        self.word_lib = pd.read_csv("data/french_words2.csv")
        self.word_lib["Correct?"] = False
        # print(self.word_lib.head)    
        
        self.root = tk.Tk()
        self.curr_row_index = None
        self.make_ui()
        self.update()
        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def update(self):
        # LOGIC
        if len(self.word_lib[self.word_lib["Correct?"] == False]) == 0:
            return("Done!")
        while self.curr_row_index is None or self.word_lib.at[self.curr_row_index, "Correct?"]:
            self.curr_row_index = random.randint(0, self.word_lib.shape[0] -1)

        try: 
            self.root.after_cancel(self.flip_timer)
        except AttributeError:
            pass
        
        self.canvas.itemconfig(self.correct_num, text=f"{len(self.word_lib[self.word_lib["Correct?"] == True])} / {self.word_lib.shape[0]-1}")
        self.canvas.itemconfig(self.q_num, text=str(self.curr_row_index))
        self.canvas.itemconfig(self.lang_text, text="French", fill="Black")        
        self.canvas.itemconfig(self.word_text, text=self.word_lib.at[self.curr_row_index, "French"], fill="Black")
        self.canvas.itemconfig(self.card_bg, image=self.card_front_image)

        self.flip_timer = self.root.after(3000, self.flip)

    def flip(self):
        self.canvas.itemconfig(self.lang_text, text="English", fill="White")
        self.canvas.itemconfig(self.word_text, text=self.word_lib.at[self.curr_row_index, "English"], fill="White")
        self.canvas.itemconfig(self.card_bg, image=self.card_back_image)

    def next_card(self, ans):
        if ans:
            print("a")
            self.word_lib.at[self.curr_row_index, "Correct?"] = True
        else:
            self.curr_row_index = None
        self.update()
    
    def make_ui(self):
        # UI
        self.root.config(padx=50, pady=50, bg=self.BACKGROUND_COLOR)

        # Store images as instance variables to prevent garbage collection
        self.card_back_image = tk.PhotoImage(file="images/card_back.png")
        self.card_front_image = tk.PhotoImage(file="images/card_front.png")
        
        self.right_image = tk.PhotoImage(file="images/right.png")
        self.wrong_image = tk.PhotoImage(file="images/wrong.png")

        # Canvas
        self.canvas = tk.Canvas(self.root, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg=self.BACKGROUND_COLOR, bd=0, highlightthickness=0)
        self.card_bg = self.canvas.create_image(self.CANVAS_WIDTH/2, self.CANVAS_HEIGHT/2, image=self.card_front_image)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Text on canvas
        self.correct_num = self.canvas.create_text(self.CANVAS_WIDTH*0.9, self.CANVAS_HEIGHT*0.1, text="Num", font=("Ariel", 20, "italic"))
        self.q_num = self.canvas.create_text(self.CANVAS_WIDTH*0.1, self.CANVAS_HEIGHT*0.1, text="Num", font=("Ariel", 20, "italic"))
        self.lang_text = self.canvas.create_text(self.CANVAS_WIDTH*0.5, self.CANVAS_HEIGHT*0.2, text="Language", font=("Ariel", 30, "italic"))
        self.word_text = self.canvas.create_text(self.CANVAS_WIDTH*0.5, self.CANVAS_HEIGHT*0.5, text="word", font=("Ariel", 60, "bold"))

        # Buttons
        self.right_button = tk.Button(image=self.right_image, highlightthickness=0, command=partial(self.next_card, True))
        self.right_button.grid(row=1, column=1)

        self.wrong_button = tk.Button(image=self.wrong_image, highlightthickness=0, command=partial(self.next_card, False))
        self.wrong_button.grid(row=1, column=0)

    def on_closing(self):
        self.root.after_cancel(self.update)
        self.root.after_cancel(self.flip)
        self.root.after_cancel(self.flip_timer)
        self.root.destroy()

if __name__ == "__main__":
    flash_card = FlashCard()
