def word_counter(file_path, word_to_be_counted):
    with open(file_path) as f:
        data = f.readlines()
        counter = 0
        for row in data:
            for word in row.split():
                if word.lower() == word_to_be_counted:
                    counter += 1
    return counter