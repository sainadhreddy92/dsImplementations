class Solution(object):
    def lexicalOrder(self, n):
        res = []
        for i in range(1,n+1):
            res.append(i)
        
        res= sorted(res,cmp=self.helper)
        return res
        
    def helper(self,x,y):
        l1 = list(str(x))
        l2 = list(str(y))
        
        maxlen = max(len(l1),len(l2))
        l1 = map(int,l1)
        l2 = map(int,l2)
        
        for i in range(maxlen):
            num1 = l1[i] if i<len(l1) else 0
            num2 = l2[i] if i<len(l2) else 0
            
            if num1<num2:
                return -1
            elif num1>num2:
                return 1
        return 0



def main():
    sol = Solution()
    print sol.lexicalOrder(5656)

if __name__=='__main__':
    main()
