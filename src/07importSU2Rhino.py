import Rhino
import os

doc=Rhino.RhinoDoc.CreateHeadless(None)
options=Rhino.FileIO.FileSkpReadOptions()
options.ImportCurves = False #不导入曲线
options.EmbedTexturesInModel = False #不导入材质

path = os.path.expanduser(r"C:\Users\2022169\Desktop\test\testsutothino.skp")
doc.Import(path,options.ToDictionary())
print(f"{doc.Objects.Count} objects")

for obj in doc.Objects:
    bbox=obj.Geometry.GetBoundingBox(True)
    print(f"Center is {bbox.Center}")

doc.Dispose()