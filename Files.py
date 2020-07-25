# Files Challenge Question
#
# Read a file and print strings the file as a list.
# Ensure not to count in the special characters:  ! @ # $ % ^ & * ” + - ~
# Try to use exceptional handling, in case the file isn’t found
# Add the sentence “Editing the file through python scripting, wohoooo! " to the file.
#
# Input:
#
# doc1.txt
#
# " Believe you can and you are already halfway there " - roosevelt
#  Document number one
#
# Output:
#
# ['Believe', 'you', 'can', 'and', 'you', 'are', 'already', 'half', 'way', 'there', 'roosevelt', 'Document', 'number', 'one']
#
# The modified file in the end should contain:
#
# " Believe you can and you are already halfway there " - roosevelt
#  Document number one
# Editing the file through python scripting, wohoooo!

import os, sys
import re

if os.path.isfile('doc1.txt'):
    with open('doc1.txt', 'r+') as f:
        s = f.read()
        f.write("\nEditing the file through python scripting, wohoooo!")
else:
    print("File Does Not Exist")
    sys.exit()

sArray = s.split()
result = [x for x in sArray if not re.findall("\W", x)]
print(result)