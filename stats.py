def get_num_words(book_content: str) -> None:
    word_count = len([word for word in book_content.split()])
    return word_count
    
def get_char_words(book_content: str) -> dict:
    ind_char_count = {}
    
    for word in book_content.split():
        for char in word.lower():
            if char not in ind_char_count:
                ind_char_count[char] = 1
            else:
                ind_char_count[char] += 1
                
    return ind_char_count

def dict_by_amount(dictionary: dict) -> dict:
    return sorted(dictionary.items(), reverse=True, key=lambda x: x[1])