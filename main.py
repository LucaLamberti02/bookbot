def read_file():
    with open("books/frankenstein.txt") as file:
        c = file.read()
        return c

def get_read(text):
    char_counts = {}
    text = text.lower()
    for cha in text:
        if cha.isalpha():
            if cha in char_counts:
                char_counts[cha] += 1
            else:
                char_counts[cha] = 1
    return char_counts

def count_words(content):
    words = content.split()
    return len(words)

content = read_file()
char_counts = get_read(content)
word_count = count_words(content)
print(f"--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document")
print("\nCharacter counts:")
for char, count in char_counts.items():
    print(f"The '{char}' character was found {count} times")
print("--- End report ---")