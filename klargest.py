class Solution(object):
    def maxheapify(self,index,size,arr):
        left = 2*index+1
        right = 2*index+2

        max_index = index

        if left<size and arr[left]<arr[max_index]:
            max_index = left
        if right<size and arr[right]<arr[max_index]:
            max_index = right

        if max_index!=index:
            arr[index],arr[max_index]=arr[max_index],arr[index]
            self.maxheapify(max_index,size,arr)


    def buildheap(self,arr,size):
        i = size/2 -1
        while i>=0:
            self.maxheapify(i,size,arr)
            i-=1


    def extractkmax(self,k,arr):
        res = []
        if not arr or len(arr)<k:
            return res
        heap_size = len(arr)-1
        self.buildheap(arr,len(arr))
        while len(res)!=k:
            res.append(arr[0])
            arr[0],arr[heap_size]=arr[heap_size],arr[0]
            heap_size-=1
            self.maxheapify(0,heap_size,arr)
        return res

def main():
    arr = [50,65,34,4,3,67,89,73,43]
    sol = Solution()
    print sol.extractkmax(len(arr),arr)

if __name__=='__main__':
    main()
