from dual_gamepad import gamepad0_read_nonblocking, gamepad1_read_nonblocking

while True:
  my_string = gamepad0_read_nonblocking()
  if (my_string != "No Input"):
    print "Player 1: " + my_string

  my_string = gamepad1_read_nonblocking()
  if (my_string != "No Input"):
    print "Player 2: " + my_string
  
