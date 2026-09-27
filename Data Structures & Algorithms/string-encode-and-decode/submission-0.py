class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            The list of strings = sentence
            Each word has its own length

            1. create a results function
            2. loop through the sentence
            3. get the length of a string in the word
            4. seperate that length(int) with a character "#" or "!"
            5. add the length, the character, and the string to the results
        """

        result = []
        length = ""
        for i in strs:
            length = str(len(i)) + "#"
            result.append(length + i)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            char_index = s.find("#", index)
            length = int(s[index:char_index])
            word_start = char_index + 1
            word_end = word_start + length
            word = s[word_start:word_end]
            result.append(word)
            index = word_end
        return result



    
