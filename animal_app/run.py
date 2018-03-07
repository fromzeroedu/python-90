import os, sys

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
    ))

from animal_app.canine.dog import Dog

import sys
pluto = Dog()
if len(sys.argv) > 1:
    pluto.sound = sys.argv[1]
print(pluto.make_sound())
