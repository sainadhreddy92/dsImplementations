import re
class solution(object):
  def terparser(self,string):
    li = list(string)
    string = ''.join(li[::-1])
    while len(string)>1:
      string=re.sub(r'(.)\:(.)\?(.)',lambda m:m.group(2) if m.group(3)=='T' else m.group(1),string)
    return string


def main():
  sol = solution()
  s="T?T?F:5:3"
  print sol.terparser(s)


if __name__=='__main__':
  main()
