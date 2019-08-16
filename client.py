import usb_gamepad

print(usb_gamepad.init(1))

while True:
  my_string = usb_gamepad.read_nonblocking(0)
  if (my_string != "No Input"):
    print my_string
