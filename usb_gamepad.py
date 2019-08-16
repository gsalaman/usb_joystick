import evdev

# our list of attached, supported gamepads.
gamepads = []

#################################
# init
#   This function initializes our gamepad module.  Pass in the number
#   of gamepads you are expecting to use.  Returns error code if not 
#   successful.
################################# 
def init(expected_gamepads):
  global gamepads
  
  if (expected_gamepads != 1):
    return("unsupported number of gamepads")

  # cleanup necessary?
  del gamepads[:]

  supported_gamepads = [ 
    'Sony PLAYSTATION(R)3 Controller'
  ]

  devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
  for device in devices:
    for supported_gamepad in supported_gamepads:
      if device.name == supported_gamepad:
        gamepads.append(evdev.InputDevice(device.path)) 
        return device.name 

  return "No device found"

#################################
# parse_ps3 
#   parses a single event and returns a string that represents that event.
#################################
def parse_ps3(event):

    # These are the key definitions for the ps3 controller 
    d_up = 544
    d_down = 545
    d_left = 546
    d_right = 547

    # parse keypress events
    if event.type ==evdev.ecodes.EV_KEY:

      # 1 indicates key press.  0 indicates release
      if event.value == 1:
        if event.code == d_up:
          return("D-up")
        elif event.code == d_down:
          return("D-down")
        elif event.code == d_left:
          return("D-left") 
        elif event.code == d_right: 
          return("D-right")

#################################
# parse_generic_usb 
#   parses a single event and returns a string that represents that event.
#################################
def parse_generic_usb(event):

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
  
################################################
# gamepad_read_blocking
#   This returns a single event from the gamepad...blocking until we get one.
################################################
def gamepad_read_blocking():
  global gamepad

  # This isn't perfect...since we're returning the first value we see, if there are
  #   "chorded" presses, we can miss events.
  for event in gamepad.read_loop():
    event_string = gamepad_parse(event)
    if (event_string != None):
      return gamepad_parse(event)

################################################
# read_nonblocking
#   This returns a single event from the specified gamepad
################################################
def read_nonblocking(index):
  global gamepads

  # This isn't perfect...since we're returning the first value we see, if there are
  #   "chorded" presses, we can miss events.
  event = gamepads[index].read_one()
  if event == None:
    return "No Input"
  else:
    # 1st cut:  just assume it's ps3 to test my parsing.  We'll add the 
    # controller switch later.
    event_string = parse_ps3(event)
    if (event_string != None):
      return(event_string)
    else:
      return "No Input"
