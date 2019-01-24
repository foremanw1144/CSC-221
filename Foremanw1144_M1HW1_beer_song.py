# CSC-221-0001
# M1HW1_Foreman
# beer_song.py
# Goal: Gold


# Author: William Foreman
# This is the second Python Code example from our Head First Python book.
#
#
from datetime import datetime
import time
import random

word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()


