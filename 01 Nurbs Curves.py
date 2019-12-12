#Import libraries
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import scriptcontext as sc

#Nurbs curves and surfaces

#Add some points into the rhino file

#Allow the user to select the points in the rhino file
pts = rs.GetObjects("Select Points",1)

#Override the points with the "coerce" command in the rhinoscriptsyntax library
#Coerce the guids into a 3d point list

#Print the points before coercing them
print "before coerce:",pts
pts = rs.coerce3dpointlist(pts)

#Print the points after coercing them
#The points should now be actual point objects rather than identification numbers (Guids)
print "after coerce:",pts

#Create a nurbs curve using the command "Nurbs.Curve.Create" in the 
#rhino geometry library
#This requires a boolean to open/close the curve, degree and points
nc = rg.NurbsCurve.Create(False,3,pts)

#Because we used the rg file instead of the rs, the curve is not added to the document
#To add curve 'nc' to the rhino document, use the scriptcontext library
#Open the objects in the document using 'sc.doc.objects' and 'AddCurve' to the document
sc.doc.Objects.AddCurve(nc)

#Refresh the screen using 'redraw' to show the curve
sc.doc.Views.Redraw()