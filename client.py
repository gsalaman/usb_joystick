import usb_gamepad
import time


init_string = usb_gamepad.init(2)
print init_string
if init_string != "success":
  exit(0) 


while True:
  my_string = usb_gamepad.read_nonblocking(0)
  if (my_string != "No Input"):
    print "0: "+my_string
  my_string = usb_gamepad.read_nonblocking(1)
  if (my_string != "No Input"):
    print "1: "+my_string
