class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the distint letter in word and put in a dict
        word_dict = {}
        for letter in word:
            word_dict[letter] = word_dict.get(letter, 0) + 1
        
        # Pigeonhole principle
        if len(word_dict) <= 8:
            return len(word)

        # Sort the numbers in word_dict by frequency
        frequency_list = sorted((list(word_dict.values())), reverse = True)
            
        # Calculate the minimum number of pushes
        total_pushes = 0
        
        # Scalar for pushes
        helper_list = [1]*8 + [2]*8 + [3]*8 + [4]*2
        
        # Sum up the push number
        for i in range(len(frequency_list)):
            total_pushes += frequency_list[i] * helper_list[i]

        return total_pushes
            
            



            

