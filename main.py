from stats import get_num_words
from stats import get_book_text
from stats import char_count
def main():
    book = get_book_text("./books/frankenstein.txt")
    print(f"Found {get_num_words(book)} total words")
    print(char_count(book))
main()
