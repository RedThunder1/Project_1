import tkinter as tk
from GUI import *

def main():
    window = tk.Tk()
    window.title('Voting App')
    window.geometry('250x300')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()