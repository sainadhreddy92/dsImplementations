def nessum(nested_list,depth,su):

  for item in nested_list:
    if isinstance(item,int):
      su = su+ item*depth
    else:
      su= nessum(item,depth+1,su)
  return su
  

def main():
  print nessum([[1,1],2,[1,1]],1,0)

if __name__=='__main__':
  main()
