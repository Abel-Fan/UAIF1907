# xlwt  写入数据到excel
# xlrd  从excel中读数据
# python-docx  world文档包
import xlrd,xlwt

book = xlrd.open_workbook("data1.xlsx")
sheet1 = book.sheet_by_index(0)
# 表名
# print(sheet1.name)
# 行数
# print(sheet1.nrows)
# 列数
# print(sheet1.ncols)

# 遍历每一行
# for i in range(0,sheet1.nrows):
#     print(sheet1.row(i))
# 查看单元格
# data = sheet1.cell(2,2)  # 单元格对象
# sheet1.cell_type() # 单元格类型
# sheet1.cell_value() # 单元格内容
# print(data.ctype)  # 1
# print(data.value)  # 男

[
    {
        'classname':'WUIF1903',
        'classcon':['全栈-13',],
        '布道师':"王琦",
        '教室':'507实训室'
    },
 {},{},
    {
        '提升老师':[],
        '助教老师':[]
    }]
