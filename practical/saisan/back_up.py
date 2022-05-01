import xlwings as xw

# back_up_fi　でターミナルで実行可能

# 【変数定義】
# ディレクトリのパス
dir_path = '/Users/kashimataichi/Desktop/採算管理/'
# 記帳中フォルダ
working_dir = '当期記帳中/'
# バックアップフォルダ
back_up_dir = 'バックアップ/'
# エクセルファイル名
excel_file_name = 'PL_BS_CF_FY2022.xlsx'
# コピー元のエクセルファイルのパス
copy_source_path = dir_path + working_dir + excel_file_name
# コピー先のエクセルファイルのパス
copy_direct_path = dir_path + back_up_dir + excel_file_name

# 【実処理】
# バックアップファイルを更新する上書き保存処理
wb = xw.Book(copy_source_path)
wb.save(copy_direct_path)
wb.close()
print('Transaction completed.')
