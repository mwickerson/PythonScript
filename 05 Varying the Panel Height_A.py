import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Varying the Panel Height

#Number of panels in X Direction
noPanelsX = 5

#Number of panels in Y Direction
noPanelsY = 3

#Width/Size of Panels
sPanelX = 5

#Height/Size of Panels
sPanelY = 10

panelheight = 1


#EXAMPLE 01

for i in range(noPanelsX):
    for q in range(noPanelsY):
        pt1=rg.Point3d((i*sPanelX),(q*sPanelY),0)   
        pt2=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,0)
        pt3=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,0)
        pt4=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),0)
        
        #Create four new points and give them Z values
        #The Z value will be the panelheight
        pt5=rg.Point3d((i*sPanelX),(q*sPanelY),panelheight)   
        pt6=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,panelheight)
        pt7=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,panelheight)
        pt8=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),panelheight)
        
        #Create a box using the "AddBox" method in the rhino geometry library
        rs.AddBox( (pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8) )

