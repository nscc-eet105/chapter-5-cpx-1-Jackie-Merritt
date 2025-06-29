from adafruit_circuitplayground import cp
import time

#Highest value: 321
#Lowest value: 0
#35.67 repeating
#0 = 0
#1-35 = A1 36-70 = A2 71-105 = A3 106-140 = A4
#141-175 = A5 176-210 = A6 211-245 = A7 246-280 = A8
#281-321 = A9

def scale(value):
    index = int(321 * 9)
    return index

def black():
    for num in range(0, 9):
        cp.pixels[num] = (0, 0, 0)


while True:
    light = cp.light
    print((light,))
    time.sleep(.05)
