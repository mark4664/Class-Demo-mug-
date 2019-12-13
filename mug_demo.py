#!/usr/bin/python3

# Script name: mug_demo.py

# Mark Bradley
# 12/12/19

# demo of a class object built to show the use of a commom tea mug
# test the class as an imported module

# *** NOTE ***
# File mug_class_3.py has to be in the same directory as this file or in your Python path
# so that it can be imported.
    
from mug_class_3 import mug   
    
print('Class mug test')
#'Create an object of class mug - mymug, holds a maximun of 350ml and has a picture of a blue bird'
mymug=mug(350,'Blue Bird')
# Fill mymug
mymug.fill(300,'hot chocolate')
# Check mymug
print(mymug.whatsleft())
# Have a sip from my mug 
mymug.sip(100)
print(mymug.whatsleft())

# Have a big sip
mymug.sip(100)
print(mymug.whatsleft())

# Have a big sip
mymug.sip(50)
print(mymug.whatsleft())

print(mymug + 100)
print(mymug.whatsleft())
# Have a big sip
mymug.sip(50)
print(mymug.whatsleft())
