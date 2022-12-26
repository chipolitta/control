# 14

def isSublist(larger, smaller):
   for i in range(0, len(larger)):
       if larger[i:i+len(smaller)] == smaller:
           return True
   return False

print(isSublist([1,2,3,4],[1,2,3]))









