import machine
from machine import Pin

def speed_test(pin):
    while True:
        pin.high()
        pin.low()
    
print(machine.freq())
pin1 = Pin(1, Pin.OUT)

speed_test(pin1)




