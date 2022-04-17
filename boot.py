import sys
from rotary_irq_rp2 import RotaryIRQ
import time
from machine import Pin
print("Booting...")

rotary_pins = [[4,6,4]] #format [DT,CLK,SW]
rotary_controller=[None]*len(rotary_pins)

button_pins=[2,3]

def button_handler(a,button_index):
    print("b_"+str(button_index),':',a.value())

for i in range(0,len(rotary_pins)):
    rotary_controller[i]=RotaryIRQ(
        pin_num_dt=rotary_pins[i][0],
        pin_num_clk=rotary_pins[i][1],
        min_val=0,
        max_val=10,
        reverse=False,
        range_mode=RotaryIRQ.RANGE_UNBOUNDED,
        pull_up=False,
        half_step=False)

for i in range(0,len(button_pins)):
    pin = Pin(button_pins[i],Pin.IN,Pin.PULL_UP)
    pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,handler=lambda a,b=i: button_handler(a,b))
