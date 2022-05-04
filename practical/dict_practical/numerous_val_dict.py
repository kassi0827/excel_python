# 地所型に複数の値は以下で可能
stock_dict = {
    'VT': (95, 97),
    'VTI': (250, 252),
    'VEA': (43, 45),
    'VWO': (65, 69),
}

# 複数のvalを持つ辞書型は以下のコードで出力可能
for stock_ticker in stock_dict:
    print(stock_ticker + '最初の値は、', stock_dict[stock_ticker][0])
    print(stock_ticker + '最後の値は、', stock_dict[stock_ticker][1])
