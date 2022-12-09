from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Bejelentkezés')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signIn():
    username = user.get()
    password = code.get()
    
    if username == 'Admin' and password == 'kisdiofa':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg = "white")
        
        Label(screen, text = "Admin felület!", bg ='#fff', font = ('Calibri(body)', 50)).pack(expand = True)
        
        screen.mainloop()
    
    elif username!= 'admin' and password!= 'kisdiofa':
        messagebox.showerror("Hiba", "Érvénytelen felhasználónév vagy jelszó!")
        
    elif password!= "kisdiofa":
        messagebox.showerror("Hiba", "Érvénytelen jelszó!")
        
    elif username!= 'admin':
        messagebox.showerror("Hiba", "Érvénytelen felhasználónév!")

img=PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=100, y=100)

frame=Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading=Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Arial', 23, 'bold'))
heading.place(x=100, y=5)

# about=Label(frame, text = 'asfasdfa', fg = '#57a1f8', bg = 'white', font = ('Arial', 12))
# about.place(x = 0, y = 0)

###############################

def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name = user.get
    if name == '':
        user.insert(0, 'Felhasználónév')
        

user = Entry(frame, width = 25, fg = 'black', border = 0 , bg = 'white', font = ('Arial, 11'))
user.place(x = 30, y = 80)
user.insert(0, 'Felhasználónév')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 107)

################################

def on_enter(e):
    code.delete(0, 'end')
    
def on_leave(e):
    name = code.get
    if name == '':
        code.insert(0, 'Jelszó')

code = Entry(frame, width = 25, fg = 'black', border = 0 , bg = 'white', font = ('Arial, 11'))
code.place(x = 30, y = 150)
code.insert(0, 'Jelszó')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 25, y = 177)

################################

Button(frame, width = 39, pady = 7, text = 'Sign in', bg = '#57a1f8', fg = 'white', border = 0,  command = signIn).place(x = 35, y = 204)
label = Label(frame, text = "Nincs még fiókja?", fg = 'black', bg = 'white', font = ('Arial', 9))
label.place(x = 75, y = 270)

sign_up = Button(frame, width = 9, text = 'Regisztráció', border = 0, bg = 'white', cursor = 'hand2', fg = '#57a1f8',)
sign_up.place(x = 215, y = 270)

root.mainloop()


#https://www.youtube.com/watch?v=8g3OJD3FfEQ