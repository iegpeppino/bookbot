import sys
from stats import get_num_words, get_num_chars

def get_book_text(path):
    with open(path) as f:
        book = f.read()
        return book

def main():
    if len(sys.argv) != 2:
        print( "Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    num_words = get_num_words(book)
    num_chars_dict = get_num_chars(book)
    # sorted_chars_dict = {key : value for key, value in sorted(num_chars_dict.items())}
    sorted_chars_list = sorted(num_chars_dict.items(), key= lambda kv: (kv[1], kv[0]), reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for duo in sorted_chars_list:
        if duo[0].isalpha():
            print(f"{duo[0]}: {duo[1]}")
    print("============= END ===============")
    return

if __name__ == "__main__":
    main()