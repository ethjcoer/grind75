class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

#        if len(ransomNote) > len(magazine):
#            return False
#
#        letters = Counter(magazine)
#        newNote = ""
#
#        for i in ransomNote:
#
#            if letters.get(i, 0) > 0:
#                letters[i] = letters[i] - 1
#                newNote = newNote + i
#
#        return newNote == ransomNote

        letters = Counter(magazine)

        for i in ransomNote:

            if i not in letters:
                return False
            elif letters[i] == 1:
                del letters[i]
            else:
                letters[i] -= 1

        return True
