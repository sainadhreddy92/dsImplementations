import sys
def main():
  a,b,x,y = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
  while a!=x or b!=y:
    if a>x:
       a-=1
    else:
       if a!=x:
         a+=1

    if b>y:
       b-=1
    else:
       if b!=y:
         b+=1
  print a,b,x,y

if __name__=='__main__':
  main()
