def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    char_times = dict()
    for char in text:
        lowered = char.lower()
        if lowered in char_times:
             char_times[lowered] += 1
        else:
            char_times[lowered] = 1
    return char_times

def sort_on(d):
    return d["num"]

def get_dict_list(char_times):
    dict_list = []
    for ch in char_times:
        ch_dicts = {"char": ch, "num": char_times[ch]}
        dict_list.append(ch_dicts)
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list


