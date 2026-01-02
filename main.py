from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(sys.argv)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    num_words=count_words(text)
    letters=count_letters(text)
    res=sort_dict(letters)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in res:
        print(f"{i['char']}: {i['num']}")

    

main() 
    