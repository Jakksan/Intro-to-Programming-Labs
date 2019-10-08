# Read each file
infile = open("input_file.txt")
text_array = []

# read the first line
line = infile.readline()

# Add each line of the text file to text_array
while line:

    # remove newline
    line = line.rstrip('\n')

    # append the line to text_array
    text_array.append(line)

    # read the next line
    line = infile.readline()


# Look at each segment of text in the text array, and figure out what to do with it
for text in text_array:
    # print(text) # debugging

    # Make the string into an array of smaller strings
    text = text.split()

    # Replace underscores with spaces
    for i in range(len(text)):
        if "_" in text[i]:
            text[i] = text[i].replace("_", " ")

    print(text)
