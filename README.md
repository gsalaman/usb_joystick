# usb_joystick
Generic USB joystick parser, built off of evdev
** TIP OF MASTER IN DEVELOPMENT!!! **

You can use usb_gamepad.py to parse events in your pi games.  
First call usb_gamepad.init(NUMBER) to initialize that number of gamepads.
Currently only one is supported.
Then you can call usb_gamepad.read_blocking(INDEX) or usb_gamepad.read_nonblocking(INDEX) to read a specified gamepad.  First connected is index 0, then 1, then....

client.py uses that file to demonstrate non-blocking reads.

generic_read.py gives the raw events. Good for debugging.

usb_parse.py parses out the events into a text string.

Event mapping for generic USB joystick:
- A button: EV_KEY 289
- B button: EV_KEY 290
- X button: EV_KEY 288
- Y button: EV_KEY 291

- D-pad up: code 1, type 03, val 0
- D-pad down: code 1, type 03, val 255
- D-pad left:code 0, type 03, val 0
- D-pad right: code 0, type 03, val 255
- D-pad centered (released) code 0 or 1, type 03 val 127

- Select: EV_KEY 296
- Start:  EV_KEY 297

- Right bumper: EV_KEY 293
- Left bumper:  EV_KEY 292
