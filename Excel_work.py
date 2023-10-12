import openpyxl

# 创建一个新的Excel工作簿
workbook = openpyxl.Workbook()

# 选择默认的工作表
sheet = workbook.active

# 写入数据到工作表
sheet['A1'] = '姓名'
sheet['B1'] = '年龄'
sheet['A2'] = 'John'
sheet['B2'] = 30
sheet['A3'] = 'Alice'
sheet['B3'] = 25

# 保存工作簿
workbook.save('office_example.xlsx')

# 打开现有的Excel文件
existing_workbook = openpyxl.load_workbook('office_example.xlsx')

# 选择工作表
existing_sheet = existing_workbook.active

# 读取数据
name = existing_sheet['A2'].value
age = existing_sheet['B2'].value

print(f'姓名: {name}, 年龄: {age}')

# 进行更多的操作，如修改、添加数据等

# 保存更改
existing_workbook.save('office_example.xlsx')
