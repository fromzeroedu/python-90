import os, sys

print('__file__:', __file__)
script_folder_name = os.path.dirname(__file__)
print('script folder name:', script_folder_name)

sys.path.append('/Users/jorescobar/python_tests')

from animal_app.canine.dog import Dog

import sys
pluto = Dog()
if len(sys.argv) > 1:
    pluto.sound = sys.argv[1]
print(pluto.make_sound())
