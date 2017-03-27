import sys

class solution(object):
  def shortest_word(self,words,word1,word2):
    if not word1 or not word2 or not words:
      return 0
    
    word_dict={}
    for index,word in enumerate(words):
      word_dict[word]=index
   
    diff = word_dict[word1]-word_dict[word2]
    if diff<0:
      return diff+len(words)
    else:
      return diff


def main():
  sol = solution()
  words=["practice","makes","perfect","coding","makes"]
  word1 = "makes"
  word2 = "coding"
  print sol.shortest_word(words,word1,word2)

if __name__=='__main__':
  main()  
