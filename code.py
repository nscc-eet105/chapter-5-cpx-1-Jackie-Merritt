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
        cp.pixels[index] = (0, 0, 0)
        print((index,))
def scale(light):
    return int(light/maxlight * maxneo)

main()
