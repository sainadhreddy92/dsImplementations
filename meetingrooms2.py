class Meeting():
  def __init__(self,start,end):
    self.start = start
    self.end = end


class solution():
  def meetingpoints(self,meetings):
    if len(meetings)<2:
      return True

    meetings.sort(key=lambda x:x.start)
   
    for meeting in meetings:
      print meeting.start
 
    for i in range(1,len(meetings)):
      if meetings[i].start<meetings[i-1].end:
        return False

    return True



  def compare(self,meeting1,meeting2):
    if meeting1.start>meeting2.start:
      return 1
    elif meeting1.start<meeting2.start:
      return -1
    else:
      return 0


def main():
  meetings=[Meeting(5,10),Meeting(0,30),Meeting(15,20)]
  print solution().meetingpoints(meetings)


if __name__=='__main__':
  main()
