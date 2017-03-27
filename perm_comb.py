import sys


class Solution():
  
  def perm(self,string):
    char_dict = {}
    odd = 0
    for char in string:
      if char in char_dict:
        char_dict[char]+=1
      else:
        char_dict[char]=1
    for key  in char_dict:
      if char_dict[key]%2!=0:
        odd+=1
    
    if len(string)%2==0:
      if not odd:
        return True
      else:
        return False

    else:
      if odd==1:
        return True
      else:
        return False




def main():
  sol = Solution()
  print sol.perm("code")
  print sol.perm("aab")
  print sol.perm("carerac")


if __name__=='__main__':
  main()
    
     
    

