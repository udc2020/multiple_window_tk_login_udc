#======= Multiple Window With Login System  =======#
#======= By Ultrasdzcoder 🔥  =======#

from tkinter import *
import time
from db import all_data
from tkinter import messagebox


class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Main App")
        app_width = 600
        app_height = 600
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width / 2) - (app_width / 2)
        y = (height / 2) - (app_height / 2)

        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        #======= COLORS =======#
        self._primary = "#669BBC"
        self._secondary = "#F3A712"

        self.config(bg=self._primary)

        title_label = Label(self, text="Main App", font=("Courier", 44))
        title_label.place(relx=0.5, rely=0.5, anchor="center")


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("login")

        app_width = 600
        app_height = 600
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        x = (width / 2) - (app_width / 2)
        y = (height / 2) - (app_height / 2)

        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.resizable(False, False)

        #======= COLORS =======#
        self._primary = "#669BBC"
        self._secondary = "#F3A712"

        self.config(bg=self._primary)

        frame = Frame(self, bg=self._primary)

        frame.place(x=120, y=50, width=550, height=500)

        headline = Label(frame, text="Login", fg="white", bg=self._primary, font=(
            "Courier", 55, "bold"), pady=20).place(x=30)

        text_email = self.Labels(frame, "Email", 120)

        self.email = self.Entrys(frame, 185)

        text_pass = self.Labels(frame, "Password", 240)

        self.password = self.Entrys(frame, 300)

        btn_login = Button(frame,
                           text="Login",
                           bg=self._secondary,
                           bd=0,
                           font=("Courier", 18),
                           command=self.login).place(x=30, y=380, width=350, height=50)

    def Entrys(self, pos, y):
        entry_obj = Entry(pos,  font=("Courier", 18, "bold"))
        entry_obj.place(x=30, y=y, width=350, height=45)
        return entry_obj

    def Labels(self, pos, text, y):
        Label(pos, text=text, fg="white", bg=self._primary, font=(
            "Courier", 18), pady=20).place(x=30, y=y)

    def login(self):
        #======= Add my data from db to lists =======#
        email_list = [d['Email'] for d in all_data]
        pass_list = [d['password'] for d in all_data]

        #======= Validation =======#
        isValid = ((self.email.get()).strip() in email_list and (
            self.password.get()).strip() in pass_list)

        isEmpty = (self.email.get() == "" and self.password.get() == "")

        if isValid:
            #======= Destroy Main Loop =======#
            self.destroy()
            time.sleep(0.5)
            main = MainApp()

        elif isEmpty:
            messagebox.showerror("Info", "Empty Email or Password Try Again")

        else:
            messagebox.showerror(
                "Error", "Invalide Email or Password Try Again")


def main():
    app = Login()
    app.mainloop()


if "__main__" == __name__:
    main()
