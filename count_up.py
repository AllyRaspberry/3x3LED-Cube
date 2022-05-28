# Lauflicht

from machine import Pin
from time import sleep

LED=[2,3,4,6,7,8,10,11,12]
LAGE=[18,19,20]

delay = .25

for l in range(3):
    LAGE[l]=Pin(LAGE[l],Pin.OUT)
for n in range(9):
    LED[n]=Pin(LED[n],Pin.OUT)
            
def ddurchzaehlen():        
    for l in range (3):
        LAGE[l].value(0)
        for n in range(9) :
            LED[n].value(1)
            sleep(delay)
            LED[n].value(0)
            sleep(delay)
        LAGE[l].value(1)
        sleep(delay)
        
def durchzaehlen():
    for z in range (1):
        for l in range (3):
            LAGE[l].value(0)
            for n in range(9) :
                LED[n].value(1)
                sleep(delay)
                LED[n].value(0)
                sleep(delay)
            LAGE[l].value(1)
            sleep(delay)

while True:
    durchzaehlen()