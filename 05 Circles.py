import rhinoscriptsyntax as rs

#Circles

#Add a circle into your rhino file using the 'AddCircle' command
#This command required a tuple as your center point and a radius
rs.AddCircle( (0,0,0), 10)