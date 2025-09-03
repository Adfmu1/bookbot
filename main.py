from stats import get_num_words

def get_book_text(filepath) -> str:
    with open(filepath) as book:
        return book.read()
    
def main():
    get_num_words(get_book_text("books/frankenstein.txt"))
    
main()