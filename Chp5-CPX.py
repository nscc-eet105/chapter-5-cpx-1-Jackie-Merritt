from adafruit_circuitplayground import cp
import time

# Highest value: 321
# Lowest value: 0
# 35.67 repeating
# 0 = 0
# 1-35 = A1 36-70 = A2 71-105 = A3 106-140 = A4
# 141-175 = A5 176-210 = A6 211-245 = A7 246-280 = A8
# 281-321 = A9

# index = Neopixels 0-9
# lightValue is the value of the light detected by the sensor
# MAX is the maximum value shown by the sensor
# Maxindex = 9 or highest neopixel


from adafruit_circuitplayground import cp
import time

maxlight = 321
maxneo = 10

def main():
    while True:
        light = cp.light
        index = scale(light)
        cp.pixels[index] = (0, 50, 0)
        time.sleep(.5)
        black()
        print((index,))
def scale(light):
    return int(light/maxlight * maxneo)

def black():
    for num in range(0, maxneo):
        cp.pixels[num] = (0, 0, 0)

main()


# while True:
    # light = cp.light
    # print((light,))
    # time.sleep(.05)
