class solution():
  def validword(self,word,abbr):
    i=j=0
    while i<len(abbr) and j<len(word):
      num = 0
      while ord(abbr[i])>=48 and ord(abbr[i])<=57:
        num=(num*10)+ ord(abbr[i])-ord('0')
        i+=1
      j+=num
      if j>=len(word):
        return False
      if abbr[i]!=word[j]:
        return False

      i+=1
      j+=1

    return (i==len(abbr)) and (j==len(word))


def main():
  print solution().validword('apple','a2e')
 
if __name__=='__main__':
  main()   
