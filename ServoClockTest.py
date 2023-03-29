#!/usr/bin/env python
#Clock
import time
import datetime
from adafruit_servokit import ServoKit

hours_servos   = ServoKit (address=0x40, channels=16)
minutes_servos = ServoKit (address=0x41, channels=16)

#num_servos
num_servos = 7 #0 - 6 

# Channels for hours and minutes in the servo controller 
# servo controller 1
hours_1 = 0, 1, 2, 3, 4, 5, 6
hours_0 = 7, 8, 9, 10, 11, 12, 13

# servo controller 2
minutes_1 = 0, 1, 2, 3, 4, 5, 6
minutes_0 = 7, 8, 9, 10, 11, 12, 13

h1_error = [0, 0, 0, 0, 0, 0, 0]
h0_error = [0, 0, 0, 0, 0, 0, 0]
m1_error = [0, 0, 0, 0, 0, 0, 0]
m0_error = [0, 0, 0, 0, 0, 0, 0]

# tuple with hide angles - how the servos will hide
# according to its position
hide = 180, 180, 0, 180, 0, 180, 180

# number_definitons
number_0 = 70, 70, 110, hide[3], 110, 70, 70
number_1 = hide[0], hide[1], 110, hide[3], hide[4], 70, hide[6]
number_2 = 70, hide[1], 110, 70, 110, hide[5], 70
number_3 = 70, hide[1], 110, 70, hide[4], 70, 70
number_4 = hide[0], 70, 110, 70, hide[4], 70, hide[6]
number_5 = 70, 70, hide[2], 70, hide[4], 70, 70
number_6 = 70, 70, hide[2], 70, 110, 70, 70
number_7 = 70, hide[1], 110, hide[3], hide[4], 70, hide[6]
number_8 = 70, 70, 110, 70, 110, 70, 70
number_9 = 70, 70, 110, 70, hide[4], 70, 70

def set_default_position(i,kit):
    # 70 degrees is the default position for all servos
        if i == (2 or 4):
            kit.servo[i].angle = 110
        else:
            kit.servo[i].angle = 70

def reset_servos():
    for i in range(hours_1[0], hours_1[6]+1):
        print(i)
        set_default_position(i, hours_servos)
    for i in range(hours_0[0], hours_0[6]+1):
        print(i)
        set_default_position(i, hours_servos)
    for i in range(minutes_1[0], minutes_1[6]+1):
        print(i)
        set_default_position(i, minutes_servos)
    for i in range(minutes_0[0], minutes_0[6]+1):
        print(i)
        set_default_position(i, minutes_servos)

def hide_all():
    #hides all the foots
    for x in range(num_servos):
        #print(i)
        kit.servo[x].angle = hide[x]

# show number
# set number to show and what group of servos
def show_number (number, group_servo,kit):
    if (number == 0):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_0[x]
            x = x + 1
    if (number == 1):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_1[x]
            x = x + 1
    if (number == 2):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_2[x]
            x = x + 1
    if (number == 3):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_3[x]
            x = x + 1
    if (number == 4):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_4[x]
            x = x + 1
    if (number == 5):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_5[x]
            x = x + 1
    if (number == 6):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_6[x]
            x = x + 1
    if (number == 7):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_7[x]
            x = x + 1
    if (number == 8):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_8[x]
            x = x + 1
    if (number == 9):
        x = 0
        for t in range(group_servo[0], group_servo[6]+1):
            kit.servo[t].angle = number_9[x]
            x = x + 1

    time.sleep(0.5)


while True:

    # Get time
    now = datetime.datetime.now()

    # save hours
    hh = list(str(now.hour))

    # save minutes
    mm = list(str(now.minute))
    
    # check if we have one digit
    if (len(mm) == 1):
        # insert 0 in first position
        mm.insert(0,"0")

    if (len(hh) == 1):
        # insert 0 in first position
        hh.insert(0,"0")

#    print ("h0: %s" % (hh[0]))
#    print ("h1: %s" % (hh[1]))
#    print ("m0: %s" % (mm[0]))
#    print ("m1: %s" % (mm[1]))


    # Show hours
    show_number(int(hh[0]),hours_1,hours_servos)
    show_number(int(hh[1]),hours_0,hours_servos)

    # show minutes
    show_number(int(mm[0]),minutes_1,minutes_servos)
    show_number(int(mm[1]),minutes_0,minutes_servos)

    # we dont need a sleep because we already have 1/2 seconds
