import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

#Convert curve into an arc

#Evaluate the curve

#Select curve
curve = rs.GetObject("Select a Curve to Subdivide",4)

#Domain of the curve and end points
domain = rs.CurveDomain(curve)
minDom = domain[0]
maxDom = domain[1]

#Start point of curve
stPt=rs.EvaluateCurve(curve,minDom)

#End point of curve
endPt=rs.EvaluateCurve(curve,maxDom)

#Center point of curve
ctrPt = rs.EvaluateCurve(curve,maxDom/2)

#Create an arc by 3 points
arc = rs.AddArc3Pt(stPt,endPt,ctrPt)