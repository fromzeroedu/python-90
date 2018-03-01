import sys
sys.path.append('/Users/jorescobar/python_tests')
print(sys.path)

from animal_app.canine.dog import Dog

import sys
pluto = Dog()
if len(sys.argv) > 1:
    pluto.sound = sys.argv[1]
print(pluto.make_sound())
