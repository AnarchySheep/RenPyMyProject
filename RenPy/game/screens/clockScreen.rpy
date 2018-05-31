init python:
    def add(hourAdd = 0, minutesAdd = 0):
        global hours
        global pm
        global minutes

        minutes += minutesAdd
        if minutes >= 60:
            minutes = minutes % 60
            hours+= 1
        hours += hourAdd
        if hours >= 12:
            hours = hours % 12
            pm = not pm
        displayTime()
        calcAngle()
        return hours

    def calcAngle():
        if hours == 0:
            print("0 hour hand angle")
        else:
            hourHandAngle = 360 / (12/float(hours))
            print(str(hourHandAngle) + " hour hand angle")
        if minutes == 0:
            print("0 minute hand angle")
        else:
            minuteHandAngle = 360 / (60/float(minutes))
            print(str(minuteHandAngle) + " minute hand angle")

    def displayTime():
        print ("It is currently %s:%s %s" % (hours, str(minutes).zfill(2), "pm" if pm else "am"))
    minutes = 0
    pm = True
    hours = 0
    add(0)
    add(24, 1)

screen clock:

    text ("%s:%s %s" % (hours, str(minutes).zfill(2), "pm" if pm else "am")) pos (20, 20) style "clockText"
