
    
       

# def char_counter():
#     with open("book/frankenstein.txt") as book:
#         contents = book.read()
#     for char in contents.lower():
#         print (char)

# char_counter()


def char_counter():
    with open("./book/frankenstein.txt") as book:
        contents = book.read()
    for char in contents.lower():
        print(char)

# Call the function
char_counter()
