def main():
    book_path = "books/frankenstein.txt"
    
    def get_num_words(text):
        words = text.split()
        return len(words)

    def get_book_text(path):
        with open(path) as f:
            return f.read()
    
    def get_char_count(text):
        lowered_string = text.lower()
        char_list = list(lowered_string)
        char_dict = {}
        for char in char_list:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
        return char_dict

    def get_list(num_chars):
        char_list = list(num_chars.items())
        return char_list

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_char_count(text)
    char_list = get_list(num_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    
    char_list.sort(reverse=True, key=lambda x: x[1])
    
    for char, count in char_list: 
        print(f"The '{char}' character was found {count} times")
     
    print("--- End report ---")

main()
