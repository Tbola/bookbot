def get_num_words(book_text):
    words=book_text.split()
    return len(words)

def count_characters(book_text):
    my_dict={}
    wordz = book_text.split()
    for word in wordz:
        for i in word:
            my_lc=i.lower()
            if my_lc in my_dict:
                my_dict[my_lc]+=1
            else:
                my_dict[my_lc]=1

    return my_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dict_in):
    my_list=[]
    for d in dict_in:
        my_list.append({"letter":d, "count":dict_in[d]})
    my_list.sort(reverse=True, key=sort_on)
    return my_list

def rip_apart_book(book_text):
    return sort_dict(count_characters(book_text))