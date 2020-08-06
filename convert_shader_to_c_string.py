
#!/usr/bin/python

import os
import argparse

parser = argparse.ArgumentParser(description='Convert GLSL File to C++/C embbeded code string')
parser.add_argument('--input', action='store', type=str, dest='input', help="The GLSL file to convert")


args = parser.parse_args()


filename = args.input

if not os.path.isfile(filename):
    print('invalid file', filename)
    exit(-1)


with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        newLine = r'test\n'
        print(repr(line).replace('\'', '"'))

exit(0)
