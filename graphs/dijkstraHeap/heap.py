from globals import *
class heap():
  def __init__(self,capacity):
    self.heap_array = []
    self.size = 0
    self.capacity = capacity

  def getLeftchild(self,parent_index):
    return 2*parent_index + 1

  def getRightchild(self,parent_index):
    return 2*parent_index +2

  def getParentindex(self,child_index):
    return (child_index-1)/2

  def isleftchild(self,parent_index):
    return  self.getLeftchild(parent_index) < self.size

  def isrightchild(self,parent_index):
    return self.getRightchild(parent_index) < self.size 

  def isparent(self,index):
    return self.getParentindex(index) >=0

  def leftchild(self,parent_index):
    return self.heap_array[self.getLeftchild(parent_index)]

  def rightchild(self,parent_index):
    return self.heap_array[self.getRightchild(parent_index)]

  def parent(self,index):
    return self.heap_array[self.getParentindex(index)]

  def peek(self):
    if len(self.heap_array)>0:
      return self.heap_array[0]

  def delete(self,vertex):
    if len(self.heap_array)>0:
      item = self.heap_array[0]
      self.heap_array[0] = self.heap_array[self.size-1]
      self.heapifydown(vertex)
      self.size-=1
    return item

  def insert(self,element):
    self.heap_array.append(element)
    self.size+=1
    self.heapifyup()

  def swap(self,index1,index2):
    self.heap_array[index1],self.heap_array[index2] = self.heap_array[index2],self.heap_array[index1]

  def heapifyup(self):
    last_index = self.size-1
    while (self.isparent(last_index) and self.parent(last_index)<self.heap_array[last_index]):
      self.swap(self.getParentindex(last_index),last_index)
      last_index = self.getParentindex(last_index)


  def heapifydown(self,vertex):
    root_index = 0
    while self.isleftchild(root_index) and vertex[self.leftchild(root_index)].bandwidth > vertex[self.heap_array[root_index]].bandwidth:
      small_index = self.getLeftchild(root_index)
      if self.isrightchild(root_index) and vertex[self.leftchild(root_index)].bandwidth < vertex[self.rightchild(root_index)].bandwidth:
        small_index = self.getRightchild(root_index)
      self.heap_array[root_index],self.heap_array[small_index]=self.heap_array[small_index],self.heap_array[root_index]
      root_index = small_index


  def update(self,vertex,index):
    for i in range(globals().vertices):
      if self.heap_array[i]==index:
        break
    
    while i>0  and vertex[self.heap_array[self.parent(i)]].bandwidth < vertex[self.heap_array[i]].bandwidth:
      self.heap_array[i],self.heap_array[self.parent(i)] = self.heap_array[self.parent(i)],self.heap_array[i]
      i = self.parent(i)

def main():
  heap_test = heap()
  heap_test.insert(1)
  heap_test.insert(10)
  heap_test.insert(9)
  heap_test.insert(8)
  heap_test.insert(7)
  heap_test.insert(6)
  heap_test.insert(5)
  heap_test.insert(14)
  heap_test.insert(13)

  for _ in range(9):
    print heap_test.peek()
    heap_test.delete()

  #print heap_test.peek()
  #heap_test.insert(2)
  #print heap_test.peek()
  #heap_test.insert(3)
  #print heap_test.heap_array
  #print heap_test.peek()
  #heap_test.delete()
  #print heap_test.heap_array
  #print heap_test.peek()
  #heap_test.delete()
  #print heap_test.peek()
if __name__=='__main__':
  main()
