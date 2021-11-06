from tkinter import *
import datetime
import time
import winsound

# alarm function
def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        currentTime = datetime.datetime.now()
        nowTime = currentTime.strftime("%H:%M:%S")
        date =  currentTime.strftime("%d/%m/%Y")
        print("Alarm set date: ", date)
        print(nowTime)
        if nowTime == setAlarmTimer:
            print("Alarm: ")
            newLabel = Label(clock, text = "Alarm triggered",fg="yellow",bg="black",font=("Arial",12,"bold")).place(x = 110,y=130)
           
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actualTime():
    setAlarmTimer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(setAlarmTimer)

# Tk Clock GUI
clock = Tk()

clock.title("My Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text= "Enter time in 24 hour format!",font="Arial").place(x=60,y=150)
addTime = Label(clock,text = "Hour   Min    Sec",font=60).place(x = 110, y=0)
currentTimeLabel = Label(clock, text = "Current time: ",font=("Arial",12,"bold")).place(x=0, y=30)
currentTime = Label(clock, text = datetime.datetime.now().strftime("%H:%M:%S"),font=("Arial",12,)).place(x=100, y=30)
setYourAlarm = Label(clock,text = "Alarm time: ",font=("Arial",12,"bold")).place(x=0, y=60)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "yellow",width = 15).place(x=110,y=60)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 15).place(x=150,y=60)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 15).place(x=200,y=60)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",width = 10,command = actualTime).place(x =110,y=100)

clock.mainloop()
#Execution of the window.