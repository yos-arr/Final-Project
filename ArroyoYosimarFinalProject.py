"""
Title: Pocket Parking App
Author: Yosi Arroyo

Application allows user to select from 3 options in home screen:
Option 1: User clicks "New Pass" to open new window and collect a new pass code.
Option 2: User clicks "Renew Pass" to open new window and renew existing pass code.
Option 3: User clicks "Cancel Pass" to delete parking pass code.

User can easily return to home page if wrong option was selected. 
User gets visual reference of new coede and confirmation messges.

"""
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random

class PocketParking(tk.Tk):
    """Home window with buttons to select pass options (new, renew or cancel) """
    def __init__(self):
        super().__init__()
        #Sets title and locks resize for 'pocket parking' window.
        self.title("Pocket Parking")
        self.resizable(width=False, height=False)

        #import image from PIL
        self.garageImage = tk.PhotoImage(file="prk.png")

        #Create and place instruction label
        self.direction_label = tk.Label(self, text="Create or renew parking pass",
                              font=("Consolas", 17, "italic"))
        self.direction_label.grid(column=0, row=0)

        #Create and place button for 'new pass' function
        self.button_newParking = tk.Button(self, text="New Pass", padx=10, pady=10, 
                                           command=self.open_newPass)
        self.button_newParking.grid(column=1, row=0)

        #Create and place button for 'renew' pass function
        self.button_renewParking = tk.Button(self, text="Renew Pass", padx=10, pady=10,
                                             command=self.open_renewPass)
        self.button_renewParking.grid(column=1, row=1)

        #Create and place button for 'cancel pass' function
        self.button_cancelParking = tk.Button(self, text="Cancel Pass", padx=10, pady=10,
                                              command=self.open_cancelPass)
        self.button_cancelParking.grid(column=1, row=2)

        #Create image label and fit to window, add alternate text with compund 
        self.img_label = tk.Label(text="WELCOME", image=self.garageImage, 
                                  width=200, height=97, compound="center")
        self.img_label.grid(column=0, row=1)

    def open_newPass(self):
        """Opens window for new pass"""
        #Sets button command for 'new pass' window
        newParking_window = NewPass()
        newParking_window.mainloop()

    def open_renewPass(self):
        """Opens window to renew pass"""
        #Sets button command for 'renew pass' window
        renewParking = RenewPass()
        renewParking.mainloop()

    def open_cancelPass(self):
        """Opens window to cancel pass"""
        #Sets button command for 'cancel pass' window
        cancelParking = CancelPass()
        cancelParking.mainloop()

class NewPass(tk.Toplevel):
    """New pass window, buttons to get new pass and return to home screen"""
    def __init__(self):
        super().__init__()
        #Sets title and locks resize for 'new pass' window
        self.title("New Pass")
        self.resizable(width=False, height=False)

        #Open image file and load to class 
        image = Image.open('prk2.png')
        self.garageImage2 = ImageTk.PhotoImage(image)

        #Create and place label to display instruction
        self.code_Label = tk.Label(self, text="Click button for parking code!",
                                  font=("Consolas", 17, "italic"))
        self.code_Label.grid(column=0, row=0)

        #Create and place button to get new pass code
        self.button_code = tk.Button(self, text="Get pass code.", padx=10, pady=10, 
                                    command=self.generate_Code)
        self.button_code.grid(column=1, row=0)

        #Create and place label to display new pass code
        self.new_code_Label = tk.Label(self, text="", padx=10, pady=10)
        self.new_code_Label.grid(column=1, row=1)

        #Create button to close 'new pass' window
        self.button_close = tk.Button(self, text="Return home", padx=10, pady=10, 
                                     command=self.exit_button)
        self.button_close.grid(column=1, row=2)

        #Create image label and fit to window
        garageImage2 = tk.Label(self, image=self.garageImage2, width=200, height=97)
        garageImage2.grid(column=0, row=1)

    def generate_Code(self):
        """Generates parking code"""
        #Generate random code, uses 'configure method' to assign to display variable.
        random_code = random.randint(10000, 90000)
        self.new_code_Label.config(text=f"Your code is: {random_code}",
                             font=("Consolas", 14, "bold"))

    def exit_button(self):
        """Returns user to home window"""
        self.destroy()

class RenewPass(tk.Toplevel):
    """Renew pass window to renew pass and return to home screen"""
    def __init__(self):
        super().__init__()
        #Sets title and locks resize for 'renew pass' window
        self.title("Renew Pass")
        self.resizable(width=False, height=False)

        #Open image file and load to class 
        image2 = Image.open('prk3.png')
        self.garageImage3 = ImageTk.PhotoImage(image2)

        # Add widgets for Window here
        self.direction_label = tk.Label(self, text="Enter 5 digit code: ",
                              font=("Consolas", 17, "italic"))
        self.direction_label.grid(column=0, row=0)

        #create entry widget for code
        self.pass_code_label = tk.Entry(self, width=10)
        self.pass_code_label.grid(column=1, row=0)

        #Create submit button to get pass == ok
        self.button_renew = tk.Button(self, text="Renew!", padx=10, pady=10,
                                      command=self.validate_code)
        self.button_renew.grid(column=1, row=1)

        #create close button
        self.button_close = tk.Button(self, text="Return home", padx=10, pady=10,
                                     command=self.exit_button)
        self.button_close.grid(column=1, row=2)

        #Create image label and fit to window
        garageImage3 = tk.Label(self, image=self.garageImage3, width=200, height=97)
        garageImage3.grid(column=0, row=1)


    def validate_code(self):
        """Validation method to confirm entry is 5 integers and input required."""
        #Gets input from entry widget 
        user_code = self.pass_code_label.get()

        #Validates entry 5 int/str, returns error or confirmation message.
        try:
            if  len(user_code) == 5 and user_code != " ":
                messagebox.showinfo("Sucess", "Pass renewed!") 
            else:
                messagebox.showerror("Error", "Enter a valid code")
        except ValueError:
                messagebox.showerror("Error", "Please enter a valid 5 digit code.")

    def exit_button(self):
        """Returns user to home window"""
        self.destroy()

class CancelPass(tk.Toplevel):
    """Cancel parking window to cancel pass and return home"""
    def __init__(self):
        super().__init__()
        #Sets title and locks resize for 'cancel pass' window
        self.title("Cancel Pass")
        self.resizable(width=False, height=False)

        #Opens image file and load to class 
        image3 = Image.open('prk4.png')
        self.garageImage4 = ImageTk.PhotoImage(image3)

        #Create and place button to cancel pass
        self.button_x = tk.Button(self, text="Shred pass", padx=10, pady=10,
                                  command=self.generate_message)
        self.button_x.grid(column=1, row=0)

        #Create and place label to display cancellation confirmation
        self.funct_Label = tk.Label(self, padx=10, pady=10,
                              text="")
        self.funct_Label.grid(column=1, row=1)

        #create close button
        self.button_close = tk.Button(self, text="Return home", padx=10, pady=10, 
                                     command=self.exit_button)
        self.button_close.grid(column=1, row=2)

        #Create image label and fit to window
        garageImage4 = tk.Label(self, image=self.garageImage4, width=200, height=97)
        garageImage4.grid(column=0, row=1)

    def generate_message(self):
            """Generates confirmation message after pass cancelled"""
            #Generates confirmation message, uses 'configure' method to assign to display variable.
            self.funct_Label.config(text="Parking pass cancelled.",
                                   font=("Consolas", 14, "bold"))


    def exit_button(self):
        """Returns user to home window"""
        self.destroy()

#iterates tkinter's mainloop by calling parent class PocketParking.
if __name__ == "__main__":
    app = PocketParking()
    app.mainloop()


