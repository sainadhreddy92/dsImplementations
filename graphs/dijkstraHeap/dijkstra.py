def dijkstra(weight,source):
  included = {}
  not_included ={}

  for i in range(len(weight)):
    if i!=source:
      not_included[i]=2**31-1
    else:
      not_included[i]=0

  cur_weight = 0
  while not_included:
    for j in range(len(weight)):
      if weight[source][j]!=0 and j not in included and cur_weight+weight[source][j] < not_included[j]:
        not_included[j]=cur_weight+weight[source][j]

    included[source] = not_included[source] 
    del not_included[source]

    if not_included:
      for key in sorted(not_included,key=not_included.get):
        source = key
        cur_weight = not_included[key]
        break

  for key in included:
    print key,included[key]



def main():
  weight = [[0,4,0,0,0,0,0,8,0],[4,0,8,0,0,0,0,11,0],[0,8,0,7,0,4,0,0,2],[0,0,7,0,9,14,0,0,0],[0,0,0,9,0,0,10,0,0,0],[0,0,4,14,10,0,2,0,0],[0,0,0,0,0,2,0,1,6],[8,11,0,0,0,0,1,0,7],[0,0,2,0,0,0,6,7,0]]
  dijkstra(weight,0)
  #for line in weight:
    #print line




if __name__=='__main__':
  main()
