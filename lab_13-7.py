
#Open the file and read all lines at once
with open('alma_mater.txt', 'r') as file:
    lines = file.readlines()

#Reverse the list of lines
lines.reverse()

for line in lines:
    print(line.strip())
    print()  
