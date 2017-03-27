import sys
import unirest
def main():
  if len(sys.argv)!=2:
    sys.exit('Usage: sentiment_analysis.py <data-t0-test>')
 

  response = unirest.post("https://community-sentiment.p.mashape.com/text/",
  headers={
    "X-Mashape-Key": "d2CTlR6NIgmshT1YkzFPEBeNPFWKp1WRS2gjsnRs6YrzA23ihX",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "txt": sys.argv[1]
  }
)
  html = response.body
  print str(html['result']['sentiment'])+" at a confidence of "+ str(html['result']['confidence'])
if __name__=='__main__':
  main()



