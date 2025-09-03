import sys

from stats import get_num_words, get_char_words, dict_by_amount

def get_book_text(filepath) -> str:
    with open(filepath) as book:
        return book.read()
    
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book_content = get_book_text(filepath)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book_content)} total words")
        print("--------- Character Count -------")
        chars = dict_by_amount(get_char_words(book_content))
        for key, value in chars:
            print(key+": "+str(value))
        print("============= END ===============")
    

main()