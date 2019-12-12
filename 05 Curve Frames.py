import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Curve Frames

#Select curve
curve = rs.GetObject("Select a Curve to Subdivide",4)

#Domain of the curve
domain = rs.CurveDomain(curve)

#End points
minDom = domain[0]
maxDom = domain[1]

#Number of divisions
noDiv = 10

#Extract individual parameters of curve
for i in range(noDiv + 1):

    #Step size
    param = ((maxDom - minDom)/noDiv)*i
    
    #Evaluate the curve
    crvPt = rs.EvaluateCurve(curve,param)

    #Create a curve Frame (requires curve_id and parameter)
    crvFrame = rs.CurveFrame(curve,param)

    #Add subdivided points into the rhino document
    rs.AddPoint(crvPt)

    #Add a surface to the normal of each point of the curve
    rs.AddPlaneSurface(crvFrame,1,5)