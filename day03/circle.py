# This is a file for assignment 3

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--radius', help='Enter a circle\'s radius', required=True, type=int) 
args = parser.parse_args()

radius = args.radius
pi = 3.14

area = pi*(radius**2)
circumference = 2*pi*radius

print (f"The area of the circle is {area}.")
print (f"The circumference of the circle is {circumference}.")