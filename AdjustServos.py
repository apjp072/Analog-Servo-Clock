#!/usr/bin/env python
#Clock
import time
import datetime
import keyboard
from adafruit_servokit import ServoKit
 
hours_servos   = ServoKit (address=0x41, channels=16)
minutes_servos = ServoKit (address=0x40, channels=16)
 
#num_servos
num_servos = 7 #0 - 6
 
# Channels for hours and minutes in the servo controller
# servo controller 1
hours_1 = 0, 1, 2, 3, 4, 5, 6
hours_0 = 7, 8, 9, 10, 11, 12, 13
 
# servo controller 2
minutes_1 = 0, 1, 2, 3, 4, 5, 6
minutes_0 = 7, 8, 9, 10, 11, 12, 13
 
# tuple with hide angles - how the servos will hide
# according to its position
#hide = 180, 180, 0, 180, 0, 180, 180
 
# number_definitons
#show = 
show_1 = [70, 70, 110, 70, 110, 70, 70] #had to make lists instead of touples as touples are immutable
show_2 = [70, 70, 110, 70, 110, 70, 70]
show_3 = [70, 70, 110, 70, 110, 70, 70]
show_4 = [70, 70, 110, 70, 110, 70, 70]

#hide angle arrays
hide_1 = [180, 180, 0, 180, 0, 180, 180]
hide_2 = [180, 180, 0, 180, 0, 180, 180]
hide_3 = [180, 180, 0, 180, 0, 180, 180]
hide_4 = [180, 180, 0, 180, 0, 180, 180]


#originals - in case of reset
"""show_1 = [30, 30, 150, 30, 150, 30, 30]
show_2 = [30, 30, 150, 30, 150, 30, 30]
show_3 = [30, 30, 150, 30, 150, 30, 30]
show_4 = [30, 30, 150, 30, 150, 30, 30]
hide_1 = [140, 140, 40, 140, 40, 140, 140] 
hide_2 = [140, 140, 40, 140, 40, 140, 140]
hide_3 = [140, 140, 40, 140, 40, 140, 140]
hide_4 = [140, 140, 40, 140, 40, 140, 140]"""

"""show_1 = [30, 30, 150, 30, 150, 30, 30] #had to make lists instead of touples as touples are immutable
show_2 = [30, 30, 150, 30, 150, 30, 30]
show_3 = [30, 30, 150, 30, 150, 30, 30]
show_4 = [30, 30, 150, 30, 150, 30, 30]

#hide angle arrays
hide_1 = [140, 140, 40, 140, 40, 140, 140] #changed numbers to give an additional 40 degrees in either direction
hide_2 = [140, 140, 40, 140, 40, 140, 140]
hide_3 = [140, 140, 40, 140, 40, 140, 140]
hide_4 = [140, 140, 40, 140, 40, 140, 140]"""

#digit on/off positions
number_0 = 1, 1, 1, 0, 1, 1, 1
number_1 = 0, 0, 1, 0, 0, 1, 0
number_2 = 1, 0, 1, 1, 1, 0, 1
number_3 = 1, 0, 1, 1, 0, 1, 1
number_4 = 0, 1, 1, 1, 0, 1, 0
number_5 = 1, 1, 0, 1, 0, 1, 1
number_6 = 1, 1, 0, 1, 1, 1, 1
number_7 = 1, 0, 1, 0, 0, 1, 0
number_8 = 1, 1, 1, 1, 1, 1, 1
number_9 = 1, 1, 1, 1, 0, 1, 1
 #hours_servos.servo[servoNum].angle = degree
def show_servos():
    for i in hours_1:
        print(i)
        hours_servos.servo[i].angle = show_1[i]
       #set_default_position(i, hours_servos)
    for i in hours_0:
        print(i)
        hours_servos.servo[i].angle = show_2[i-7]
       #set_default_position(i, hours_servos)
    for i in minutes_1:
        print(i)
        minutes_servos.servo[i].angle = show_3[i]
        #set_default_position(i, minutes_servos)
    for i in minutes_0:
        print(i)
        minutes_servos.servo[i].angle = show_4[i-7]
        #set_default_position(i, minutes_servos)

def hide_servos():
    for i in hours_1:
        print(i)
        hours_servos.servo[i].angle = hide_1[i]
       #set_default_position(i, hours_servos)
    for i in hours_0:
        print(i)
        hours_servos.servo[i].angle = hide_2[i]
       #set_default_position(i, hours_servos)
    for i in minutes_1:
        print(i)
        minutes_servos.servo[i].angle = hide_3[i]
        #set_default_position(i, minutes_servos)
    for i in minutes_0:
        print(i)
        minutes_servos.servo[i].angle = hide_4[i]
        #set_default_position(i, minutes_servos)

# show number
# set number to show and what group of servos
   #show_number(int(hh[0]),hours_1,hours_servos)
def show_number (number, group_servo,kit, digitShow, digitHide):
    if (number == 0):
        for index, servoNum in enumerate(group_servo):
            if number_0[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 1):
        for index, servoNum in enumerate(group_servo):
            if number_1[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 2):
        for index, servoNum in enumerate(group_servo):
            if number_2[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 3):
        for index, servoNum in enumerate(group_servo):
            if number_3[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 4):
        for index, servoNum in enumerate(group_servo):
            if number_4[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 5):
        for index, servoNum in enumerate(group_servo):
            if number_5[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 6):
        for index, servoNum in enumerate(group_servo):
            if number_6[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 7):
        for index, servoNum in enumerate(group_servo):
            if number_7[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 8):
        for index, servoNum in enumerate(group_servo):
            if number_8[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    if (number == 9):
        for index, servoNum in enumerate(group_servo):
            if number_9[index] == 1:
                servoAngle = digitShow[index]
            else:
                servoAngle = digitHide[index]
            kit.servo[servoNum].angle = servoAngle

    time.sleep(0.5)
 
 
while True:
 
   # Get time
   now = datetime.datetime.now()
 
   # save hours
   hh = list(now.strftime('%I'))
 
   # save minutes
   mm = list(str(now.minute))
  
   # check if we have one digit
   if (len(mm) == 1):
       # insert 0 in first position
       mm.insert(0,"0")
 
   if (len(hh) == 1):
       # insert 0 in first position
       hh.insert(0,"0")
 
   print ("h0: %s" % (hh[0]))
   print ("h1: %s" % (hh[1]))
#    print ("m0: %s" % (mm[0]))
#    print ("m1: %s" % (mm[1]))
 
 
   # Show hours
   show_number(int(hh[0]),hours_1,hours_servos, show_1, hide_1)
   show_number(int(hh[1]),hours_0,hours_servos, show_2, hide_2)
   #show_servos(); 
   # show minutes
   show_number(int(mm[0]),minutes_1,minutes_servos, show_3, hide_3)
   show_number(int(mm[1]),minutes_0,minutes_servos, show_4, hide_4)

   #show minutes test
   #for i in range(10):
   #    show_number(i,minutes_1,minutes_servos)
   #    show_number(i,minutes_0,minutes_servos)

   # we dont need a sleep because we already have 1/2 seconds
 


def main(): 
    show_servos()
    while True:
        print("SHOW: Enter digit, servo #, or 0 0 to quit")
        digit, servoNum = map(int, input().split())
        if digit == 0:
            break
        if digit == 1:
            degree = show_1[servoNum%7]
            while True:
                if keyboard.is_pressed('d'):  # if key 'd' is pressed 
                    degree += 1
                    time.sleep(0.1)

                if keyboard.is_pressed('a'):  # if key 'a' is pressed 
                    degree -= 1
                    time.sleep(0.1)

                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    break
                print(degree)
                hours_servos.servo[servoNum].angle = degree
        if digit == 2:
            show_2[servoNum%7] = degree
            hours_servos.servo[servoNum-14].angle = degree
        if digit == 3:
            show_3[servoNum%7] = degree
            minutes_servos.servo[servoNum].angle = degree
        if digit == 4:
            show_4[servoNum%7] = degree
            minutes_servos.servo[servoNum-14].angle = degree

    print("show_1 = " + str(show_1)) #prints each "show" line
    print("show_2 = " + str(show_2))
    print("show_3 = " + str(show_3))
    print("show_4 = " + str(show_4))

    while True:
        print("HIDE: Enter digit, servo #, or 0 0 to quit")
        digit, servoNum, degree = map(int, input().split())
        if digit == 0:
            break
        if digit == 1:
            hide_1[servoNum%7] = degree
            hours_servos.servo[servoNum].angle = degree
        if digit == 2:
            hide_2[servoNum%7] = degree
            hours_servos.servo[servoNum-14].angle = degree
        if digit == 3:
            hide_3[servoNum%7] = degree
            minutes_servos.servo[servoNum].angle = degree
        if digit == 4:
            hide_4[servoNum%7] = degree
            minutes_servos.servo[servoNum-14].angle = degree

    print("hide_1 = " + str(hide_1)) #prints each "hide" line
    print("hide_2 = " + str(hide_2))
    print("hide_3 = " + str(hide_3))
    print("hide_4 = " + str(hide_4))   
        
	        

#main()

