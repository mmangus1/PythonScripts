# Matthew Mangus
# Jan. 1, 2025
# Portfolio Project
# Number Guessing Game

import random
import tkinter as tk
from tkinter import Label, Entry, Button


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        Create graphical interface
        :param parent:
        :param args:
        :param kwargs:
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label = Label(self)
        self.label2 = Label(self)
        self.entry = Entry(self)
        self.button = Button(self, text="Submit",
                             command=self.genandcomp
                             )

        self.label.config(text="Guess a number")
        self.entry.config()
        self.button.config()
        self.label2.config(text="Guess from 1 to 10")

        self.label.pack(side="top", fill="both")
        self.entry.pack(side="top", fill="both")
        self.button.pack(side="top", fill="both")
        self.label2.pack(side="top", fill="both")

    def genandcomp(self):
        """
        Generate and compare guesses, when button is hit
        :return:
        """
        randomint = random.randint(1, 10)
        try:
            if int(self.entry.get()) > 10:
                raise ValueError()
            guess = self.entry.get()
            if randomint == guess:
                self.label2.config(text="Guess is correct!")
            else:
                self.label2.config(
                    text=f"Guess again. The number was {randomint}.")
            self.entry.delete(0, tk.END)
        except (ValueError, TypeError):
            self.label2.config(text="Not an integer from 1 to 10.")


def main():
    """
    Main function to orchestrate program flow
    :return:
    """
    root = tk.Tk()
    root.title("Number Guessing Game")
    root.geometry("1024x768")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
