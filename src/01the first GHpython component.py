import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

pt=rs.AddPoint(5,4,3)
pt2=rg.Point3d(57,4,3)

print(rs.AddPoint(7,8,9))

print(pt2)