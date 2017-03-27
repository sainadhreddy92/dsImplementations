def finddepth(nestedlist):
  depth = 0
  if not isinstance(nestedlist,int):
    for item in nestedlist:
      depth = max(depth,finddepth(item))
    return depth+1
  return depth


def main():
  nestedlist = [[1,2],[1]]
  print finddepth(nestedlist)

if __name__=='__main__':
  main()
