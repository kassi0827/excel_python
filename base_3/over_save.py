import openpyxl

# ディレクトリのパス
dir_path = '/Users/kashimataichi/play_python/excel_python/base_3/'

# コピー元のエクセルファイルのパス
excel_path = dir_path + 'Book1.xlsx'

# コピー先のエクセルファイルのパス
copy_excel_path = dir_path + 'target_over_save/Book1.xlsx'

wb = openpyxl.load_workbook(excel_path)
wb.save(copy_excel_path)
