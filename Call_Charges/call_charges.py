#Kylie Drawdy
#4/15/24
#Write a GUI application that allows the user to select a rate category, and enter the number of minutes
#of the call into an Entry widget. An info dialog box should display the charge for the call.

import tkinter
import tkinter.messagebox

class LongDistanceGUI:
    def __init__(self):
        #Create main window
        self.main_window = tkinter.Tk()

        #Create 2 frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Create variable for radio buttons
        self.radioVariable = tkinter.IntVar()

        #Set default for radio buttons to 1
        self.radioVariable.set(1)

        #Create radio buttons
        self.radiobtn1 = tkinter.Radiobutton(self.top_frame, text = "Daytime", variable = self.radioVariable, value = 1)
        self.radiobtn2 = tkinter.Radiobutton(self.top_frame, text = "Evening", variable = self.radioVariable, value = 2)
        self.radiobtn3 = tkinter.Radiobutton(self.top_frame, text = "Off-Peak", variable = self.radioVariable, value = 3)

        # Pack radio buttons
        self.radiobtn1.pack()
        self.radiobtn2.pack()
        self.radiobtn3.pack()

        #Create items for middle frame
        self.minuteLabel = tkinter.Label(self.middle_frame, text = "Enter minutes: ")
        self.minuteEntry = tkinter.Entry(self.middle_frame, width = 10)

        #Pack items for middle frame
        self.minuteLabel.pack(side = "left")
        self.minuteEntry.pack(side = "left")

        #Create submit button
        self.displayButton = tkinter.Button(self.bottom_frame, text = "Display Charges", command = self.calcCharges)

        #Pack button
        self.displayButton.pack()

        #pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        #Start listening for events
        tkinter.mainloop()

    def calcCharges(self):
        #Get entered value
        self.minuteEntry = float(self.minuteEntry.get())

        #Determine which radio button was checked and set value
        if self.radioVariable.get() == 1:
            self.minuteRate = 0.07
        elif self.radioVariable.get() == 2:
            self.minuteRate = 0.12
        elif self.radioVariable.get() == 3:
            self.minuteRate = 0.05

        #Calculate charges
        self.finalCharge = self.minuteRate * self.minuteEntry

        #Display results and close window
        tkinter.messagebox.showinfo("Total: " + format(self.finalCharge, ',.2f'))
        self.main_window.destroy()

longDistance = LongDistanceGUI()