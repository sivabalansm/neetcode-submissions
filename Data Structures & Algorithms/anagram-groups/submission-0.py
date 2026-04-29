class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map =  dict()
        for s in strs:
            s_sort = ''.join(sorted(s))
            if s_sort in str_map:
                str_map[s_sort].append(s)
            else:
                str_map[s_sort] = [s]
        print(str_map.values())

        return list(str_map.values())
