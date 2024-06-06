from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path
import Rhino.Geometry as rg
import ghpythonlib.components as ghc
import ghpythonlib.treehelpers as th
import random
import itertools

flatten_lst=lambda lst: [m for n_lst in lst for m in flatten_lst(n_lst)] if type(lst) is list else [lst]


def space_truss_cube_pts(pt_start,pt_end,distance,count,):

   #A-X向点（单排）
   vector_x=ghc.Vector2Pt(pt_start,pt_end,True)[0]
   vectors4Xmove=[ghc.Amplitude(vector_x,distance*i) for i in range(count)]
   pts_x=[ghc.Move(pt_start,v)[0] for v in vectors4Xmove]
   
   #B-Y向点（多排）
   vector_y=ghc.Vector2Pt(pt_start,ghc.Rotate(pt_end,ghc.Radians(Rotate),ghc.XYPlane(pt_start))[0],True)[0]
   vectors4Ymove=[ghc.Amplitude(vector_y,distance*i) for i in range(count)]
   pts_xy=[[ghc.Move(pt,v)[0] for v in vectors4Ymove] for pt in pts_x]
   
   #C-Z向点（三维矩阵）
   vector_z=ghc.UnitZ(distance)
   vectors4Zmove=[ghc.Amplitude(vector_z,distance*i) for i in range(count)]
   pts_xyz=[[[ghc.Move(pt_y,v) for v in vectors4Zmove] for pt_y in pts_x] for pts_x in pts_xy]
   pts_xyz_tree=th.list_to_tree(pts_xyz)
   
   #D-随机半径球体上随机点
   random_radius=map(lambda x:x*distance/2,ghc.Random(ghc.ConstructDomain(0,1),len(flatten_lst(pts_xyz)),Ratio_seed))
   random_sphere=[ghc.Sphere(ghc.XYPlane(pt),r) for pt,r in zip([p[0] for p in pts_xyz_tree.Branches],random_radius)]
   random_pts=[ghc.PopulateGeometry(pt,1,random.uniform(0,10000)) for pt in random_sphere]
   
   #E-转换为Tree类型数据结构
   random_pts_tree=DataTree[rg.Point3d]()
   for pt,path in zip(random_pts,pts_xyz_tree.Paths):
       random_pts_tree.Add(pt,path)
   
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
