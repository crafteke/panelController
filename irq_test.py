from machine import Pin
import time
print("hello")
rotary_pins = [[4,6,4]] #format [DT,CLK,SW]
clkValues=[0]*len(rotary_pins)
dtValues=[0]*len(rotary_pins)

def dtEvent(channel,id):
    # global clkPreviousValues
    # message={'to': 'laserUnity','msg':{"controller_id":id}}
    if clkValues[id] == dtValues[id]:
    #    message['msg']['value']='+1'
       print("+")
    dtValues[id] = channel.value()
    # sio.emit('Message', message)


def simple():
    print("simple")
    led = Pin(25, Pin.OUT)
    led.toggle()
    time.sleep(1)
    led.toggle()


def clkEvent(channel,id):
    #print("Event on id " , id)
    # message={'to': 'laserUnity','msg':{"controller_id":id}}
    # #print("CLK ", clkState, "DT ", dtState)
    if clkValues[id] == dtValues[id]:
    #     message['msg']['value']='-1'
        print("-")
    clkValues[id] = channel.value()
    # sio.emit('Message', message)


for i in range(0,len(rotary_pins)):
    print("pin:",rotary_pins[i][0])
    p0 = Pin(rotary_pins[i][0],Pin.IN,Pin.PULL_UP)
    p1 = Pin(rotary_pins[i][1],Pin.IN,Pin.PULL_UP)
    #rotary_pins[i]=[p0,p1] bad
    dtValues[i]=p0.value()
    clkValues[i]=p1.value()

    #GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #p0.irq(lambda p,b=i:print("0 p:",p.value(),"i:",i))
    #p1.irq(lambda p,b=i:print("1 p:",p.value(),"i:",i))

    p0.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,handler=lambda a,b=i: dtEvent(a,b))
    p1.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,handler=lambda a,b=i: clkEvent(a,b))
