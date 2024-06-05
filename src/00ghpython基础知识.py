#导入相关库
import Rhino
import scriptcontext
import Rhino.Geometry as rg
import ghpythonlib.components as ghc
import rhinoscriptsyntax as rs


if B:
    print(type(G))
    #we obtain the reference in the rhino doc
    doc_object = scriptcontext.doc.Objects.Find(G)
    print(type(doc_object))

    attribute = doc_object.Attributes
    print(type(attribute))

    geometry=doc_object.Geometry
    print(str(type(doc_object)))

    #we change the scriptcontext
    scriptcontext.doc=Rhino.RhinoDoc.ActiveDoc

    #we both the geomety and the attributes to the rhino doc
    rhino_berp=scriptcontext.doc.Objects.Add(geometry,attribute)
    print(rhino_berp)


    