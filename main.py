def get_book_text(file_path):
    file = ""
    with open(file_path) as book:
        file = book.read()
    return file

def main():
    book = get_book_text("./books/frankenstein.txt")
    print(book)

main()