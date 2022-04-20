class MaxHeap:
  def __init__(self):
    self.heap = []

  def insert(self, val):
    self.heap.append(val)
    self.__prelocate_up(len(self.heap) - 1)

  def get_max(self):
    if self.heap:
      return self.heap[0]
    return float('-inf')
  
  def remove_max(self):
    if len(self.heap) > 1:
      max = self.heap[0]
      self.heap[0] = self.heap[-1]
      del self.heap[-1]
      self.__max_heapify(0)
      return max
    if len(self.heap) == 1:
      max = self.heap[0]
      del self.heap[0]
      return max
    return float('-inf')
  
  def __prelocate_up(self, index):
    parent = (index-1)//2
    if index <= 0:
      return
    if self.heap[parent] < self.heap[index]:
      tmp = self.heap[parent]
      self.heap[parent] = self.heap[index]
      self.heap[index] = tmp
      self.__prelocate_up(parent)

  def __max_heapify(self, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    largest = index
    if (left < len(self.heap) and self.heap[largest] < self.heap[left]):
      largest = left
    if (right < len(self.heap) and self.heap[largest] < self.heap[right]):
      largest = right
    if largest != index:
      tmp = self.heap[largest]
      self.heap[largest] = self.heap[index]
      self.heap[index] = tmp
      self.__max_heapify(largest)

  def build_max_heap(self, arr):
    for e in arr:
      self.insert(e)

# testing
my_heap = MaxHeap()
my_heap.build_max_heap([1,2,3,4,5,77])
my_heap.remove_max()
print(my_heap.get_max())
my_heap.insert(123)
print(my_heap.get_max())


    