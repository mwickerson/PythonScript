import rhinoscriptsyntax as rs

#Example 02

#Attractors
#Select a single attractor point using the 'GetObject' command
attPt = rs.GetObject("Select Attractor",1)

#Allow the user to select multiple points using the 'GetObjects' 
#command and filtering it to points using the parameter '1'
pts = rs.GetObjects("Select Pts",1)

#Extract out each point in the points variable and place a circle around that point
for point in pts:
    #Vary the size of the circle based on its distance from the attractor point
    dist = rs.Distance(attPt,point)
    radius = dist/10
    #Add a circle to each point using the variables for the point and radius
    rs.AddCircle(point, radius)