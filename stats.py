def get_book_text(file_path):
    file = ""
    with open(file_path) as book:
        file = book.read()
    return file

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    count = {}
    i = 0
    while i < len(book_text):
        if book_text[i].lower() in count:
            count[book_text[i].lower()] += 1
        else:
            count[book_text[i].lower()] = 1
        i += 1
    return count

def dic_sort(char_dictionary):
    dic_list = []
    for char, num in sorted(char_dictionary.items(), key=lambda char_dictionary: char_dictionary[1], reverse=True):
        dic_list.append({"char" : char, "num": num})
    return dic_list