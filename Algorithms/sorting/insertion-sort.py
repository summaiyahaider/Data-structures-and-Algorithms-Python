
'''
Algorithm:
1) pick an element which is in wrong order
2) insert it in the right position

Time Complexity:
worst-case: O(n**2)
average-case: O(n**2)
best-case: O(n)

Space Complexity:
O(1)
'''

def insertion_sort(lst):
  for i in range(len(lst)-1):
    if lst[i+1] < lst[i]:
      elem = lst.pop(i+1) 
      for j in range(i+1):
        if (elem > lst[j]):
          continue
        else: break
      lst.insert(j, elem)