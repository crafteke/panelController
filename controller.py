import os
import time
from signal import signal, SIGINT
from sys import exit
import socketio
import serial #pip3 install serial
import os

SIO_SERVER='http://face6core.local:4567'

sio = socketio.Client()
serials=[None]*2

# correct_tags=["0415911acdc826","0415917a9b5728","0415910a76d926","0415910a66c326","0415918a11ac28","0415911a2ce826"]
# GPIO.setmode(GPIO.BCM)
# VALIDATE_BUTTON=4
# START_BUILDING=17
#
# @sio.event
# def connect():
#     print("Connected to server. Registering.")
#     sio.emit('Register','rfidpi')
@sio.event
def connect_error():
    print("The connection failed!")

@sio.event
def disconnect():
    print("Disconnected from server")

def main():
    print("Starting smallworld controller...")
    try:
       sio.connect(SIO_SERVER)
    except:
        print("SocketIO server not available")
    if sio.connected:
        sio.emit('Register',"lockerspi")
        print("Connected with SID ",sio.sid)
    print("Opening available serial ports... ")
    usb_devices_array=os.popen('ls /dev/ttyACM*').read().split('\n')
    usb_devices_array=list(filter(lambda e: len(e)>0, usb_devices_array))
    i=0
    retries=0
    for ser_port in usb_devices_array:
        if(os.path.exists(ser_port)):
            serials[i]=serial.Serial()
            serials[i].baudrate = 115200
            serials[i].port = ser_port
            connected=False
            while not connected and retries<10:
                retries+=1
                try:
                    serials[i].open()
                    print("Port ",ser_port," opened.")
                    connected=True
                    i+=1
                except:
                    print("Error connecting ", ser_port," Retry...")
            retries=0
    while True:
        for i in range(0,2):
            if(serials[i]!= None and serials[i].in_waiting):
                data=serials[i].readline()
                # print("Received from",serials[i].port,':',data)
                data=data.decode("utf-8").strip()
                msg={}
                if(data[0]=='#' and data[2]=='>'):
                    pico_id=data[1]
                serial_msg=data[3:].split(':')
                if(pico_id in ["A","B"]):
                    msg["controller_id"]= 'ac_'+pico_id+'_'+serial_msg[0]
                    msg['value']=serial_msg[1]
                    if sio.connected:
                        sio.emit('Command',msg)
        time.sleep(0.1)

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    sio.disconnect()
    for ser in serials:
        if(ser != None):
            ser.close()
    #GPIO.cleanup()

    exit(0)
# @sio.event
# def Command(data):
#     if(data['controller_id']=='rfid_button_calibrate' and data['value']=='1'):
#         print("Calibration of rfid.")
#         for i in range(0,6):
#             if(serials[i]!= None):
#                 serials[i].write(bytes('2', 'utf-8'))

if __name__ == "__main__":
    signal(SIGINT, handler)
    main()
