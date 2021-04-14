def dict_join(x, y):
    xy = dict(zip(x, y))
    print(xy)


coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
dict_join(coin, code)
