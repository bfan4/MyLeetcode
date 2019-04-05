class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # mapp = {}
        # for w in sorted(strs):
        #     key = tuple(sorted(w))
        #     mapp[key] = mapp.get(key, []) + [w]
        # ans =  mapp.values()
        # return ans
                
    
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
            
        
        