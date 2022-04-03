import os

file_names = os.listdir("lyrics")

for file in file_names:
    with open("lyrics/"+ file) as f:
        text = f.read()
        words = text.split()
        print(file, len(words) )