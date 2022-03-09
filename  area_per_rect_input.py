#!/usr/bin/env python3
# Created by: Titwech wal
# Created on: Mar. 05. 2022

#program calculates the area and perimeter 
#of a rectangle with the user input

import math

def main():
      # input
        print("Lets calculate the area and")
        print("perimeter of a rectangle")
        length = int(input("Enter the length (cm): "))
        width = int(input("Enter the width (cm): "))
        
        #calaution input 
        area = length * width 
        perimeter = 2*(length * width)
        
        #output
        print ("Area = {} mm^2". format (area))
        print ("Perimeter = {} mm". format (perimeter))
        
if __name__ == "__main__":
    main()