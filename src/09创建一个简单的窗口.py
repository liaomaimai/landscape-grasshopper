#! python3
 
# Imports
import Rhino
import scriptcontext
import System
import rhinoscriptsyntax as rs
# Eto组件
import Rhino.UI
import Eto.Drawing as drawing
import Eto.Forms as forms
 
# SampleEtoRoomNumber dialog class
# 创建一个案例类，该类继承forms.Dialog类
class SampleEtoRoomNumberDialog(forms.Dialog[bool]):
 
    # Dialog box Class initializer
    def __init__(self):
        super().__init__()
        # Initialize dialog box
        self.Title = 'Sample Eto: Room Number'
        self.Padding = drawing.Padding(10)
        self.Resizable = False
 
        # Create controls for the dialog
        # 创建输入信息
        self.m_label = forms.Label()
        self.m_label.Text = 'Enter the Room Number:'
        self.m_textbox = forms.TextBox()
        self.m_textbox.Text = ""
 
        # Create the default button
        # 默认按钮
        self.DefaultButton = forms.Button()
        self.DefaultButton.Text ='creat'
        self.DefaultButton.Click += self.creat_line
 
        # Create the abort button 
        # 中止按钮
        self.AbortButton = forms.Button()
        self.AbortButton.Text ='Cancel'
        self.AbortButton.Click += self.OnCloseButtonClick
 
        # Create a table layout and add all the controls
        # 创建布局
        layout = forms.DynamicLayout()
        layout.Spacing = drawing.Size(5, 5)
        layout.AddRow(self.m_label, self.m_textbox)

        layout.AddRow(None) # spacer
        
        layout.AddRow(self.DefaultButton, self.AbortButton)
 
        # Set the dialog content
        self.Content = layout
 
    # Start of the class functions
 
    # Get the value of the textbox
    def GetText(self):
        return self.m_textbox.Text
 
    # Close button click handler
    def OnCloseButtonClick(self, sender, e):
        self.m_textbox.Text = ""
        self.Close(False)
 
    # OK button click handler
    def OnOKButtonClick(self, sender, e):
        if self.m_textbox.Text == "":
            self.Close(False)
        else:
            self.Close(True)
 
    ## End of Dialog Class ##
    def creat_line(self,sender,e):
        point_a = (0,0,0)
        point_b = (self.GetText(),0,0)
        self.Close(False)
        return rs.AddLine(point_a,point_b)
 
# The script that will be using the dialog.
def RequestRoomNumber():
    dialog = SampleEtoRoomNumberDialog()
    # 将dialog与rhinoui交互10
    rc = dialog.ShowModal(Rhino.UI.RhinoEtoApp.MainWindow)
    if (rc):
        print(dialog.GetText()) #Print the Room Number from the dialog control
 
##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if __name__ == "__main__":
    RequestRoomNumber()