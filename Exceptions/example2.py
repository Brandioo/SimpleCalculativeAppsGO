try:
    file = open("temp.txt")
    file.write("Ala has a cat")
except IOError:
    print("An error occurred while processing the file!")
finally:
    file.close()