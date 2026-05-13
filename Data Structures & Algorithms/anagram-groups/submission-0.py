class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for s in strs:
            if str(sorted(s)) not in result_dict:
                result_dict[str(sorted(s))] = [s]
            else:
                result_dict[str(sorted(s))].append(s)
        return list(result_dict.values())