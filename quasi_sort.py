#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def arrange(arr):
  """
  Arranges list so that negative number come first, then all zeroes, then all positive numbers. Array does not have to be sorted in the end
  """
  _, offsetPos = find_offset(arr)
  offsetNeg = 0
  index = 0
  stopPos = offsetPos
  while index < stopPos:
    if (arr[index] < 0):
      arr[index], arr[offsetNeg] = arr[offsetNeg], arr[index]
      index += 1
      offsetNeg +=1
    elif arr[index] > 0:
      arr[index], arr[offsetPos] = arr[offsetPos], arr[index]
      offsetPos += 1
    else:
      index += 1
  return arr

def find_offset(arr):
  """
  Calculate where in the resulting array, zeroes and positive numbers, respectively, should start 
  """
  offsetZer = 0
  offsetPos = 0
  for elem in arr:
    if elem < 0:
      offsetPos += 1
      offsetZer += 1
    if elem == 0:
      offsetPos += 1
  return (offsetZer, offsetPos)

if __name__ == "__main__":
  """
  Example use
  """
  arr = [-1, 3, -3, 0, 1, 0]
  print("Pre-sorting: ", arr)
  result = arrange(arr)
  print("Post arranging:", result)
  print(find_offset(arr))
  arr = [-4, 13, 10, -13, -13, 3, 7, 17, -16, -4, -8, 9, 2, 0, -9, -2, -12, -17, -19, -19]
  print("Pre-sorting: ", arr)
  result = arrange(arr)
  print("Post arranging:", result)
  print(find_offset(arr))
