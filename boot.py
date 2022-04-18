import sys
from rotary_irq_rp2 import RotaryIRQ
import time
from machine import Pin
print("Booting...")

#SV1 : [0,2],[4,6],[1,3],[5,7]
#SV2 : [8,10],[12,14],[8,11],[13,15] (actually unused for now and maybe for ever)
#SV4 : [17,19],[21,/],[18,20],[22,/]
#SV3 : [8,10,12,14,16,9,11,13,15]

rotary_pins = [[0,2],[4,6],[1,3],[5,7],[17,19],[18,20]] #format [DT,CLK,SW] (pour l'instant [DT,CLK])
rotary_controller=[None]*len(rotary_pins)

button_pins=[8,10,12,14,16,9,11,13,15,21,22]
button_controller=[None]*len(button_pins)

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
    button_controller[i] = Pin(button_pins[i],Pin.IN,Pin.PULL_UP)
    #pin.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING),handler=lambda a,b=i: button_handler(a,b))
        
