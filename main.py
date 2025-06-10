from stats import get_book_text, word_counter, char_counter, sorting_char
import sys

def main():
    if len(sys.argv) > 1:
        filePath = sys.argv[1]
        fullbook = get_book_text(filePath)
        count_word = word_counter(fullbook)
        char_count = char_counter(fullbook)
        sorted_char_count = sorting_char(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filePath}")
        print(f"----------- Word Count ----------")
        print(f"Found {count_word} total words")
        print("--------- Character Count -------")
        # print(sorted_char_count)

        for char in sorted_char_count:  
            # print(char["char"])

            if char["char"].isalpha():
                print(f'{char["char"]}: {char["num"]}')
        print('============= END ===============')
    else:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
main()