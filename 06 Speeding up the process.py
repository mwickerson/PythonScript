import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as m

#Speeding up the process

#Number of panels in X Direction
noPanelsX = 5

#Number of panels in Y Direction
noPanelsY = 3

#Width/Size of Panels
sPanelX = 5

#Height/Size of Panels
sPanelY = 10

#Disable the redrawing so that the script processes the geometry only 
#once in its memory instead of redrawing it every time the loop runs
rs.EnableRedraw(False)

for i in range(noPanelsX):
    for q in range(noPanelsY):
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


#Enable redraw at the end of the script and turn on the display to 
#speed up the processing time of your script
rs.EnableRedraw(True)
