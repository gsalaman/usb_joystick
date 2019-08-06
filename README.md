# usb_joystick
Generic USB joystick parser

Python code to parse button events off of the generic USB joystick, using the evdev package.

generic_read.py gives the raw events.

usb_parse.py parses out the events into a text string.

Event mapping:
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
