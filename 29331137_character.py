class CharacterAnalyser():
#A constructor is defined.
    def __init__(self):                                                 
        self.charDict={}
    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.charDict.get(key)) for key in self.charDict])
#A function to get the occurance of letters.
    def analyse_characters(self,decoded_sequence):
#removing the punctuations from the decoded sequence.
        decoded_sequence = ''.join(e for e in decoded_sequence if e not in ('.',',','?'))  

       
        for n in decoded_sequence:
            keys = self.charDict.keys()
            if n in keys:
                self.charDict[n] += 1
            else:
                self.charDict[n] = 1
#returning the character dictionary with letter occurence.     
        return self.charDict


# Initialising class objects and invoking the function.        
message=input("Enter the message to be decoded: ")
task2=CharacterAnalyser()
result=task2.analyse_characters(message)
print(result)

        
