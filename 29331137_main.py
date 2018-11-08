# Intialising class Decoder
class Decoder:
#creating morse code dictionary using constructor.    
    def __init__(self):        
        self.MORSE_CODE_DICT={'A':'01', 'B':'1000',
                       'C':'1010', 'D':'100', 'E':'0',
                       'F':'0010', 'G':'110', 'H':'0000',
                       'I':'00', 'J':'0111', 'K':'101',
                       'L':'0100', 'M':'11', 'N':'10',
                       'O':'111', 'P':'0110', 'Q':'1101',
                       'R':'010', 'S':'000', 'T':'1',
                       'U':'001', 'V':'0001', 'W':'011',
                       'X':'1001', 'Y':'1011', 'Z':'1100',
                       '1':'01111', '2':'00111', '3':'00011',
                       '4':'00001', '5':'00000', '6':'10000',
                       '7':'11000', '8':'11100', '9':'11110',
                       '0':'11111', ', ':'110011', '.':'010101',
                       '?':'001100'}
        print(self.MORSE_CODE_DICT)

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.MORSE_CODE_DICT.get(key)) for key in self.MORSE_CODE_DICT])

#function to decode the morse code sequence 
    def decode(self,morse_code_sequence):
        self.__str__()
        morsecharacters=""
# Getting the morse code sequence from the user.        
# checks if the first character is in binary.        
        if morse_code_sequence[0] == '1' or morse_code_sequence[0] == '0':
            for i in range(1,len(morse_code_sequence)):
# checks if the characters after the first characters are in binary.
                if morse_code_sequence[i] == '1' or morse_code_sequence[i] == '0' or morse_code_sequence[i]=='*':
                    morsecharacters += morse_code_sequence[i]
                    morsechar= morse_code_sequence.split('*')
            
                else:
                    print("This is an invalid input. It is not in binary form.")
                    choice = input("Do you want to continue? Press y for yes. Program terminates with any other character.")
                    if choice == 'Y' or choice == 'y':
                        return('Starts Again.')
                    else:
                        print("Program terminated.")
                        exit(0)
                        
                      
                    
        elif morse_code_sequence[0]!= '1' or morse_code_sequence[0]!= '0':
            print("This is an invalid input.Input not in binary form.")
            choice = input("Do you want to continue? Press y for yes. Program terminates with anyother character.")
            if choice == 'Y' or choice == 'y':
                return('Starts Again.')
            else:
                print("Program terminated.")
                exit(0)
                    

        

       
# decoding the input morse sequence.    
        morseToEnglish=[]                                                     
        alphabets=dict((value,key) for key, value in self.MORSE_CODE_DICT.items())  
        alphabets['']=' '
        alphabet_str=""
# checks if a sentence starts with a punctuation.
        if morsechar[0] == "001100" or morsechar[0] == "010101" or morsechar[0] == "110011":
            print("A sentence cannot start with punctuations and hence is invalid.")
            choice = input("Do you want to continue? Press y for yes. Program terminates with anyother character.")
            if choice == 'Y' or choice == 'y':
                return('Starts Again.')
            else:
                print("Program terminated.")
                exit(0)
            
# checks if a sentence ends with a punctuation or not.            
        if morsechar[-1] != "001100" and morsechar[-1] != "010101" and morsechar[-1] != "110011":
            print("Sentence has to end with a punctuation and hence is invalid.")
            choice = input("Do you want to continue? Press y for yes. Program terminates with anyother character.")
            if choice == 'Y' or choice == 'y':
                return('Starts Again.')
            else:
                print("Program terminated.")
                exit(0)

# checks if another sequence apart for the ones in dictionary are present else decode.       
        for i in range(len(morsechar)):
            if morsechar[i] in alphabets:
                morseToEnglish.append(alphabets[morsechar[i]])
                alphabet_str = ''.join(morseToEnglish)
            else:
                print(morsechar[i],"is invalid.Program terminated.")
                exit(0)
                
# Removing the space from the decoded sequence and seeing if consecutive punctuations are present.                    
            final_decoded_str = alphabet_str.replace('   ',' ')
        temp = final_decoded_str
        final_decoded_str=final_decoded_str.replace(" ","")
        punctuations= ".,?"

        for i in range(len(final_decoded_str)):
            for j in range(i+1,len(final_decoded_str)):
                if final_decoded_str[i] in punctuations and final_decoded_str[j] in punctuations:
                    print("No two punctuations can be together. Hence input is invalid.")
                    choice = input("Do you want to continue? Press y for yes. Program terminates with any other character.")
                    if choice == 'Y' or choice == 'y':
                        return('Starts Again.')
                    else:
                        print("Program terminated.")
                        exit(0)
                else:
                    i+=1
                    j+=1
                    

        
        
                    
        
        
        return(temp)

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

#initialise class SentenceAnalyser
class SentenceAnalyser():
    def __init__(self):
        self.sentDict={}
    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.sentDict.get(key)) for key in self.sentDict])

#function to analyse sentences from decoded sequence.
    def analyse_sentences(self,decoded_sequence):
        self.sentDict = {'Questions':[], 'Clauses':[], 'Statements':[]}
#splits the sequence on every occurance of punctuation using re.
        import re
        sentencess=re.split('(?<=[.,?]) +',decoded_sequence)
#To find the different sentences and put in dictionary.
        for x in sentencess:
            if x[-1:] == '?':
                self.sentDict['Questions'].append(x)
            elif x[-1:] == '.':
                self.sentDict['Statements'].append(x)
                

            else:
                self.sentDict['Clauses'].append(x)

#A dictionary is created to count the occerance of each type of sentence.            
        new_dic = {}
        for key,value in self.sentDict.items():
            new_dic[key] = len([item for item in value if item])
#merging of both the dictionary to form new dictionary.
        analysed_dict = { k: [ self.sentDict[k], new_dic[k] ] for k in self.sentDict }
        return analysed_dict

        



def main():
    while True:
        user_input = input("Hey there! Do you want to continue? : Y or N ")
        if user_input == 'Y' or user_input == 'y':
            task1=Decoder()
            message = input("Enter the message to be decoded: ")   
            result = task1.decode(message)
            print(result)
            while result == 'Starts Again.':
                message1 = input("Enter new message: ")   
                result = task1.decode(message1)
                print(result)
    
    
            count = 0
            while count < 3:
                choice = '0'
                while choice == '0':
                    print("Main Choice: Choose 1 of 4 choices")
                    print("Choose 1 for Letter Count")
                    print("Choose 2 for Word Count")
                    print("Choose 3 for Sentence Count")
                    print("Choose 4 for all")
       

                    choice = input ("Please make a choice: ")

        
                if choice == "1":
                    task2=CharacterAnalyser()
                    result2=task2.analyse_characters(result)
                    print("The number of occurances of letters are as follow: ", result2)
                    break
                elif choice == "2":
                    task3=WordAnalyser()
                    result3=task3.analyse_words(result)
                    print("The number of occurances of words are as follows: ",result3)
                    break

        
                elif choice == "3":
                    task4=SentenceAnalyser()
                    result4=task4.analyse_sentences(result)
                    print("The number of occurances of sentences and their types are as follows: ",result4)
                    break
       
                elif choice == "4":
                    task2=CharacterAnalyser()
                    result2=task2.analyse_characters(result)
                    print("The number occurances of letters are as follow: ", result2)
            


                    task3=WordAnalyser()
                    result3=task3.analyse_words(result)
                    print("The number of occurances of words are as follows: ",result3)

         

                    task4=SentenceAnalyser()
                    result4=task4.analyse_sentences(result)
                    print("The number of occurances of sentences and their types are as follows: ",result4)
                    break

        
                else:
                    print("I don't understand your choice.Try again. Program will be terminated after 3 chances.")
                    count +=1

            else:
                print("Invalid choice. Program terminated.")
                exit(0)


        else:
            break



    

if __name__ == '__main__':
    main()
   






