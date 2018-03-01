from animal.canine.dog import Dog

import sys
pluto = Dog()
if len(sys.argv) > 1:
    pluto.sound = sys.argv[1]
print(pluto.make_sound())
