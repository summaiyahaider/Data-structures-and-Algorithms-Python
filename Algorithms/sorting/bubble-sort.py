'''
Algorithm:
1) swap adjacent elements if they are in wrong order
2) repeat step 1 n times for each element (n = length_of_list)

Time Complexity:
worst-case: O(n**2)
average-case: O(n**2)
best-case: O(n**2)

Space Complexity:
O(1)
'''

def bubble_sort(lst):
  for i in range(len(lst)):
    for j in range(len(lst)-1-i):
     if lst[j] > lst[j+1]:
        lst[j],lst[j+1] = lst[j+1],lst[j]



