import xlrd,pickle
"""
data = [
    {'name':'班级名','con':[],'teacher':'','room':''},
    {'name':'未安排老师','con':[] }
]
"""
book = xlrd.open_workbook("练习.xlsx")
sheet1 = book.sheet_by_index(0)
rownum = sheet1.nrows
data = []
for i in range(4,rownum):
    if i>=76:
        cls = {}
        cls['name'] = sheet1.cell_value(i,0).strip()
        data.append(cls)
    elif (i-1)%3==0:
        cls = {}
        name = sheet1.cell_value(i,0).strip()
        cls['teacher'] = sheet1.cell_value(i + 1, 2).strip()

        cls['con'] = [ i for i in  sheet1.row_values(i)[2:] if i!='']
        cls['room'] = sheet1.cell_value(i + 2, 2).strip()
        cls['name'] = name
        data.append(cls)


with open('data.txt','wb') as f:
    pickle.dump(data,f)