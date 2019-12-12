#Import libraries
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

#Allow the user to select the points in the rhino file
pts = rs.GetObjects("Select Points",1)

#Coerce the guids into a 3d point list
pts = rs.coerce3dpointlist(pts)

#Create a nurbs curve
nc = rg.NurbsCurve.Create(False,3,pts)


#ALTERNATE technique to creating a curve using the rg library
#Create a polyline instead of a curve
pl = rg.Polyline(pts)

#Add the polyline to the rhino document
sc.doc.Objects.AddPolyline(pl)


#Add the curve to the rhino document
sc.doc.Objects.AddCurve(nc)

#Redraw the curve
sc.doc.Views.Redraw()




