'''
objectsList AccessGeometryBase

path:a new 3dm
'''

import Rhino
import System

#创建一个新的空doc
doc=Rhino.RhinoDoc.CreateHeadless(None)

#将gh对象写入doc
if not objects is None:
    for o in objects:
        doc.Objects.Add(o)


options = Rhino.FileIO.File3mfWriteOptions()
options.Title = title
options.Designer = Rhino.RhinoApp.LicenseUserName
options.Metadata["Test"] = "Star"
options.MoveOutputToPositiveXYZOctant = True;



#导出
if not path is None:
    path=System.Environment.ExpandEnvironmentVariables(path)
    success=doc.Export(path)
    print(success)

doc.Dispose()