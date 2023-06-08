# Panel Controller #

How to turn a giant panel into a huge input-output controller. Including plug detection puzzles, electro-lum wires control, knob, buttons...
## Dependencies

* python > 3.6
* pip3, RPi.GPIO, olad, ola (python wrapper)
* install requirements with pip3 install -r requirements.txt

## Service setup 

```
sudo cp controller.service /etc/systemd/system/
sudo cp elwire_controller.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable controller.service
sudo systemctl enable elwire_controller.service
```
## Flash RPi Pico controller

```
pip3 install adafruit-ampy
ampy --port /dev/ttyACM0 put pico/*.py
ampy --port /dev/ttyACM0 put pico/A
ampy --port /dev/ttyACM1 put pico/*.py
ampy --port /dev/ttyACM1 put pico/B
```
The pico distinguish the role (controller customization) from A and B file. 

