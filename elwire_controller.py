import time
#rom timeloop import Timeloop #pip3 install timeloop
from datetime import timedelta
from signal import signal, SIGINT
from sys import exit
from ola.ClientWrapper import ClientWrapper
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017 # pip3 install adafruit-circuitpython-mcp230xx

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)

control_pins=[None]*16
dmx_values=[0]*16

REFRESH_DELAY=int(1000/30)

def NewData(data):
    for x in range(0,min(len(data),len(dmx_values))):
        dmx_values[x]=data[x]

def updateElWires():
    for i in range(0,16):
        if(dmx_values[i]==0):
            control_pins[i].value=0
        else:
            control_pins[i].value=1
    wrapper.AddEvent(REFRESH_DELAY, updateElWires)

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    wrapper.Stop()
    #tl.stop()
    exit(0)

if __name__ == "__main__":
    signal(SIGINT, handler)
    print("Starting ELWIRE ANIMATOOOOORRRRRRRR.")
    for i in range(0,16):
        control_pins[i] = mcp.get_pin(i)
        control_pins[i].direction = Direction.OUTPUT
    wrapper = ClientWrapper()
    client = wrapper.Client()
    client.RegisterUniverse(1, client.REGISTER, NewData)
    wrapper.AddEvent(REFRESH_DELAY, updateElWires)
    wrapper.Run()
