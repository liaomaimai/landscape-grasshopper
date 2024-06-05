import rhinoscriptsyntax as rs
import ghpythonlib.components as ghc
import random
import itertools
import ghpythonlib.treehelpers as th
import Rhino.Geometry as rg
from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path

#定义函数，展开list
flatten_lst=lambda lst:[m for n_lst in lst  for m in flatten_lst(n_lst)] if type(lst) is list else [lst]
#lambda表达式，定义了一个隐藏函数。
#def flatten)lst(lst):
#   return [m for n_lst in lst  for m in flatten_lst(n_lst)] if type(lst) is list else [lst]

def space_truss_cube_pts(pt_start,pt_end,distance,count):
    #建立空间立方体结构，并产生随机变化的点

    #建立X方向单位向量
    vector_x=ghc.Vector2Pt(pt_start,pt_end,True)[0]
    #生成同方向，不同倍数距离的向量
    vectors4XMove=[ghc.Amplitude(vector_x,distance*i) for i in range(count)]
    #将起点沿上方向量列表依次移动
    pts_x=[ghc.Move(pt_start,v) for v in vectors4XMove]

    
    #建立Y方向的单位向量
    vector_y=ghc.Vector2Pt(pt_start,ghc.Rotate(pt_end,ghc.Radians(90),ghc.XYPlane(pt_start)[0]))[0]
    #生成同Y方向，不同倍数距离向量
    vectors4YMove=[ghc.Amplitude(vector_y,distance*i) for i in range(count)]
    #根据X方向点，生成Y方向点
    pts_xy=[[ghc.Move(pt,v) for v in vectors4YMove] for pt in pts_x]

    #建立Z方向单位向量
    vector_z=ghc.UnitZ(distance)
    #生成同Z方向，不同倍数距离向量
    vectors4ZMove=[ghc.Amplitude(vector_z,distance*i) for i in range(count)]
    #根据XY点集，生成三维点集
    pts_xyz=[[[ghc.Move(pt_y,v) for v in vector_z] for pt_y in pts_x] for pts_x in pts_xy]
    #拍平数据
    pts_xyz_tree=th.list_to_tree(pts_xyz)


    #随机半径球体上随机点
    random_radius=map(lambda x:x*distance/2,ghc.Random(ghc.ConstructDomain(0,1),len(flatten_lst(pts_xyz)),Ratio_seed))#map(a,b)函数，a为函数，B为迭代器
    random_sphere=[ghc.Sphere(ghc.XYPlane(pt),r)for pt,r in zip([p  for p in pts_xyz_tree.Branches],random_radius)]
    random_pts=[ghc.PopulateGeometry(s,1,random.uniform(0,1000)) for s in random_sphere]


    #转换tree数据结构
    random_pts_tree=DataTree[rg.Point3d]()
    for pt, path in zip(random_pts, pts_xyz_tree.Paths):
        random_pts_tree.Add(pt, path)
    return random_pts_tree

def space_truss_cube_crvs(pts_tree):
    #A-y和z向折线。通过路径组织分组点
   paths=pts_tree.Paths  
   paths_idx_z=zip(['%s%s%s'%(p[0],p[1],p[2]) for p in paths],paths)
   paths_idx_y=zip(['%s%s%s'%(p[0],p[1],p[3]) for p in paths],paths)   
   crvs_xyz=[]
   
   for paths_idx in([paths_idx_z,paths_idx_y]):#
       paths_idx_sorted=sorted(paths_idx,key=lambda x:x[0][-1]) #按路径最后分枝排序，用于分组
       key_func=lambda x:x[0]            
       paths_group=itertools.groupby(paths_idx_sorted,key_func)
       paths_group_dict={k:[i[1] for i in list(v)] for k,v in paths_group}
       #print(paths_group_dict)
       crvs=[]
       for i in paths_group_dict.values():
           pts=[pts_tree.Branch(p)[0] for p in i]
           #print(pts)
           crv=ghc.PolyLine(pts,False)
           #break
           crvs.append(crv)
       crvs_xyz.append(crvs)
       
   #B-x向折线。方法1，修改path，如下述代码；方法2，用ghc.trees.TrimTree(pts_tree,2)
   paths_x=[GH_Path(p[0],p[1]) for p in paths] 
   pts_tree_x=DataTree[rg.Point3d]()
   for pt,path in zip(pts_tree.Branches,paths_x):
       pts_tree_x.Add(pt[0],path)
   pts_tree_x_flipMatrix=ghc.trees.FlipMatrix(pts_tree_x)
   crvs=ghc.PolyLine(pts_tree_x_flipMatrix,False)
   crvs_xyz.append(crvs)
   
   crvs_xyz_tree=th.list_to_tree(crvs_xyz)
   return crvs_xyz_tree
   
if __name__=="__main__":
   spaceStrussCube_pts=space_truss_cube_pts(pt_start,pt_end,distance,count)
   print('Finished the points calculation...')
   spaceStrussCube_crvs=space_truss_cube_crvs(spaceStrussCube_pts)
   print('Finished the curves calculation...')
