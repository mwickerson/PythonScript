import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#CREATE YOUR PARAMETERS

#Number of panels
noPanelsX = 5

#Width/Size of Panels
sPanelX = 5

#Height/Size of Panels
sPanelY = 10



#EXAMPLE 01

#Create a row of panels through a loop
#This creates 5 panels on top of each other
#Make sure to tab in all the lines included in the loop
for i in range(noPanelsX):
    pt1=rg.Point3d(0,0,0)
    pt2=rg.Point3d(0,5,0)
    pt3=rg.Point3d(5,5,0)
    pt4=rg.Point3d(5,0,0)

#Create a surface out of the four points
    rs.AddSrfPt( (pt1,pt2,pt3,pt4) )




#EXAMPLE 02

#To space out each panel, move each point by the appropriate spacing required 

for i in range(noPanelsX):
    
    #Each x value is to be set to the variable sPanelX and multiplied (*) by i e.g. (i*sPanelX)
    #This moves the surface horizontally by one whole surface panel every time the loop runs
    #Point one starts at (0,0,0)
    pt1=rg.Point3d((i*sPanelX),0,0)
    
    #At this stage, the y value does is not required to change with every iteration and 
    #therefore can be set to sPanelY to move it vertically by the variable panel height
    pt2=rg.Point3d((i*sPanelX),sPanelY,0)

    #The third point needs to add the length of the panel to point two for it to be moved horizontally across
    pt3=rg.Point3d((i*sPanelX)+sPanelX,sPanelY,0)

    #Similarly, the fourth point needs to add the length of the panel to point one for it to be moved horizontally across
    pt4=rg.Point3d((i*sPanelX)+sPanelX,0,0)

    #Create a surface out of the four points
    rs.AddSrfPt( (pt1,pt2,pt3,pt4) )