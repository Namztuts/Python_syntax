#1 and #2
def print_upper_words(words):
    ''' For a list of words, print out each word uppercase
        and on a seperate line
    
        For example: print_upper_words(["hello","goodbye"])
        HELLO
        GOODBYE  
    '''
    for word in words:
        print(word.upper())
        
#3
def print_upper_words2(words):
    ''' For a list of words, print any word that starts with 'e'
        and turns it uppercase
    
        For example: print_upper_words(["ello","goodbye"])
        ELLO 
    '''
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

#4
def print_upper_words3 (words, start_with):
    ''' For a list of words, print any word that starts with
        a provided list of letters and turn it uppercase
    
        For example: print_upper_words3(["hello","goodbye"], ['h'])
        HELLO 
    '''
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
    
#Tests
# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words2(["ello", "ey", "goodbye", "yo", "yes"])
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],['h', 'g'])