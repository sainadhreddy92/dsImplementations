def nestedsum(nestedlist):
  su = 0
  if not nestedlist:
    return 0

  queue =[]

  for elem in nestedlist:
    queue.append(elem)

  depth =0
  while queue:
    depth+=1
    size = len(queue)
    for _ in range(size):
      li = queue.pop(0)
      if isinstance(li,int):
        su+=li*depth
      else:
        for subelem in li:
          queue.append(subelem)
  return su

def main():
  print nestedsum([[1,1],2,[1,1]])

if __name__=='__main__':
  main()
