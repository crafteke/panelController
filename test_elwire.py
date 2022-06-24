import board
import busio
from digitalio import Direction
import time

from adafruit_mcp230xx.mcp23017 import MCP23017 # pip3 install adafruit-circuitpython-mcp230xx

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)
toggle=0
while True:
    for i in range(0,16):
        pin = mcp.get_pin(i)
        pin.direction = Direction.OUTPUT
        pin.value=toggle
        time.sleep(0.1)
    toggle=(toggle+1)% 2
