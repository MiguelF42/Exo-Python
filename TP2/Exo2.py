def decomment(file):
    output = ""
    with open(file, 'r') as f:
        for line in f.readlines():
            if line[0] == '#':
                continue
            print(line)
            output += line + '\n'
    new_file=file.split(".")[0]+"_decommented."+file.split(".")[1]
    with open(new_file, 'w') as f:
        f.write(output)


decomment("fich.txt")