class solution(object):
  def group_shifted(self,strings):
    strings.sort()
    keys_dict ={}
    for string in strings:
      key = ''
      for i in range(1,len(string)):
        key+=chr(ord('a')+(ord(string[i])-ord(string[i-1])+26)%26)
      if key in keys_dict:
        keys_dict[key].append(string)
      else:
        keys_dict[key]=[string]
    return keys_dict.values()


def main():
  sol = solution()
  strings =["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
  print sol.group_shifted(strings)


if __name__=='__main__':
  main()

