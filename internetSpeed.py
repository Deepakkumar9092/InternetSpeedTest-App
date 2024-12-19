from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + " Mbps"
    up = str(round(sp.upload()/(10**6),3)) + " Mbps"
    
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("500x650")
sp.config(bg="Blue")

lab = Label(sp,text="Test Internet Speed", font=("Time New Roman",35, "bold"),bg="Blue",fg="White")
lab.place(x = 40, y=40,height=50,width=380)

lab = Label(sp,text="Downloading Speed", font=("Time New Roman",35, "bold"))
lab.place(x = 40, y=130, height=50,width=380)

lab_down = Label(sp,text="00", font=("Time New Roman",35, "bold"))
#,bg="Blue",fg="White"
lab_down.place(x = 40, y=200,height=50,width=380)

lab = Label(sp,text="Uploading Speed", font=("Time New Roman",35, "bold"))
lab.place(x = 40, y=290,height=50,width=380)

lab_up = Label(sp,text="00", font=("Time New Roman",35, "bold"))
lab_up.place(x = 40, y=360,height=50,width=380)

button = Button(sp, text="Check Speed",font=("Time New Roman",35,"bold"),relief=RAISED,fg="Blue",command=speedCheck)
button.place(x=70,y=460,height=50,width=330)

sp.mainloop()


