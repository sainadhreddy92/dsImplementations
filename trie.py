class trienode(object):
  def __init__(self):
    self.map = {}
    self.isCompleteword = False

class solution(object):
  def addName(self,rootNode,word):
    for i in range(len(word)):
      if word[i] in rootNode.map:
        if i==len(word)-1:
          rootNode.isCompleteword = True
        rootNode = rootNode.map[word[i]]
      else:
        newnode = trienode()
        rootNode.map[word[i]]= newnode
        if i==len(word)-1:
          rootNode.isCompleteword = True
        rootNode = newnode

  def findword(self,rootNode,prefix):
    for i in range(len(prefix)):
      if prefix[i] in rootNode.map:
        if i == len(prefix)-1 and rootNode.isCompleteword==True:
          return True
        rootNode = rootNode.map[prefix[i]]
      else:
        return False
    return False

  def getallwords(self,rootNode,prefix):
    res = []
    rootnode2 = rootNode 
    rootNode = self.isprefix(rootNode,prefix)
    if not rootNode:
      return []
    else:
      res.extend(self.helper(rootNode,prefix,[]))
    
    if self.findword(rootnode2,prefix):
      res=[prefix]+res
    return res
      

  def helper(self,rootNode,prefix,res):
    if not rootNode:
      return res
    for letter in rootNode.map:
      if rootNode.isCompleteword==True:
        res=self.helper(rootNode.map[letter],prefix+letter,res+[prefix+letter])  
      else:
        res=self.helper(rootNode.map[letter],prefix+letter,res)
    return res


  def isprefix(self,rootNode,prefix):
    for char in prefix:
      if char not in rootNode.map:
      	return None
      rootNode = rootNode.map[char]
    return rootNode


def main():
  li = ["hack","hackerrank","abc","abcd","abcde","abcdef","abcdefg"]
  rootNode = trienode()
  sol = solution()
  for element in li:
    sol.addName(rootNode,element)
  #print sol.findword(rootNode,"hack")
  #print sol.findword(rootNode,"hackerrank")
  #print sol.findword(rootNode,"abc")
  #print sol.findword(rootNode,"abcd")
  #print sol.findword(rootNode,"bdjcbejbjfb")
  print sol.getallwords(rootNode,"")
if __name__=='__main__':
  main()
