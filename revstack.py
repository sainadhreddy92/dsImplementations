def revstack(stack):
  if not stack:
    return stack

  elem=stack.pop()
  stack = revstack(stack)
  stack= bottompush(stack,elem)
  return stack


def bottompush(stack,elem):
  if not stack:
    stack.append(elem)
  else:
    elem2=stack.pop()
    stack=bottompush(stack,elem2)
    stack.append(elem)
  return stack
    


def main():
  stack = [3,5,56,8,9]
  print revstack(stack)


if __name__=='__main__':
  main()
