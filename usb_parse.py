from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event0')

def gamepad_read_blocking(gamepad):
  # These are the key definitions for the generic USB joystick
  d_up = 544
  d_down = 545
  d_left = 546
  d_right = 547
  x = 288
  y = 291
  a = 289
  b = 290
  select = 296
  start = 297
  right_bumper = 293
  left_bumper = 292 

  # This isn't perfect...since we're returning the first value we see, if there are
  #   "chorded" presses, we can miss events.
  for event in gamepad.read_loop():
    # parse keypress events
    if event.type ==ecodes.EV_KEY:

      # 1 indicates key press.  0 indicates release
      if event.value == 1:
        if event.code == x:
          return("X")
        elif event.code == y:
          return("Y")
        elif event.code == a:
          return("A") 
        elif event.code == b: 
          return("B")
        elif event.code == select:
          return("Select")
        elif event.code == start:
          return("Start")
        elif event.code == right_bumper:
          return("Right-bumper")
        elif event.code == left_bumper:
          return("Left-bumper")

    # type 3 are absolute axis events.  The D-pad uses these.
    if event.type == 3:
      # code 0 are x axis events
      if (event.code == 0):
        if event.value == 0:
          return("D-left")
        if event.value == 255:
          return("D-right")
        # ignoring the "return to center" value of 127.

      # code 1 are y axis events
      if (event.code == 1):
        if event.value == 0:
          return("D-up")
        if event.value == 255:
          return("D-down")
  

print(gamepad)
while True:
  print gamepad_read_blocking(gamepad)
