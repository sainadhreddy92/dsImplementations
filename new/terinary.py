class Solution(object):
  def terparser(self,expression):
    if not expression or len(expression)==0:
      return None

    i=len(expression)-1
    stack=[]
   
    while i>=0:
      char = expression[i]
      
      if stack and stack[-1]=='?':
        stack.pop()
        first = stack.pop()
        stack.pop()
        second = stack.pop()

        if char=='T':
          stack.append(first)
        else:
          stack.append(second)      
      else:
         stack.append(char)


      i-=1

    return stack[-1]

def main():
  sol = Solution()
  expression = 'T?T?F:5:3'
  print sol.terparser(expression)


if __name__=='__main__':
  main()
