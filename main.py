def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_char(text):
    lowered_text = text.lower()
    char_dict = {}

    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_list(dict):
    listed_dicts = []
    for d in dict:
        listed_dicts.append({'name': d, 'num': dict[d]})
    listed_dicts.sort(reverse=True, key=sort_on)
    return listed_dicts

def get_book_path(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_path(book_path)

    report_list = dict_list(count_char(book_text))

    print(f'*** Begin report of {book_path} ***')
    print(f'{count_words(book_text)} words found in the document\n')

    for c in report_list:
        if c['name'].isalpha():
            print(f"The '{c['name']}' character was found {c['num']} times")
            
    print(f'*** End report ***')

main()
