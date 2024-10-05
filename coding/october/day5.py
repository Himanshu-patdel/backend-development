from collections import Counter
lst=[3,2,4,2,2,223,4,5,4,4]
d={}
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
print(Counter(lst))
d2={}
for i in lst:
    if i not in d2:
        d2[i]=1
    else:
        d2[i]+=1
print(d2)


from typing import List

class Solution:
    def duplicates(self, arr: List[int]) -> List[int]:
        seen = set()
        duplicates = set()
        
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        return sorted(duplicates) if duplicates else [-1]


