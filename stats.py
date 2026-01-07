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

def get_top_words(text, limit=20):
    words = text.split()
    word_counts = {}
    for word in words:
        cleaned = word.lower()
        cleaned = cleaned.strip('.,;:"!?()[]{}\'"-')
        if not cleaned:
            continue
        if cleaned in word_counts:
            word_counts[cleaned] += 1    
        else:
            word_counts[cleaned] = 1 
    word_list = []
    for w in word_counts:
        word_list.append({"word": w, "num": word_counts[w]})
    word_list.sort(key=sort_on, reverse=True)
    return word_list[:limit]
