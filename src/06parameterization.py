import os
import pandas as pd

def recursive_listdir(path):
    files = os.walk(path)
    return files

def to_excel(list1,file_name):

    # 创建 DataFrame
    df1 = pd.DataFrame({file_name: list1})

        # 创建文件路径
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'{file_name}.xlsx')
        
    # 将 DataFrame 写入 Excel 文件
    df1.to_excel(file_path, sheet_name='Sheet1', index=False)
        
    return '写入成功'



# 调用函数
path1 = "Y:\\6 项目归档\\3 施工图归档\\施工图成果\\景观\\盖章PDF\\20230615_计量院景观施工图"
path2 = "Y:\\6 项目归档\\3 施工图归档\\施工图成果\\景观\\盖章PDF\\20230613 深圳计量科学院 景观电气 DWG+PDF"
path3 = "Y:\\6 项目归档\\3 施工图归档\\施工图成果\\景观\\盖章PDF\\20230615_深圳计量院景观给排水-招标"
path4 = r"Y:\6 项目归档\3 施工图归档\施工图成果\景观\盖章PDF\深圳计量科学院照明图纸（景观泛光） 2023.06.12"

result1 = to_excel(recursive_listdir(path1),"la")
result2 = to_excel(recursive_listdir(path2),"dq")
result3 = to_excel(recursive_listdir(path3),"gps")
result4 = to_excel(recursive_listdir(path4),"fgzm")
print(result1,result2,result3,result4)


#下一步，进一步获取文件名，筛选出需要的文件名