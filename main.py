import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import get_dict_list
from stats import get_top_words

def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_list = get_dict_list(chars_dict)
    top_words = get_top_words(text, 20)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Top 20 Words ----------")
    for entry in top_words:
        print(f"{entry['word']}: {entry['num']}")
    print("--------- Character Count -------")
    
    for entry in dict_list:
        if not entry["char"].isalpha():
            continue
        else:
            print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])

    