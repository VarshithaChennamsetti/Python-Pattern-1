# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:40:18 2020

@author: Varshitha
"""
ch=True
while(ch==True): #Valid Inputs
    triangles=int(input("Enter the no. of triangles in the christmas tree: "))
    layers=int(input("Enter the no. of layers per each triangle: "))
    if(triangles<2 and layers<3):
        print("\nGive valid numbers: Numbers have to be positive and layers>2 and triangles>1 to make a pretty tree!")
        print("Please enter again!")
    else:
        print()
        ch=False


total_rows=triangles*(layers+1) #to get the extra stand for tree to stand upon
max_width=triangles*layers
for row in range(0,total_rows):
    if(row<layers): #for the first triangle
        no_stars=row+1
    elif(row%layers==0 and row>0 and row<max_width): #Start of every triangle
        no_stars=no_stars-1
    elif(row>=max_width): #for the stand
        no_stars=triangles
    else: #all other layers in each triangle
        no_stars=no_stars+1
    start_at=abs(max_width-(no_stars-1))
    for col in range(0,total_rows*2):
        if(col==start_at):
            print("* "*no_stars,end=" ")
        else:
            print(end=" ")
    print()