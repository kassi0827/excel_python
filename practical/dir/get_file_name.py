import os

# ターゲットフォルダのパス
path = '/Users/kashimataichi/play_python/excel_python/practical/dir/target'

# <<指定のフォルダ内のファイル名を取得する>>
file_list = os.listdir(path)
print(file_list)
print(file_list[0])
print(file_list[1])


# <<カレントディレクトリを表示するコード>>
print(os.getcwd())


# <<ターミナルのlsコマンド>>
os.system("ls")
