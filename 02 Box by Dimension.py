import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Box by Dimension

#Define box by dimensions
def boxbydim(x,y,z):

    #Make a box through dimensions rather than points

    #Create 8 points through rg library
    pt1 = rg.Point3d( 0,0,0 )
    pt2 = rg.Point3d( x,0,0 )
    pt3 = rg.Point3d( x,y,0 )
    pt4 = rg.Point3d( 0,y,0 )

    pt5 = rg.Point3d( 0,0,z )
    pt6 = rg.Point3d( x,0,z )
    pt7 = rg.Point3d( x,y,z )
    pt8 = rg.Point3d( 0,y,z )
    

    #Construct a box using the 8 points
    thebox = rs.AddBox( (pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8) )
    
    #Create a loop stating that if the box is made, return true
    if thebox:
        return True

#Create a box by dimensions (5,5,5)
boxbydim(5,5,5)

