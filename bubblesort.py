class solution(object):
  def bubble(self,arr):
    l = len(arr)
    if not arr:
      return arr
    for i in range(l):
      for j in range(l-i-1):
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def main():
  sol = solution()
  arr = [10,16,5,9,3,4]
  print sol.bubble(arr)


if __name__=='__main__':
  main()
