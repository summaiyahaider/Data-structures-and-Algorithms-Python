class MinHeap:
  def __init__(self):
    self.heap = []

  def insert(self, val):
    self.heap.append(val)
    self.__prelocate_up(len(self.heap)-1)

  def get_min(self):
    if self.heap:
      return self.heap[0]
    return float('inf')

  def remove_min(self):
    if len(self.heap) > 1:
      tmp = self.heap[0]
      self.heap[0] = self.heap[-1]
      del self.heap[-1]
      self.__min_heapify(0)
      return tmp
    if len(self.heap) == 1:
      tmp = self.heap[0]
      del self.heap[0]
      return tmp
    return float('inf')
  
  def __prelocate_up(self, index):
    parent = (index - 1)//2
    if index <= 0:
      return
    if self.heap[parent] > self.heap[index]:
      self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
      self.__prelocate_up(parent)

  def __min_heapify(self, index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    smallest = index
    if (left < len(self.heap) and self.heap[left] < self.heap[smallest]):
      smallest = left
    if (right < len(self.heap) and self.heap[right] < self.heap[smallest]):
      smallest = right
    if smallest != index:
      tmp = self.heap[smallest]
      self.heap[smallest] = self.heap[index]
      self.heap[index] = tmp
      
      self.__min_heapify(smallest)

  def build_min_heap(self, arr):
    for e in arr:
      self.insert(e)


# testing
my_heap = MinHeap()
my_heap.build_min_heap([1,2,-3,22,-1,2,4,9])
print(my_heap.get_min())
my_heap.insert(-111)
print(my_heap.get_min())

      
