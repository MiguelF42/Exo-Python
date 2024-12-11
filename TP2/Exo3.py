import os # Importation de la librairie os

def read_to_buffer(filename):
    with open(filename, 'r') as f:
        return f.read()

def read_to_words(filename):
    with open(filename, 'r') as f:
        return f.read().split()
    
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

def find_file_by_extension(extension, directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)
    return files

def display_files(directory):
    for file in os.listdir(directory):
        print(file)


print(read_to_buffer("C:\\Cours\\Python\\TP2\\fich.txt"))
print(read_to_words("C:\\Cours\\Python\\TP2\\fich.txt"))
rename_file("C:\\Cours\\Python\\TP2\\fich.txt", "C:\\Cours\\Python\\TP2\\fich2.txt")
print(find_file_by_extension(".txt", "C:\\Cours\\Python\\TP2"))
display_files("C:\\Cours\\Python\\TP2")