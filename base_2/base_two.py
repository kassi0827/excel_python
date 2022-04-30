import openpyxl
import pprint as ppr

# この実行ファイルのパス
cur_path = "/Users/kashimataichi/play_python/excel_python/base_2/"
excel_path = cur_path + "Book2.xlsx"

wb = openpyxl.load_workbook(excel_path)

# ワークブック変数をfor文で処理するとシート名一覧を取得できる
for sheet in wb:
    print(sheet.title)

# シート.rowsをfor文でループ処理するとデータが入力されている範囲を１行ずつ読み込めます。
# cell.coordinateでセルのアドレスを出力することができる
target_sheet = wb['Sheet1']
addrs = []
for row in target_sheet.rows:
    for cell in row:
        addrs.append(cell.coordinate)
        print(",".join(addrs))

print('###############################')
print(addrs)
