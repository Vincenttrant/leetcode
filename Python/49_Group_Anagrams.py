class Solution(object):
    def groupAnagrams(self, strs):
        dictOutput = {}

        for word in strs:
            sWord = "".join(sorted(word))
            
            if sWord not in dictOutput:
                dictOutput[sWord] = [word]
            else:
                dictOutput[sWord].append(word)
        
        output = []
        for word in dictOutput.values():
            output.append(word)
        
        return output
