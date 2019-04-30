import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
      
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
#        shift = 13  #establish cipher shift
        
        origKeys = []  #create original keys
        for lower in string.ascii_lowercase:
            origKeys.append(lower)
        for upper in string.ascii_uppercase:
            origKeys.append(upper)
        
        origVals = []  #cretae original values
        for i in range(0,26):  #assign a-z vaues 0-25
            origVals.append(i)
        for i in range(26, 52):  #assign A-Z values 52-77
            origVals.append(i+26)
                   
        origDict = dict(zip(origKeys, origVals))  #create the original dictionary  
        
        newDict = origDict.copy()  #create copy of origDict to create newDict
        for key, value in newDict.items():  #assign new values due to shift
            for newDict[key] in range(0,26):  #for a-z
                newDict[key] = value - shift              
                    
            for newDict[key] in range(26, 52):  #for A-Z
                newDict[key] = value - shift

        for key, value in newDict.items():  #correct order
            if newDict[key] < 0:  #of a-z
                newDict[key] += 26
            if 26 < newDict[key] < 52:  #of A-Z
                newDict[key] += 26
               
        shiftKeys = sorted(newDict, key=newDict.__getitem__)  #sort by value
        shiftDict = dict(zip(origKeys, shiftKeys))  #create the new dictionary
        
#        print("OrigDict is ", origDict, '\n')
#        print("newDict is ", newDict, '\n')
#        print("shiftDict is ", shiftDict, '\n')
        return shiftDict


    def apply_shift(self, shift):
        
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shiftMsg = []  #container for shifted message
        cipher = Message.build_shift_dict(self, shift)  #bring in cipher from build_shift_dict()
                
        for i in self.message_text:  #check each character in message
            if i in cipher.keys():  #if character upper or lower case letter
                shiftMsg.append(cipher[i])  #add matching code letter to output
            else:
                shiftMsg.append(i)  #if character punctuation or digit, add it to output
        
        shiftMsg = ''.join(shiftMsg)  #convert list to string of characters
        
        return shiftMsg  #return string
        
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text = text #Message.get_message_text
        self.valid_words = Message.get_valid_words
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
            
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
    
    
    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        encryptDictCopy = Message.build_shift_dict(self, self.shift).copy()
        return encryptDictCopy    
    
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted
    
    
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text  #text  #string, determined by input text
        self.valid_words = load_words(WORDLIST_FILENAME)  #list of all valid words
        
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        mostWords = 0  #track the shift giving the largest number of valid decrypted words
        bestShift = 0  #initialize bestShift at '0'
        
        for shift in range(0, 26):  #try all 26 possible shifts
            message = Message.apply_shift(self, shift)  #get the decrypted message for respective shift
            message = message.split(' ')  #convert message to a list of words
            
            for word in message:  #compare each word in message list to valid word list
                if word not in self.valid_words:
                    message.remove(word)  #remove invalid words from the message
                    
            if len(message) > mostWords:  #update shift if better than previous
                mostWords = len(message)
                bestShift = shift
            else:
                bestShift = bestShift  #if not better, do NOT update shift 
             
        message = Message.apply_shift(self, bestShift)  #use the bestShift to generate the most likely vaid message
        decryption = (bestShift, message)  #tuple, stores best shift and resulting message 
 
        return decryption

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())
