#initialise class SentenceAnalyser
class SentenceAnalyser():
    def __init__(self):
        self.sentDict={}
    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.sentDict.get(key)) for key in self.sentDict])
#function to analyse sentences from decoded sequence.
    def analyse_sentences(self,decoded_sequence):
        self.sentDict = {'Question':[], 'Clause':[], 'Statement':[]}
#splits the sequence on every occurance of punctuation using re.        
        import re
        sentencess=re.split('(?<=[.,?]) +',decoded_sequence)
#To find the different sentences and put in dictionary.
        for x in sentencess:
            if x[-1:] == '?':
                self.sentDict['Question'].append(x)
                
            
                

            elif x[-1:] == '.':
                self.sentDict['Statement'].append(x)
                
                

            else:
                self.sentDict['Clause'].append(x)
#A dictionary is created to count the occerance of each type of sentence.
        new_dic = {}
        for key,value in self.sentDict.items():
            new_dic[key] = len([item for item in value if item])
        
#merging of both the dictionary to form new dictionary.       
        analysed_dict = { k: [ self.sentDict[k], new_dic[k] ] for k in self.sentDict }
        return analysed_dict

# Initialising class objects and invoking the function.         
message=input("Enter the decoded message: ")
task4=SentenceAnalyser()
result=task4.analyse_sentences(message)
print(result)
