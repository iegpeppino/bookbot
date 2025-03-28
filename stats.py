def get_num_words(document):
    document = str(document)
    count = 0
    for word in document.split():
        count += 1
    return count

def get_num_chars(document):
    char_dict = {}
    document = str(document).lower().split()
    for word in document:
        for char in word:
            if char not in char_dict.keys():
                char_dict[char] = 1
            else: 
                char_dict[char] +=1
    return char_dict