def get_num_words(book_content: str) -> None:
    word_count = len([word for word in book_content.split()])
    print(f"{word_count} words found in the document")