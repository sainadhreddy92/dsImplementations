from heapq import heappush,heappop,heapreplace,heapify,_heapify_max
class heapnode(object):
    def __init__(self,listindex,index):
        self.listindex = listindex
        self.index = index

class Solution(object):
    def mergeksortarrays(self,arrays):
        if not arrays:
            return []
        res =[]

        h = []
        for i in range(len(arrays)):
            if arrays[i]:
                heappush(h,(arrays[i][0],heapnode(i,0)))
        heapify(h)

        while  h:

            val,node = h[0]

            res.append(val)

            if node.index<len(arrays[node.listindex])-1:
                heapreplace(h,(arrays[node.listindex][node.index+1],heapnode(node.listindex,node.index+1)))
            else:
                heappop(h)

        return res
def main():
    sol = Solution()
    arrays = [[1,9,23],[],[2,4,7],[12,14,23]]
    print sol.mergeksortarrays(arrays)


if __name__=='__main__':
    main()
