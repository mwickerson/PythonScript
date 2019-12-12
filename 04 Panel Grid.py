import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Number of panels in X Direction
noPanelsX = 5

#Number of panels in Y Direction
noPanelsY = 3

#Width/Size of Panels
sPanelX = 5

#Height/Size of Panels
sPanelY = 10


#Issue another 'for loop' to create a grid of panels

for i in range(noPanelsX):
    #Place your loop for creating a grid within the existing loop and use the variable 'q'
    for q in range(noPanelsY):
        #Double tab the points below to include them in the new loop
        #Each y value is to be set to the variable sPanelY and multiplied (*) by the new loop q e.g. (q*sPanelY)
        #This moves the surface vertically by one whole surface panel every time the loop runs
        pt1=rg.Point3d((i*sPanelX),(q*sPanelY),0)

       #The second and third points need to add the height of the panel after each loop iteration for it to be moved vertically
        pt2=rg.Point3d((i*sPanelX),(q*sPanelY) + sPanelY,0)
        pt3=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY) + sPanelY,0)

        pt4=rg.Point3d((i*sPanelX)+sPanelX,(q*sPanelY),0)

        #Create a surface out of the points
        rs.AddSrfPt( (pt1,pt2,pt3,pt4) )