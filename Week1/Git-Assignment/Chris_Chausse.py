from will import *
# Chris Chausse
# Date 3/31/2025
# Week 1 Assignment: Writing Functions as a Group/Team

#def rect_area(length, width):
#    return length * width
    
# Written by Chris Chausse    
def rect_surface_area(length, width, height):
    front_back = 2 * rect_area(length, width)
    top_bottom = 2 * rect_area(length, height)
    sides = 2 * rect_area(width, height)
    
    return (front_back + top_bottom + sides)