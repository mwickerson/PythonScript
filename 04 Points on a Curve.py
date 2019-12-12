import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Points on a Curve

#Allow user to select curve using rhinoscriptsyntax 'GetObject' command
#and use filter '4' to allow them to only select a curve (check this in the 'help' dialogue)
curve = rs.GetObject("Select a Curve to Subdivide",4)

#Get the domain of the curve and assign the curve to the domain parameter
domain = rs.CurveDomain(curve)

#Extract out end points of the curve and store them in variables
minDom = domain[0]
maxDom = domain[1]

#Define the number of divisions on the curve
noDiv = 10

#Create a loop to extract individual parameters of curve
#Increase the number of divisions by 1 to account for the loop starting at 0 instead of 1
for i in range(noDiv + 1):

    #Create the step size and multiply by 'i' to increment the step size each time the loop runs 
    param = ((maxDom - minDom)/noDiv)*i
    print param
    
    #Evaluate the curve (requires curve_id and parameter)
    crvPt = rs.EvaluateCurve(crv,param)

    #Print the points to see the tuples of each point
    print crvPt
    
    #Add subdivided points into the rhino document
    rs.AddPoint(crvPt)


