#import Rhino Script Syntax
import rhinoscriptsyntax as rs

#import Rhino geometry
import Rhino.Geometry as rg

#import Random library
import random


#Point Clouds

#Set up a list of points
pts=[]

#Create random positions

#Create 50 points using a for loop
for i in range(50):
    #Create a random x position and multiply by 25 to give a number between 0 and 25
    xpos = random.random()*25
    #Repeat for Y and Z positions
    ypos = random.random()*25
    zpos = random.random()*25
    
    #Append the points with a tuple containing the x, y and z positions
    pts.append((xpos,ypos,zpos))
    
#Create a point cloud and use the points as the parameter
pointcloud=rs.AddPointCloud(pts)

#The point cloud selects as one object