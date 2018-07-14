coins = [10, 6, 1]


def makeChange(money):
    cache = [0]*(money+1)
    for i in range(1, money+1):
        min_coins = float('inf')
        for coin in coins:
            if(i - coin >= 0):
                curr_coins = cache[i-coin]+1
                if(curr_coins < min_coins):
                    min_coins = curr_coins
        cache[i] = min_coins
        print cache
    return cache[money]
print makeChange(10)
