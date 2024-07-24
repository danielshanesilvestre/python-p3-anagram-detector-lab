# your code goes here!


class Anagram:

    def __init__(self, word):
        self.word = word


    def match(self, input):
        sorted_chars = sorted([char for char in self.word])
        result = []
        
        for word in input:
            if sorted_chars == sorted([char for char in word]):
                result.append(word)
        
        return result