import sys


class ValidWordAbbrev:
  dict_unique = {}
  def __init__(self,word_dict):
      self.word_dict= word_dict
      for each in word_dict:
         self.dict_unique[each] = self.CalcAbbrev(each)

  def CalcAbbrev(self,word):
    if len(word)>2:
      return word[0]+str(len(word[1:-1]))+word[-1]
    else:
      return word

  def isUnique(self,word):
    print self.dict_unique
    if word not in self.dict_unique:
      for each in self.dict_unique:
        if self.dict_unique[each]==self.CalcAbbrev(word):
          return False
      return True
    else:
      return False


def main():
  word_dict=[ "deer", "door", "cake", "card" ]
  vw = ValidWordAbbrev(word_dict)
  print vw.isUnique(sys.argv[1])


if __name__=='__main__':
  main()	
