def get_book_text(filepath) -> str:
    with open(filepath) as book:
        return book.read()
    
def main():
    print(get_book_text("books/frankenstein.txt"))
    
main()