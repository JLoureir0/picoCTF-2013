#!/usr/bin/env python2

def decodeROT(cyphered_phrase, shift):
        decoded_line = ""
        for letter in cyphered_phrase:
            if 65 <= ord(letter) <= 90:
                decoded_line += chr(65 + ((ord(letter)-65+shift) % 26))
            elif 97 <= ord(letter) <= 122:
                decoded_line += chr(97 + ((ord(letter)-97+shift) % 26))
            else:
                decoded_line += letter

        print decoded_line

cyphered_text = open('read_manual.txt')

cyphered_first_line = cyphered_text.readline()

for i in range(1,27):
    print i,
    decodeROT(cyphered_first_line, i)

rotation = int(raw_input("Enter the correct rotation: "));

print "=========== ROT %i ===========" %rotation

for cyphered_line in cyphered_text:
    decodeROT(cyphered_line, rotation)
