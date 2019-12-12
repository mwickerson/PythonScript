import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random

#Recursive Network

#EXAMPLE 02

#Ask the user to select a curve
crv = rs.GetObject("Select Base Curve",4)

#Define the ratio as a decimal number (parameters require message,minimum and maximum number)
ratio = rs.GetReal("Input decimal number for Ratio",0.2,0,1)

#Define the starting scale as a decimal number
scale = rs.GetReal("Input decimal number for Scale",0.7,0,1)

#Set the direction
dir = 1

#Make a recursion function (curve, ratio, scale, direction, no. iterations)
def network(crv,ratio,scale,dir,no):
    if no<1:
        return True
    else:
        print no
        
        #Get the point parameter along your line
        #Curve domain
        crvdom = rs.CurveDomain(crv)
        
        #Parameters equal the curve domain start plus the curve domain length, multiplied by the scale factor
        param = crvdom[0] + ((crvdom[1]-crvdom[0])*scale)

        #Evaluate the curve > This will give you the curve point
        crvPt = rs.EvaluateCurve(crv,param)

        #Set up different direction behaviours 
        
        #If direction = 1, move right (double == represents equals)
        if dir==1:
            x=1
            y=0
            
        #if direction = 2, move down
        if dir==2:
            x=0
            y=-1
            
        #if direction = 3, move up and right
        if dir==3:
            x=1
            y=1
            
        #if direction = 4, move up
        if dir==4:
            x=0
            y=1
            
        #if direction = 5, move left
        if dir==5:
            x=-1
            y=0


        #Set up direction vector
        vec=rg.Vector3d(x,y,0)


        #Alter direction for next iteration
        
        #If direction is less than set behaviours, add one value to the direction
        #This moves onto the next direction for the next iteration
        if dir<5:
            dir=dir+1
        #If dir>5, the direction should be equal to 1
        else:
            dir=1


        #Calculate new line distance
        newdist = rs.CurveLength(crv)*scale

        #Multiple the new distance by the direction
        lineVector = rs.VectorScale(vec,newdist)

        #Determine the end point of the line
        endPt = rs.VectorAdd(crvPt,lineVector)

        #Add line to document
        crvchild = rs.AddLine(crvPt,endPt)

        #Terminate the line
        terminate = rs.AddCircle(endPt,newdist*0.01)

        #Call Recursion
        network(crvchild, ratio, scale, dir, no-1)

        #Call Recursion Again > Send recursion in different direction
        network(crvchild, ratio, scale, 1, no-5)

#Create Recursion
network(crv,ratio,scale,dir,25)