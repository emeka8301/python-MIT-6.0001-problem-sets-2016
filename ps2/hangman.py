# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count=0 #count to keep track of letters that appear in both arguments
    
    for char in secret_word: #Iterate through the secret word
        for index in letters_guessed: #use each character to iterate through the guessed letters
            if char==index: 
                count+=1 
                break #add 1 to count if letters match
                
    if count==len(secret_word): #if count is equal to secret word length
        return True
    else:
        return False           






def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result=[] #create an empty list to store '_ '
    
    for i in range(len(secret_word)): #loop to store '_ ' equal to the secret word length
       result.append('_ ')
       
    result_index=[] #create an empty list to store index of matched guesses in secret word 

    for i in range(len(secret_word)): #loop to check for index of correct guesses in secret word
        for char in letters_guessed:
            if secret_word[i]==char:
                result_index.append(i)
                
               
    for i in result_index: #loop to replace correct guesses
       result[i]=secret_word[i]        
    
    return ''.join(result) #convert lit to string
    





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabets=string.ascii_lowercase
    alphabets_list=[]
    
    alphabets_list[:0]=alphabets
    
    for i in range(len(letters_guessed)): #loop to check for index of correct guesses in secret word
        for j in alphabets_list:
            if letters_guessed[i]==j:
                alphabets_list.remove(j)
               
 
    
    return ''.join(alphabets_list)
    
  
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    
    '''
    dash_line="--------------------------------"
    guesses=6
    warning=3
    letters_guessed=[]
    
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print(dash_line)
    
    while guesses>0:
        if secret_word==get_guessed_word(secret_word, letters_guessed):  #breaks the while loop if the user has guessed the secret word
            break
        
        print("You have", guesses, " guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))
        
        try: #makes sure the user doesnt enter a null value
            get_guess=input("Please guess a letter:")[0]
        
            if is_guess_alphabet(get_guess)==True: #Checks if input is an alphabet between A and Z
                
                if is_guess_in_list(get_guess, letters_guessed)==False: #checks if the user has guessed the letter
                    letters_guessed.append(get_guess)
                    
                    if is_guess_correct(secret_word, get_guess)==True: #checks if guess is correct
                        print("Correct guess!",get_guessed_word(secret_word, letters_guessed))
                        print(dash_line)
                        
                    elif (is_guess_correct(secret_word, get_guess)==False) & is_guess_vowel(get_guess): #check if guess is incorrect and if guess is a vowel
                        print("Oh no!, That is incorrect", get_guessed_word(secret_word, letters_guessed))
                        guesses-=2
                        print(dash_line)
                        
                    else: #check if guess is incorrect and if guess is a consonant
                        print("Oh no!, That is incorrect", get_guessed_word(secret_word, letters_guessed))
                        guesses-=1
                        print(dash_line)
                          
                elif (is_guess_in_list(get_guess, letters_guessed)==True)& (warning>0): # if the user has guessed the letter, removes a warning
                    warning-=1
                    print("Oops!, you have already used that Letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    
                    print(dash_line)
               
                else: #remove a guess if user has guessed the letter and run out of warnings
                    print("Oops!, you have already used that Letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    guesses-=1
                    print(dash_line)
                    
            elif (is_guess_alphabet(get_guess)==False)& (warning>0): #if input is not an alphabet and warning is not 0, tells the user
                warning-=1
                print("Oops!, That is not a valid letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                print(dash_line)
            
            else: #takes away a guess if you have run out of warnings
                print("Oops!, That is not a valid letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                guesses-=1
                print(dash_line)
            
        except (SyntaxError,IndexError):
            print("you did not enter a word")
            
    Total_score=guesses*unique_letters(secret_word)        
        
    if guesses==0:
        print("you ran out of guesses, you lose")
        print("The word is", secret_word)
        print("Your total score for this game is", Total_score)
   
    else:
        print("Congrats, you win!!!")
        print("Your total score for this game is", Total_score)
        
        
        
    # FILL IN YOUR CODE HERE AND DELETE "pass"

def unique_letters(secret_word): #returns number of unique letters in secret word
    s=set([])
    
    for char in secret_word:
        s.add(char)
    
    return len(s)




def is_guess_alphabet(get_guess): #checks if guess is alphabet
    
   return get_guess.lower().isalpha()

def is_guess_correct(secret_word,get_guess): #checks if guess is correct
    for char in secret_word:
        if get_guess==char:
         return True
    return False

def is_guess_in_list(get_guess, letters_guessed): #checks if users guess has already been guessed
    for char in letters_guessed:
        if char==get_guess:
            return True
    return False    

def is_guess_vowel(get_guess): #checks if guess is a vowel
    vowels="aeiou"     
    for char in vowels:
        if get_guess==char:
            return True
    return False




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word=my_word.replace(" ", "")
    
    if len(my_word)!=len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if (my_word[i]!=other_word[i])& (my_word[i]!="_"):
               return False
    return True   



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches=[]
    
    for word in wordlist:
        if (match_with_gaps(my_word, word))==True:
            matches.append(word)
    
    if len(matches)==0:
        return "No matches found"
    else:
        return " ".join(matches)



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    dash_line="--------------------------------"
    guesses=6
    warning=3
    letters_guessed=[]
    
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print(dash_line)
    
    while guesses>0:
        if secret_word==get_guessed_word(secret_word, letters_guessed):  #breaks the while loop if the user has guessed the secret word
            break
        
        print("You have", guesses, "guesses and", warning, "warnings left.")
        print("Available letters:",get_available_letters(letters_guessed))
        
        try: #makes sure the user doesnt enter a null value
            get_guess=input("Please guess a letter:")[0]
            
            if get_guess=="*":
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            else:
                if is_guess_alphabet(get_guess)==True: #Checks if input is an alphabet between A and Z
                    
                    if is_guess_in_list(get_guess, letters_guessed)==False: #checks if the user has guessed the letter
                        letters_guessed.append(get_guess)
                        
                        if is_guess_correct(secret_word, get_guess)==True: #checks if guess is correct
                            print("Correct guess!",get_guessed_word(secret_word, letters_guessed))
                            print(dash_line)
                            
                        elif (is_guess_correct(secret_word, get_guess)==False) & is_guess_vowel(get_guess): #check if guess is incorrect and if guess is a vowel
                            print("Oh no!, That is incorrect", get_guessed_word(secret_word, letters_guessed))
                            guesses-=2
                            print(dash_line)
                            
                        else: #check if guess is incorrect and if guess is a consonant
                            print("Oh no!, That is incorrect", get_guessed_word(secret_word, letters_guessed))
                            guesses-=1
                            print(dash_line)
                              
                    elif (is_guess_in_list(get_guess, letters_guessed)==True)& (warning>0): # if the user has guessed the letter, removes a warning
                        warning-=1
                        print("Oops!, you have already used that Letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                        
                        print(dash_line)
                   
                    else: #remove a guess if user has guessed the letter and run out of warnings
                        print("Oops!, you have already used that Letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                        guesses-=1
                        print(dash_line)
                        
                elif (is_guess_alphabet(get_guess)==False)& (warning>0): #if input is not an alphabet and warning is not 0, tells the user
                    warning-=1
                    print("Oops!, That is not a valid letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    
                    print(dash_line)
                
                else: #takes away a guess if you have run out of warnings
                    print("Oops!, That is not a valid letter. You have", warning, "warnings left:", get_guessed_word(secret_word, letters_guessed))
                    guesses-=1
                    print(dash_line)
            
        except (SyntaxError,IndexError):
            print("you did not enter a word")
            
    Total_score=guesses*unique_letters(secret_word)        
        
    if guesses==0:
        print("you ran out of guesses, you lose")
        print("The word is", secret_word)
        print("Your total score for this game is", Total_score)
   
    else:
        print("Congrats, you win!!!")
        print("Your total score for this game is", Total_score)
        
        
        


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
   #secret_word = choose_word(wordlist)
   
   #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
   secret_word = choose_word(wordlist)
   hangman_with_hints(secret_word)
