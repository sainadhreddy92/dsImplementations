def encode(string):
  if not string or len(string)<1:
    return ''

  char = string[0]
  count = 1
  res =  ''
  for i in range(1,len(string)):
    if string[i]==char:
      count+=1
    else:
      res+=char+str(count)
      count=1
      char = string[i]

  return res+char+str(count)


def main():
  print encode('wwwwaaabcccdd')

if __name__=='__main__':
  main()
