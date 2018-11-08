# Intialising class Decoder
class Decoder:
    def __init__(self):
# creating morse code dictionary        
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
# function to decode the morse code sequence 
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

# Initialising class objects and invoking the function.
task1=Decoder()
message = input("Enter the message to be decoded: ")
result = task1.decode(message)
print(result)
while result == 'Starts Again.':
    message1 = input("Enter new message: ")   
    result = task1.decode(message1)
    print(result)
    

