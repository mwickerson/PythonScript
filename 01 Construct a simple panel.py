#To work with geometry, import rhinoscriptsyntax and assign it an alias 'rs'
#This gives you access to all of the rhino commands
import rhinoscriptsyntax as rs

#Create four points and add a Tuple into its parameters
#The tuple must be in its own parentheses
rs.AddPoint( (0,0,0) )
rs.AddPoint( (0,5,0) )
rs.AddPoint( (5,5,0) )
rs.AddPoint( (5,0,0) )

#Assign variables to points
pt1 = rs.AddPoint( (0,0,0) )
pt2 = rs.AddPoint( (0,5,0) )
pt3 = rs.AddPoint( (5,5,0) )
pt4 = rs.AddPoint( (5,0,0) )

#Use the above points to make a surface
rs.AddSrfPt((pt1,pt2,pt3,pt4))
