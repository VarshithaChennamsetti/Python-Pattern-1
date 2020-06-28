# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 20:51:58 2020

@author: Varshitha
"""

padding=int(input("Enter the padding: "))#to print the diamond after some spacing (just for printing it wherever we want)
ch=True

while(ch==True): #Loop to check if correct input for the pattern is given
    Max_width=int(input("Enter the maximum width of the diamond: "))
    if(Max_width%2==0 or Max_width<2):
        print("Number needs to be even and greater than 1, please enter again!")
    else:
        ch=False
        print("\n")
    
for row in range(0,Max_width): #Main loop for pattern
    no_of_stars=(2*row)+1
    start_at=(Max_width/2)-row
    if(no_of_stars>Max_width): #To print the stars in reverse after Max_width
        no_of_stars=((Max_width-row-1)*2)+1
        start_at=(Max_width/2)-(Max_width-row-1)
    print(" "*padding,end=" ")
    for col in range(0,Max_width):
        if(col>=start_at):
            print("*"*no_of_stars,end=" ")
            break
        else:
            print(end=" ")
    print("\n")
    