#Import rhinoscriptsyntax
import rhinoscriptsyntax as rs
#Import the rhino geometry library in addition to the rhinoscriptsyntax and give it an alias rg
import Rhino.Geometry as rg

#Using rg instead of rs creates a surface in rhino without adding points
#This is useful for construction geometry
#These points do not require tuples
pt1 = rg.Point3d(0,0,0)
pt2 = rg.Point3d(0,5,0)
pt3 = rg.Point3d(5,5,0)
pt4 = rg.Point3d(5,0,0)

#Use the above points to make a surface
rs.AddSrfPt((pt1,pt2,pt3,pt4))
