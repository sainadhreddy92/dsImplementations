import re

def reg(string):
  string=re.sub(r'//.*','',string)
  string=re.sub(r'/\*.*\*/','',string,flags=re.DOTALL)
  nf = open("newfile.py","w")
  nf.write(string)  
  nf.close()

def main():
  fp = open("sample.py","r")
  string = fp.read()
  reg(string)
  fp.close()

if __name__=='__main__':
  main()
