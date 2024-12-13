def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    list_of_chars = dict_to_arr(chars_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for i in range(len(list_of_chars)):
        char = list_of_chars[i]["name"]
        count = list_of_chars[i]["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    count = len(text.split())
    return count

def character_count(text):
    characters = {}
    lower_case = text.lower()
    for character in lower_case:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def dict_to_arr(dict):
    chars_arr = []
    for key,value in dict.items():
        chars_arr.append({"name": key, "num": value})
    return chars_arr

main()