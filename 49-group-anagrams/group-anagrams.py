class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        comp_dict = {}
        for words in strs:
            sorted_word = ''.join(sorted(words))
            comp_dict[sorted_word] = comp_dict.get(sorted_word, [])
            comp_dict[sorted_word].append(words)
        final_dict = comp_dict.values()
        return final_dict