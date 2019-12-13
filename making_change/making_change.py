#!/usr/bin/python

import sys
total_ways = 0


def making_change(amount, denominations):
    global total_ways

    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 1:
        return 1

    return making_change(amount-denominations[-1], denominations) + making_change(amount, denominations[:-1])            

making_change(10, denominations = [1, 5, 10, 25, 50])

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")

    # self.assertEqual(making_change(0, self.denominations), 1)
    # self.assertEqual(making_change(1, self.denominations), 1)
    # self.assertEqual(making_change(5, self.denominations), 2)
    # self.assertEqual(making_change(10, self.denominations), 4)
    # self.assertEqual(making_change(20, self.denominations), 9)
    # self.assertEqual(making_change(30, self.denominations), 18)
    # self.assertEqual(making_change(100, self.denominations), 292)
    # self.assertEqual(making_change(200, self.denominations), 2435)
    # self.assertEqual(making_change(300, self.denominations), 9590)    