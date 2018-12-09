import xlrd

# 打开Excel(work_book)
excel = xlrd.open_workbook("../data/data.xlsx")

# 指定工作表
# sheet = excel.sheet_by_name("登录")
# 0是登录第一个工作表，1是第二个工作表注册
# sheet = excel.sheet_by_index(0)

# 有效数据行数
# print(sheet.nrows)
# # 有效数据列数
# print(sheet.ncols)
#
# # 打印第x行数据
# print(sheet.row_values(0))
# print(sheet.row_values(1))
# print(sheet.row_values(2))
#
# # 打印某一单元格的数据
# print(sheet.cell(0,0).value)
# print(sheet.cell(2,0).value)
# print(sheet.cell(1,2).value)

# 遍历注册表
# sheet1 = excel.sheet_by_name("注册")
# for b in range(1,sheet1.nrows):
#      print(sheet1.row_values(b))

