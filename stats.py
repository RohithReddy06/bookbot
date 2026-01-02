import string

def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_counts={}
    cleaned_text = ''.join(char.lower() for char in text if char in string.ascii_letters)
    for char in cleaned_text:
        letter_counts[char]=letter_counts.get(char, 0) + 1
    return letter_counts
    
def sort_dict(dict):
    result = [{"char": ch, "num": num} for ch, num in dict.items() if ch.isalpha()]
    def get_num(d):
        return d["num"]
    
    result.sort(key=get_num, reverse=True)
    return result
