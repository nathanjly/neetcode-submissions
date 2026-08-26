class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        new_list = []
        for s in strs:
            sorted_word = "".join(sorted(s))
            new_list.append(sorted_word)
        anagrams_indexes = {}
        for i, s in enumerate(new_list):
            if s not in anagrams_indexes:
                anagrams_indexes[s] = [i]
            else:
                anagrams_indexes[s].append(i)

        # Go through dict, assign each index in the lists to original words
        for a in anagrams_indexes:
            one_anagram = []
            for i in range(len(anagrams_indexes[a])):
                index_original = anagrams_indexes[a][i]
                one_anagram.append(strs[index_original])
            output.append(one_anagram)
                
        return output
        
