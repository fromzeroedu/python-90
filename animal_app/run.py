import os, sys

print('__file__:', __file__)
script_folder_name = os.path.dirname(__file__)
print('script folder name:', script_folder_name)

parent_relative_path = os.path.join(script_folder_name, '..')
print('parent relative path', parent_relative_path)

root_path = os.path.abspath(parent_relative_path)
print('root path', root_path)

sys.path.append('/Users/jorescobar/python_tests')

from animal_app.canine.dog import Dog

import sys
pluto = Dog()
if len(sys.argv) > 1:
    pluto.sound = sys.argv[1]
print(pluto.make_sound())
