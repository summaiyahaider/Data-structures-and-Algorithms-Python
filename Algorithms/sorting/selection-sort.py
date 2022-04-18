'''
Algorithm:
1) select a min element and put it at its place
2) repeat step 1 for n elements (n = length of array)

Time Complexity:
worst-case: O(n**2)
average-case: O(n**2)
best-case: O(n**2)

Space Complexity:
O(1)
'''

def selection_sort(lst):
  for i in range(len(lst)):
    min_idx = i
    for j in range(i+1, len(lst)):
      if lst[j] < lst[min_idx]:
        min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]
