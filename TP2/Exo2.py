def decomment(file): # This function reads a file and writes it to a new file without comments
    output = ""
    with open(file, 'r') as f:
        for line in f.readlines(): # Read the file line by line
            if line[0] == '#': # If the line starts with a comment, skip it
                continue
            print(line)
            output += line + '\n' # Add the line to the output
    new_file=file.split(".")[0]+"_decommented."+file.split(".")[1] # Create a new file name
    with open(new_file, 'w') as f: # Write the output to the new file
        f.write(output)

decomment("fich.txt")