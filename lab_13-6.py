
#Open the file and read it line by line
with open('alma_mater.txt', 'r') as file:
    for line in file:
        #Print each line with a blank line following it
        print(line.strip())
        print()  #This adds a blank line after each printed line
