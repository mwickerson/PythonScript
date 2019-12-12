import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Using Conditionals

#Selecting an attractor point
att = rs.GetObject("Select Attractor",1)

#Selecting the field of points
field = rs.GetObjects("select pt Field",1)

#Create a variable for the field of influence of the attractor
fieldofinfluence = 15

#Add a circle (field of influence) using the attractor points and a radius
rs.AddCircle(att,fieldofinfluence)

#Cycle through the field
for pt in field:

    #Coerce the data into a single point
    thept = rs.coerce3dpoint(pt)

    #Add conditions
    #If the distance between the point and the attractor is less than the fieldofinfluence
    if rs.Distance(pt,att) < fieldofinfluence:

    #If the object is within this influence, add a line
        rs.AddLine(pt,(thept[0],thept[1]