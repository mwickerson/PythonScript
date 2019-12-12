#Create a line

import rhinoscriptsyntax as rs

#Example 01
#Add a point in the Rhino file
rs. AddPoint((1,2,3,))

#Example 02
#Allow the user to select a point in the rhino file
pt1 = rs.GetObject("Select Point", 1)
pt2 = rs.GetObject("Select Point 2", 1)

#Create a line between the two points
line = rs.AddLine(pt1,pt2)