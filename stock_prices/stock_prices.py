#!/usr/bin/python

import argparse
# find index of largest, value past index[0], work backwords to see if value is max profit
# if that value is sutracted from rest of values and is > answer solved, 
# if not, stop at that index and work back from that one


# O(n)
def find_max_profit(prices):
  largest_num_i = 1
  largest_num = 0
  max_diff = 0

  # find largest value index
  for num in prices[1:len(prices) - 1]:
      if num > largest_num:
          largest_num = num
          largest_num_i = prices.index(num)

  # find max difference  
  for num in prices[0:largest_num_i]:
        if prices[largest_num_i] - num > max_diff:
            max_diff = prices[largest_num_i] - num
        elif prices[largest_num_i] - num < 0:
            max_diff = prices[largest_num_i] - num        
  
  return max_diff  


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


  # ([10, 7, 5, 8, 11, 9]), 6)
  # ([100, 90, 80, 50, 20, 10]), -10)
  # ([1050, 270, 1540, 3800, 2]), 3530)
  # ([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)


print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))   
