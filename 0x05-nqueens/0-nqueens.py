#!/usr/bin/python3

"""Program that solves the N queens problem"""


import sys


"""Function prints board"""
def printBoard(board, num):
  array = []
  for i in range(num):
    for j in range(num):
      if j == board[i]:
        array.append([i, j])
  print(array)
  
  
"""Function determines the safe 
position for the queen"""
def validPosition(board, i, j, l):
    return board[i] in (j, j - i + l, i - l + j)
  
  
def positions(board, row, num):
  if row == num:
    printBoard(board, num)
      
  else: 
    for j in range(num):
      allowed = True
      for i in range(row):
        if validPosition(board, i, j, row):
          allowed = False
      if allowed:
        board[row] = j
        positions(board, row + 1, num)
        
        
def createBoard(length):
  return [0 * length for i in range(length)]


if len(sys.arg) != 2:
  print("Usage: nqueens N")
  sys.exit(1)
  
try:
  num = int(sys.argv[1])
except BaseException:
  print("N must be a number")
  sys.exit(1)
  
if (num < 4):
  print("N must be at least 4")
  sys.exti(1)
  

row = 0
board = createBoard(int(num))
positions(board, row, int(num))
