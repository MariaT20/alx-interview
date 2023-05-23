#!/usr/bin/python3

"""determining the fewest number of coins needed 
to meet a given amount total"""

def makeChange(coins, total):
 if total <= 0
    return 0

  coinValue = 0
  usedCoin = 0
  currentTotal = total
  sortedCoin = sorted(coins, reverse=True)
  coinLength = len(coins)
  
  while currentTotal > 0:
    if usedCoin >= coinLength:
      return -1
    if currentTotal - sortedCoin[usedCoin] >= 0:
      currentTotal = currentTotal - sortedCoin[usedCoin]
      coinValue = coinValue + 1
    else:
      usedCoin = usedCoin + 1
  return coinValue
