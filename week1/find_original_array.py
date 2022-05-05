class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        hashmap = Counter(changed)

        original_array = []
        if len(changed)%2!=0: return  []
        for i in changed:
            if(hashmap[i]>0):
                hashmap[i]  -=1
                if(hashmap[i*2] >0):
                    original_array.append(i)
                    hashmap[i*2]  -=1
        if len(changed)/2== len(original_array): return original_array
        return []