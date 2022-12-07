def mininum_coin(total_price):
    coin_num=0;
    for coin in [500,100,50,10]:
        coin_num+=total_price//coin
        total_price%=coin # 더 간단한 방법으로 변경
    return coin_num;
    
print(mininum_coin(int(input())))