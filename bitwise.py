#!/usr/bin/env python2

verification_array = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
password = []

for number in verification_array:
    number ^= 111
    password.append(chr((number >> 5 | number << 3) & 255))

print "".join(password)
