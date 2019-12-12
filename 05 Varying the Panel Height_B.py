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

#EXAMPLE O2
#Introduce variability by importing random geometry

#Import random numbers library with the alias 'm'
import random as m

for i in range(noPanelsX):
    for q in range(noPanelsY):

        #Set the panel height to a random number
        panelHeight=m.random()
        
        pt1=rg.Point3d((i*sPanelX),(q*sPanelY),0)   
        pt2=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,0)
        pt3=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,0)
        pt4=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),0)
        
        pt5=rg.Point3d((i*sPanelX),(q*sPanelY),panelHeight)   
        pt6=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,panelHeight)
        pt7=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,panelHeight)
        pt8=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),panelHeight)
        
        rs.AddBox( (pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8) )

