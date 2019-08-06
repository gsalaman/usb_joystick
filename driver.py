from usb_gamepad import gamepad_read_blocking,gamepad_read_nonblocking 

while True:
  my_string = gamepad_read_nonblocking()
  if (my_string != "No Input"):
    print my_string
