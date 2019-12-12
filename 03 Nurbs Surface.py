import rhinoscriptsyntax as rs

#Nurbs surface

#Allow the user to select the points in the rhino file
pts = rs.GetObjects("Select Pt Grid",1)

#Add a surface by Point Grid (requires count in two directions (u and v),
#points and degree in both directions)
#The degree is set to a default of 3
rs.AddSrfPtGrid( (3,5), pts )