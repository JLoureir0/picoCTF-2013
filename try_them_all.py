#!/usr/bin/env python2
import md5

hashed_password = "46d6eeda57a201a7673c4df4b0f8ede4"
salt = '6737'

dictionary = open("english_dictionary")

for word in dictionary:
    hashed_word = md5.new(word.strip() + salt).hexdigest()
    if hashed_word == hashed_password:
        print word.strip()
        break
