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
