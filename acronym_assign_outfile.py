# Acronym converter to text file
# this program will create an acronym, joining the first letters of each word and capitalizing them, then save the data to a text file
# Justin Middagh
# Hilbert College CS131
# October 17,2020

# defines the program called acronym_converter
def acronym_converter():
    # set a string input to a variable for use in the program
    initial_words = str(input('Please enter words or a phrase that will be converted to an Acronym:'))
    # takes the previous string input, grabs the first letter of each word and capitializes it
    acronym_converted = '.'.join(initial_words[0] for initial_words in initial_words.upper().split())
    # creates a file called "output.txt" with the option to append further text to the file
    outfile = open('output.txt', 'a')
    # prints, or saves the initial_words input along with the newly created acronym to the new text file
    print('The words you chose were:', initial_words, '\n''Your Acronym is:', acronym_converted, file=outfile)
    # closes the text file
    outfile.close()
    # prints the first letter of each word (capitalized) to the screen
    print('Your newly minted Acronym is:', acronym_converted)


acronym_converter()
