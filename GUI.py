from fileinput import close
from tkinter import *
from tkinter.font import Font
import csv


class GUI:
    def __init__(self, window):
        self.window = window

        #Header frame
        self.frame_one = Frame(self.window)
        self.header = Label(self.frame_one, text="Voting App", font=Font(size=25))
        self.header.pack()
        self.frame_one.pack()

        #ID input frame
        self.frame_two = Frame(self.window)
        self.id_label = Label(self.frame_two, text="ID", font=Font(size=12))
        self.id_input = Entry(self.frame_two)
        self.id_label.pack(side="left")
        self.id_input.pack()
        self.frame_two.pack(pady=15)

        #Candidate selection frame
        self.frame_three = Frame(self.window)
        self.candidates_label = Label(self.frame_three, text="Candidates", font=Font(size=20))
        self.candidates_radio = IntVar()
        self.candidate_jane = Radiobutton(self.frame_three, text="Jane", value=1, variable=self.candidates_radio, font=Font(size=12))
        self.candidate_john = Radiobutton(self.frame_three, text="John", value=2, variable=self.candidates_radio, font=Font(size=12))
        self.candidates_label.pack()
        self.candidate_jane.pack()
        self.candidate_john.pack()
        self.frame_three.pack()

        #Submit frame
        self.frame_four = Frame(self.window)
        self.submit_button = Button(self.frame_four, text="Submit", command=self.submit, width=20, bg="#cecece")
        self.alert_label = Label(self.frame_four, text="Please fill out all entries!", font=Font(size=12))
        self.submit_button.pack(pady=10)
        self.alert_label.pack()
        self.frame_four.pack(pady=15)

    def submit(self):
        entered_id = self.id_input.get()
        vote = self.candidates_radio.get()

        #Check if there was no entered value for id or candidate
        if entered_id == '' or vote == 0:
            self.alert_label["text"] = "Please fill out all entries!"
            self.alert_label["fg"] = "red"
            return

        vote = 'Jane' if vote == 1 else 'John'

        with open('votes.csv', 'a+' , newline='') as file:
            file.seek(0)
            lines = [line for line in csv.reader(file)]
            writer = csv.writer(file)

            #Check if id is in file, return if true
            if len(lines) < 1:
                writer.writerow(['ID', 'Vote'])
            else:
                for line in lines:
                    if entered_id in line:
                        self.alert_label['text'] = "Already voted"
                        self.alert_label['fg'] = 'red'
                        return

            #Write vote and id to file, update alert text
            writer.writerow([entered_id, vote])
            self.alert_label['text'] = "Vote Submitted!"
            self.alert_label['fg'] = 'black'
            self.id_input.delete(0, END)
            self.candidates_radio.set(0)