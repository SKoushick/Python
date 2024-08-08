import datetime
##from playsound import playsound
alarmHour = int(input("Enter Hour:"))
alarmMin = int(input("Enter Minutes:"))
alarmAm = input("Am / Pm")

if alarmAm=="Pm":
    alarmHour+=12


while True:
    if alarmHour==datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing..")
##        playsound("punky.mp3")
        break
