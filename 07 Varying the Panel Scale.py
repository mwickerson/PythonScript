import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as m

#Varying the Panel Scale

#Number of panels in X Direction
noPanelsX = 10

#Number of panels in Y Direction
noPanelsY = 5

#Width/Size of Panels
sPanelX = 5

#Height/Size of Panels
sPanelY = 10

#Disable redraw
rs.EnableRedraw(False)


#EXAMPLE 01

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
        
        #Store the box in a variable to be able to use it later to scale the object
        #This acts as the identifier of the geometry
        thepanel=rs.AddBox( (pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8) )
        
        #Add in the parameters to scale the object
        rs.ScaleObject(thepanel,pt1,(0.5,1,1) )



#EXAMPLE 02

for i in range(noPanelsX):
    for q in range(noPanelsY):
        panelHeight=m.random()

        #Scale by a random number
        scalefactor=m.random()
        
        pt1=rg.Point3d((i*sPanelX),(q*sPanelY),0)   
        pt2=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,0)
        pt3=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,0)
        pt4=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),0)
        
        pt5=rg.Point3d((i*sPanelX),(q*sPanelY),panelHeight)   
        pt6=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,panelHeight)
        pt7=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,panelHeight)
        pt8=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),panelHeight)
        
        thepanel=rs.AddBox( (pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8) )
        
        #Add in the parameters to scale the object
        #Replace the x value by the variable 'scalefactor' to add variability to the project
        rs.ScaleObject(thepanel,pt1,(scalefactor,1,1) )



#EXAMPLE 03

for i in range(noPanelsX):
    for q in range(noPanelsY):

        #Multiply your random number for panel height by three to create wider variety in your panel
        panelHeight=m.random()*3

        #Scale by a random number
        scalefactor=m.random()
        
        pt1=rg.Point3d((i*sPanelX),(q*sPanelY),0)   
        pt2=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,0)
        pt3=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,0)
        pt4=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),0)
        
        pt5=rg.Point3d((i*sPanelX),(q*sPanelY),panelHeight)   
        pt6=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,panelHeight)
        pt7=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,panelHeight)
        pt8=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),panelHeight)
        
        thepanel=rs.AddBox( (pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8) )
        
        rs.ScaleObject(thepanel,pt1,(scalefactor,1,1) )

#Enable redraw
rs.EnableRedraw(True)


