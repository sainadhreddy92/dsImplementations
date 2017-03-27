class stackrev(object):
  def revstack(self,stack):
    if stack:
      top = stack.pop()
      self.revstack(stack)
      self.helper(stack,top)

  def helper(self,stack,top):
    if not stack or top>stack[-1]:
      stack.append(top)

    else:
      elem = stack.pop()
      self.helper(stack,top)
      stack.append(elem)


def main():
  stack =[]
  stack.append(8)
  stack.append(22)
  stack.append(0)
  stack.append(14)
  print stack
  stackrev().revstack(stack)
  print stack


if __name__=='__main__':
  main()
