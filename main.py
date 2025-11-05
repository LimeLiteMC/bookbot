import sys
from stats import get_num_words
from stats import get_book_text
from stats import char_count
from stats import dic_sort
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        print(sys.argv.count)
        sys.exit(1)
    print(sys.argv[1])
    book = get_book_text(sys.argv[1])
    data = char_count(book)
    sorted_data = dic_sort(data)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------\nFound {get_num_words(book)} total words")
    print("--------- Character Count -------")
    #print(dic_sort(data))
    for let_count in sorted_data:
        if let_count["char"].isalpha():
            print(f"{let_count["char"]}: {let_count["num"]}")
    print("============= END ===============")
main()
