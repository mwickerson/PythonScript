import rhinoscriptsyntax as rs

#Example 01

#Allow the user to select multiple points using the 'GetObjects' 
#command and filtering it to points using the parameter '1'
pts = rs.GetObjects("Select Pts",1)

#Extract out each point in the points variable and place a circle around that point
for point in pts:
    rs.AddCircle( point, 10)