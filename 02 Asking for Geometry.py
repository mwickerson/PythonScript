#Asking for Geometry
#We can ask the User to select geometry using the 'Get' command in Python

#Import the geometry library from rhino and assign it an alias
import rhinoscriptsyntax as rs

#Ask the User to select a point in Rhino by accessing the geometry 
#library and calling the "GetPoint" command in Python
rs.GetPoint()

#Assign a message to the command to make it easy for the user to implement
rs.GetPoint("Select Point 1")

#Assign a variable to both points
pt1 = rs.GetPoint("Select Point 1 for line")
pt2 = rs.GetPoint("Select Point 2 for line")

#Use the variable to create a line
#Access the AddLine function from the rs and use pt1 and pt2 as your start and end points
rs.AddLine(pt1,pt2)