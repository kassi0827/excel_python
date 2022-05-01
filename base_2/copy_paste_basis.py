import openpyxl

# この実行ファイルのパス
cur_path = "/Users/kashimataichi/play_python/excel_python/base_2/"
excel_path = cur_path + "Book2.xlsx"

wb = openpyxl.load_workbook(excel_path)

cp_data_sheet = wb['Sheet2']
pt_data_sheet = wb['Sheet3']

# エクセルファイルを開いていると実行されない。閉じていることが必須。
pt_data_sheet['A1'].value = cp_data_sheet['A1'].value
print(pt_data_sheet['A1'].value)

wb.save(excel_path)
