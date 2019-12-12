import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random

pts=[]

for i in range(50):
    xpos = random.random()*25
    ypos = random.random()*25
    zpos = random.random()*25
    
    pts.append((xpos,ypos,zpos))
    
pointcloud=rs.AddPointCloud(pts)

#Select the point cloud using the 'SelectObject' command and store them 
#in a variable 'selObj'
selObj=rs.SelectObject(pointcloud)

#Issue a rhino command to explode the point cloud
#When using macros, add an underscore (_) between each command to link the commands together
#Macros require a space after each command
rs.Command("_explode _Enter")

#Add a polyline between the selected point cloud objects
rs.AddPolyline( rs.SelectedObjects() )

#These points are only temporary geometry
#We can delete these objects using the 'DeleteObjects' command
rs.DeleteObjects( rs.SelectedObjects() )