import xlrd
import conf.config

# 打开一个Excel，并获取指定的工作表
def get_sheet(file,name):
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name(name)
    return sheet

# 从一个工作表中找到指定用例名的用例数据
def get_case(sheet,case_name):
    # 遍历每一行的数据
    for i in range(1,sheet.nrows):
        # 判断每一行第一列的值是否为指定用例名，满足的话打印该列数据
        if sheet.cell(i,0).value == case_name:
            return sheet.row_values(i)
    # return None

if __name__ == "__main__":
    sh = get_sheet(conf.config.data_path,"注册")
    # print(sh)
    case_data = get_case(sh,"test_user_reg_normal")
    print(case_data)