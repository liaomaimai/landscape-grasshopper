"""
input:
    curve:定义汀步路线
    length:汀步长度
    width:汀步宽度
    spacing:两个汀步之间的间距
output:
    Trails:最后的汀步box

"""
import rhinoscriptsyntax as rs
import ghpythonlib.components as ghc

def trail_size(point,length,width,highth=50):
    box=ghc.CenterBox(point,length,width,highth)
    print(box)
    #根据点，生产单个汀步
    return box
    

def creat_points(curve,space,width):
    curve_length=rs.CurveLength(curve)
    print(curve_length)
    #获得曲线分割距离
    divide_length=space+width
    #得到box中心的frame

    points_t=rs.DivideCurveLength(curve,divide_length)
    print(points_t)
    frames=rs.CurveFrame(curve,points_t)
    print(frames)

    return points

if __name__ =="__main__":
    points = creat_points(curve,space,width)
    print('divided succed')
    Trails = trail_size(points,length,width,highth)
    print('finished')
