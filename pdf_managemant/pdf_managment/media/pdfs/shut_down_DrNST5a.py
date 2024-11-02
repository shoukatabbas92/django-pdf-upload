from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')

def restart_time():
    os.system("shutdown /r /t 20")
    
def log_off():
    os.system('shutdown -l')

def shutdown():
    os.system('shut_down /s /t 1')

shut_down = Tk()
shut_down.title("ShutDown App")
shut_down.geometry("500x500")
shut_down.config(bg="blue")
r_buttion =Button(shut_down,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)
r_buttion.place(x=150,y=60,height=50, width=180)

r_buttion =Button(shut_down,text="Restart Time",font=("Time New  Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
r_buttion.place(x=150,y=170,height=50,width=180)

lg_buttion =Button(shut_down,text="Log-Off",font=("Time New  Roman",20,"bold"),relief=RAISED,cursor="plus",command=log_off)
lg_buttion.place(x=150,y=270,height=50,width=180)

shut_down_buttion =Button(shut_down,text="ShutDown",font=("Time New  Roman",20,"bold"),relief=RAISED,cursor="plus",command=shut_down)
shut_down_buttion.place(x=150,y=370,height=50,width=180)




shut_down = mainloop()