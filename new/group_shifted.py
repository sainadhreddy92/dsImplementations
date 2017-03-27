class Solution(object):
  def groupShifted(self,strings):
    res = []
    word_dict={}

    if not strings:
      return res
    strings.sort()
    for string in strings:
      key = ''
      for i in range(len(string)-1):
        key+=str((ord(string[i])-ord(string[i+1])+26)%26)
      if key in word_dict:
        word_dict[key].append(string)
      else:
        word_dict[key]=[string]

    for key in word_dict:
      res.append(word_dict[key])

    return res

def main():
  sol = Solution()

  strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

  print sol.groupShifted(strings)

if __name__=='__main__':
  main()
