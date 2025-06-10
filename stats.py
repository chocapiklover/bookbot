def get_book_text(filePath):
    with open(filePath) as book:
        contents = book.read()
        return(contents)

#alternatively could have been acheived with len(word)
def word_counter(contents):
    count = 0
    words = contents.split()
    for word in words:
        count += 1
    return count


def char_counter(contents):
    dict = {}
    lowercase = contents.lower()
    for char in lowercase:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict


def sorting_value(list_of_chars):
    # print(list_of_chars["num"])
    return list_of_chars["num"]


def sorting_char(dict):
    
    list_of_chars = []
    for char in dict:
        new_double_dict = {}
        new_double_dict["char"] = char
        new_double_dict["num"] = dict[char]
    
        list_of_chars.append(new_double_dict)


    list_of_chars.sort(reverse=True, key=sorting_value )

    return list_of_chars



    
    

    