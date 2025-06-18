import sys
from stats import *

def main():
    
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print("Found",get_num_words(text), 'total words')
        print("--------- Character Count -------")
        sorted_list = rip_apart_book(text)
        for i in sorted_list:
            print(f"{i["letter"]}: {i["count"]}")
    

    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()