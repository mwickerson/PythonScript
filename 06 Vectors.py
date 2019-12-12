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

    #Curve Frame
    crvFrame = rs.CurveFrame(curve,param)

    #Add a curve tangent to each point
    crvTan = rs.CurveTangent(curve,param)

    #Scale the curve tangent to make it more visible in the rhino file
    crvTan = rs.VectorScale(crvTan,10)

    #To draw a line on each point and map out each tangent, you need 
    #to add a tangent point in the form of a vector to each subdivided point
    tanPt = rs.VectorAdd(crvPt,crvTan)

    #Add subdivided points into the rhino document
    rs.AddPoint(crvPt)

    #Add a line from the curve point (crvPt) to the tangent point (tanPt)
    rs.AddLine(crvPt,tanPt)

    #Add a surface to the normal of each point of the curve
    rs.AddPlaneSurface(crvFrame,1,5)
