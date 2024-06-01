#导入相关库
from ghpythonlib.componentbase import executingcomponent as component
import Grasshopper, GhPython
import System
import Rhino
import rhinoscriptsyntax as rs
import os
import subprocess

VScode = 'D:\Microsoft VS Code\Code.exe'

#自定义类，创建组件
class myconmponent(component):

    def RunScript(self,RunVScode,VScode,file,CopyCode):

        ''' 定义函数，运行脚本，包含四个输入变量。
        1开始运行VScode
        2VScode位置
        3python文件位置
        4将python文件中的代码复制到GH中
        '''
        VScode_path = VScode.replace('\\','\\\\')#将文件路径中的‘\’替换为‘\\’，python中，‘\’为转义字符
        file_path = VScode.replace('\\','\\\\')
        command=[VScode_path,file_path]
        process_name='Code'

        def save_file(file_path):
            subprocess.Popen([vscode_path, '--command', 'workbench.action.files.save'], shell=True)
            
        def run_vscode():
            subprocess.Popen(command, shell=True)
            
        def close_vscode():
            save_file(file_path)
            subprocess.Popen(['taskkill', '/F', '/IM', process_name + '.exe'], shell=True)
            
        def copy_content(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
            return file_content
        
        if(RunVSCode):
            if os.path.exists(file):
                run_vscode()
                print("The file is found, opening the file in VSCode succeeded...")
                if(CopyCode):
                    content = copy_content(file_path)
                    Code = content
                    print("File contents are copied from VSCode to Grasshopper Successfully!")
            else:
                command = [vscode_path]
                run_vscode()
                print("The file does not exist, opening VSCode instance without files...")
            
        
        else:
            save_file(file_path)
            close_vscode()
            Code = None
            print("Successfully closed VSCode!")


        return Code




