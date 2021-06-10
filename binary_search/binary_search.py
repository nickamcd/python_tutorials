import random
import time

def naive_search(l, target):
  for i in range(len(l)):
    if l[i] == target:
      return i
  return -1

def binary_search(l, target, low=None, high=None):
  if low is None:
    low = 0
  if high is None:
    high = len(l) - 1

  # not found
  if high < low:
    return -1
  
  mid = (low + high) // 2

  if l[mid] == target:
    return mid
  elif target < l[mid]:
    return binary_search(l, target, low, mid - 1)
  else:
    return binary_search(l, target, mid + 1, high)

if __name__ =='__main__':
  length = 100000
  print("starting...")

  sorted_list = set()
  while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
  sorted_list = sorted(list(sorted_list))

  # try searching for each item as target
  start = time.time()
  for target in sorted_list:
    naive_search(sorted_list, target)
  end = time.time()
  print("naive search time: ", (end - start)/length, "seconds")

  start = time.time()
  for target in sorted_list:
    binary_search(sorted_list, target)
  end = time.time()
  print("binary search time: ", (end - start)/length, "seconds")