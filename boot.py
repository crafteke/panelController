import sys
from rotary_irq_rp2 import RotaryIRQ
import time

print("Booting...")

rotary_pins = [[4,6,4]] #format [DT,CLK,SW]
rotary_controller=[None]*len(rotary_pins)

button_pins=[]

for i in range(0,len(rotary_pins)):
    rotary_controller[i]=RotaryIRQ(
        pin_num_clk=4,
        pin_num_dt=6,
        min_val=0,
        max_val=10,
        reverse=False,
        range_mode=RotaryIRQ.RANGE_UNBOUNDED,
        pull_up=False,
        half_step=False)

irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,handler=lambda a,b=i: dtEvent(a,b))
