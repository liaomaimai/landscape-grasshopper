"""
input:
    file_path:excel文件路径;Data structure:Item Access
    worksheet_num:表的索引;Data structure:ItemAccess
    test_rowNum:如果测试，指定测试行数，default=10;Data structure:ItemAccess
output:
    data:读取的表数据，Tree类型数据结构
"""

import rhinoscriptsyntax as rs
import clr 
import ghpythonlib.treehelpers as th

def read_excel(file_path,worksheet_num=1,test_rowNum=10):
    #使用clr包，在ghpython中调用Cpython
    clr.AddReference("Microsoft.Office.Interop.Excel")
    #导入需要的模块
    import Microsoft.Office.Interop.Excel as excel
    #create excel opp
    ex=excel.ApplicationClass()
    #打开workbook
    workbook=ex.Workbooks.open(file_path)
    #读取excelsheets
    ws=workbook.worksheets[worksheet_num]
    #print(help(workbook))
    columns=map(chr,range(65,91)) #chr()函数，接受一个整数，返回对应ASCII码，65-91对应从字面A到Z
    #print(columns)
   
    data_dict={}  #创建一个字典，用来存放每行的数据

    #遍历每一行
    for i in range(ws.UsedRange.Rows.Count):
        #print(i)
        #判断该行是否有数据
        if i==0:
            #如果没有，跳过
            continue
        #创建一个list,用来存放行数据
        row_data=[]
        #遍历第I行的每一列
        for j in columns:
            cell_data=ws.Range("{}{}".format(j,i + 1)).Value2 #"{}{}".format(j,i+1)是python的格式化表达，用来生成excel中的单元格地址，后边.Value2用来读取当前单元格数据
            if cell_data:
                row_data.append(cell_data)
            else:
                break
        data_dict[i]=row_data
        if test_rowNum:
            print("Testing rows:%d"%test_rowNum)
            if i==test_rowNum:break
        #if i==30:break
    workbook.Close(True)
    ex.Quit()

    #
    data_tree=th.list_to_tree(data_dict.values())
    return data_tree

if __name__=="__main__":

    if worksheet_num:
        if test_rowNum:
            data=read_excel(file_path,worksheet_num,test_rowNum)
        else:
            data=read_excel(file_path,worksheet_num)
    else:
        if test_rowNum:
            data=read_excel(file_path,test_rowNum=test_rowNum)
        else:
            data=read_excel(file_path)