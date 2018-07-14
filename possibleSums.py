def possibleSums(coins, quantity):
    sums = {0:0}
    length = len(quantity)
    for i in range(length):
        for quant in range(quantity[i]):
            temp_list = []
            for key in sums:
                # print(coins[i])
                temp_list.append(key+coins[i])
            sums.update(dict.fromkeys(temp_list, 0))
    print(sums)
    return len(sums.keys())-1

print(possibleSums([1, 2],[5, 2]))