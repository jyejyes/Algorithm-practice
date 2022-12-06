def mininum_coin(total_price):
    coin_num=0;
    for coin in [500,100,50,10]:
        coin_num+=total_price//coin
        total_price-=((total_price//coin)*coin)
    return coin_num;
    
print(mininum_coin(int(input())))