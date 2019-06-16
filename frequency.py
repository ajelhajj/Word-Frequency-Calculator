# Write a program that reads in the contents of a text file and displays
# a histogram of the frequency that words appear in the text.

def main():
    filename = input("Enter the filename: ") # Request filename from user
    infile = open(filename, 'r') # Open said file
    s = infile.read() # Read file

    punctuation = [',',';','.',':','!',"'","\""] # Create list containing punctuation
    for ch in punctuation:
        s = s.replace(ch,' ') # Remove all punctuation and replace with a space
    s = s.lower() # Force words to lowercase 
    s = s.split() # Split string into list containing char for each word

    print(s)

    dictionary = {} # Create empty dictionary to store unique words and their counts 

    for word in s:
        count = s.count(word) # Count frequency of word occurrence in string
        dictionary[word] = count # Add as a key with value to the dictionary

    print("Word" + "\t" + "Frequency") # Print header of table to console
    print("--------------") 

    for word in dictionary:
        asterisks = "*" * dictionary[word] # Print an asterisk equivalent to the frequency
        print(word + ": " + asterisks)

    infile.close() # Close the file

main()
