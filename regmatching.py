import re
def isRegMatched(reg_string,match_string):
  if '$' in reg_string:
    regex_formed = r'.*%s' %reg_string 
  elif '^' in reg_string:
    regex_formed = r'%s.*' %reg_string
  else:
    regex_formed = r'.*%s.*' %reg_string

  print regex_formed
  matched = re.match(regex_formed,match_string)

  if matched:
    return True
  return False



def main():
  print isRegMatched('alt','coaltar')



if __name__=='__main__':
  main()
