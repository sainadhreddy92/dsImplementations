class solution(object):
  def sol(self,string1,string2):
    word_dict={}
    res =[]
    list1 = string1.split()
    list2 = string2.split()
    for item in list1:
      if item not in word_dict:
        word_dict[item]=1
    for item2 in list2:
      if item2 not in word_dict:
        word_dict[item2]=1
      else:
        word_dict[item2]+=1

    for key in word_dict:
      if word_dict[key]==1:
        res.append(key)
    return res

def main():
  s = solution()
  print s.sol("I Am Happy","I Am Old")
  

if __name__=='__main__':
  main()
