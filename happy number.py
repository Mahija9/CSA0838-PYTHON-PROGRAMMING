class Solution:

def isHappy(self, n: int) -> bool:

s=set()

while n not in s:

s.add(n)

n=sum([int(i)**2 for i in str(n)])

if(n==1):

return True

return False
