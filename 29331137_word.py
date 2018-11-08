#initialising class WordAnalyser
class WordAnalyser():
#building a constructor
    def __init__(self):
        self.wordDict={}
    def __str__(self):
        str=""
        return ', '.join(['{key}={value}'.format(key=key, value=self.wordDict.get(key)) for key in self.wordDict])

#function to get occurence of words
    def analyse_words(self,decoded_sequence):
#removing the punctuations from decoded sequence.        
        decoded_sequence = ''.join(e for e in decoded_sequence if e not in ('.',',','?'))
        wordss = decoded_sequence.split()
        for w in wordss:
            self.wordDict[w] = self.wordDict.get(w,0)+1
            self.wordDict.items()
#returning the word dictionary.            
        return self.wordDict        

message=input("Enter the message to be decoded: ")

#initialising class objects  
task3=WordAnalyser() #constructor will be initialised.
result=task3.analyse_words(message)
print(result)

