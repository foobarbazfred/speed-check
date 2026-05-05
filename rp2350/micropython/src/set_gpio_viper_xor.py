import machine
from machine import Pin

#SIO_BASE_REG = 0xd0000000
#SIO_GPIO_OUT_XOR_REG_OFFSET = 0x28 
#SIO_GPIO_OUT_XOR_REG = SIO_BASE_REG + SIO_GPIO_OUT_XOR_REG_OFFSET

@micropython.viper
def _gp1_xor():
    while True:
        # 0xd0000028 : SIO_GPIO_OUT_XOR_REG
        ptr32(0xd0000028)[0] = 0x00_02  # 0x00_02 means gpio:1

print(machine.freq())
pin1 = Pin(1, Pin.OUT)
_gp1_xor()








