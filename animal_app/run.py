import os, sys

sys.path.append(os.path.abspath(
<<<<<<< HEAD
    os.path.join(os.path.dirname(__file__), '..')
=======
        os.path.join(os.path.dirname(__file__), '..')
>>>>>>> bf2ea48d6c5be0c1c8a0c069ee61425c5e8b0a97
    ))

from animal_app.canine.dog import Dog

import sys
pluto = Dog()
if len(sys.argv) > 1:
    pluto.sound = sys.argv[1]
print(pluto.make_sound())
