class sol(object):
  def prin(a,b):
    print "a+b"



class sol2(sol):
  def prin2():
    sol.prin(2,3) 


def main():
  s1 = sol()
  s2 = sol2()
  s1.prin(2,3)

if __name__=='__main__':
  main() 
