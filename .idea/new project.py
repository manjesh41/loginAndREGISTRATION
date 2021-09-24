from tkinter import *
from PIL import ImageTk,Image
import os


# Designing window for registration


def register():
    global register_screen
    register_screen = Toplevel(mainRoot)
    register_screen.title("Register")
    register_screen.geometry("600x550")
    register_screen.config(bg='sky blue')


    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please Register For Your school ID",bg='black',fg='white',font=("Times", "20", "bold italic")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen,bg='yellow', text="Username * ",font=('STYLE_BRACEBAD, 20'))
    username_lable.pack()
    username_entry = Entry(register_screen ,bg='white',fg='black', textvariable=username,font=("Times", "25", "bold italic"))
    username_entry.pack()
    password_lable = Label(register_screen,bg='yellow', text="Password * ",font=('STYLE_BRACEBAD, 20'))
    password_lable.pack()
    password_entry = Entry(register_screen,bg='white',fg='black',textvariable=password, show='*',font=("Times", "25", "bold italic"))

    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=2, fg='white',bg="red",font=('STYLE_BRACEBAD, 13'), command=registerNewUser).pack()


#different windows for loging

def signup():
    global signupScreen
    signupScreen = Toplevel(mainRoot)
    signupScreen.title("sign-up")
    signupScreen.geometry("400x350")
    Label(signupScreen, text="Please Enter School ID",bg='green',font=("Times", "20", "bold italic")).pack()
    Label(signupScreen, text="").pack()
    signupScreen.config(bg="wheat")

    global usernameVerify
    global passwordVerify

    usernameVerify = StringVar()
    passwordVerify = StringVar()

    global usernameSignupEntry
    global passwordSignupENtry

    Label(signupScreen, text="Username * ",font=('STYLE_BRACEBAD, 20')).pack()
    usernameSignupEntry = Entry(signupScreen,bg='yellow' ,font=('STYLE_BRACEBAD, 20'), textvariable=usernameVerify)
    usernameSignupEntry.pack()
    Label(signupScreen, text="",font=('STYLE_BRACEBAD, 20')).pack()
    Label(signupScreen, text="Password * ",font=('STYLE_BRACEBAD, 20')).pack()
    passwordSignupENtry = Entry(signupScreen,bg='yellow' ,font=('STYLE_BRACEBAD, 20'),textvariable=passwordVerify, show='*')
    passwordSignupENtry.pack()
    Label(signupScreen, text="",font=('STYLE_BRACEBAD, 20')).pack()
    Button(signupScreen, text="Login",bg='red'  ,width=10, height=1, font=('STYLE_BRACEBAD,20'),command=signupVerify).pack()


# Implementing event on register button

def registerNewUser():
    usernameInformatio = username.get()
    passwordInformaion = password.get()

    file = open(usernameInformatio, "w")
    file.write(usernameInformatio + "\n")
    file.write(passwordInformaion)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def signupVerify():
    username1 = usernameVerify.get()
    password1 = passwordVerify.get()
    usernameSignupEntry.delete(0, END)
    passwordSignupENtry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            signupSucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def signupSucess():
    global signupSuccessScreen
    signupSuccessScreen = Toplevel(signupScreen)
    signupSuccessScreen.title("Success")
    signupSuccessScreen.geometry("500x500")
    Label(signupSuccessScreen, text="Login Success").pack()
    Button(signupSuccessScreen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(signupScreen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("800x800")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="exit", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(signuScreen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    SignuoSuccessScreen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# showing the first screen
def mainRootScreen():
    global mainRoot
    mainRoot = Tk()
    mainRoot.geometry("700x400")

    mainRoot.title("ABC SCHOOL")
    mainRoot.config(bg="yellow")
    bg=PhotoImage(file="C:/Users/ACER/Downloads/school.png")
    mylabel=Label(mainRoot,image=bg)
    mylabel.place(x=0,y=0)
    Label(text="ABC SCHOOL",bg="red",fg='white', width="300", height="2",font=("Times", "40", "bold italic") ).pack()
    Label(text="").pack()
    Button(text="Sign UP", fg='blue',bg='yellow', height="2", width="30",font=('STYLE_BRACEBAD, 15'), command=signup).pack()
    Label(text="").pack()
    Button(text="Register",fg='blue', bg='yellow',height="2", width="30",font=('STYLE_BRACEBAD, 15'), command=register).pack()

    mainRoot.mainloop()


mainRootScreen()