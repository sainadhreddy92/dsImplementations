class Solution(object):
    def replacespaces(self,string):
        if not string or len(string)<1:
            return string

        spaces = 0
        for char in string:
            if char==' ':
                spaces+=1
        length= len(string)+ spaces*2

        newstring = ['']*length

        i = length-1
        j = len(string)-1
        while i>=0 and j>=0:
            if string[j]!=' ':
                newstring[i]=string[j]
                i-=1
                j-=1
            else:
                newstring[i]='0'
                i-=1
                newstring[i]='2'
                i-=1
                newstring[i]='%'
                i-=1
                j-=1
        return ''.join(newstring)

def main():
    sol = Solution()
    string1 = None
    print sol.replacespaces(string1)
    print sol.replacespaces('a b c')
    print sol.replacespaces('abc')
    print sol.replacespaces(' ')

if __name__=='__main__':
    main()
