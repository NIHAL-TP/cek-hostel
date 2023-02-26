from tkinter import *
from PIL import *
print("Welcome to project")
def verify_login():
    if((e_username.get()=="user") and (e_password.get()=="pword")):
        root.destroy()
        logged=Tk()
        label=Label(logged,text="logged in successfully",bg="black",fg="green")
        label.pack()
        logged.mainloop()
    else:
        root.destroy()
        error=Tk()
        label=Label(error,text="error")
        label.pack()
        error.mainloop()



root=Tk()
root.geometry("400x300+50+50")
root.title("admin login")

label1=Label(root,text="ADMIN LOGIN PAGE")
label1.pack()

frame_login=LabelFrame(root)
frame_login.pack(padx=10,pady=10)

label_username=Label(frame_login,text="username:")
label_username.place(x=50,y=50)

label_password=Label(frame_login,text="password:")
label_password.place(x=50,y=100)

e_username=Entry(frame_login)
e_username.place(x=150,y=50)


e_password=Entry(frame_login)
e_password.place(x=150,y=100)

exit_button=Button(frame_login,text="Exit",command=root.quit)
exit_button.place(x=100,y=150)

b_login=Button(frame_login,text="login",bg="black",fg="white",command=verify_login)
b_login.place(x=150,y=150)

root.mainloop()