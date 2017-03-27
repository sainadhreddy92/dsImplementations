def flatten(lists):
  res = []
  helper(lists,res)

  return res



def helper(lists,res):
  for elem in lists:
    if isinstance(elem,int):
      res.append(elem)
    else:
      helper(elem,res)


def main():
  lists = [[1,1],2,[1,1]]
  print flatten(lists)


if __name__=='__main__':
  main()
