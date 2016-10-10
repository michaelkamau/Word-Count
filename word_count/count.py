def words(str_words):
    import re
    pattern = re.compile(r'\s+')
    word_list = pattern.split(str_words)
    # Check for strings with ints, convert if necessary
    for i in range(len(word_list)):
        try:
            word_list[i] = int(word_list[i])
        except ValueError:
            continue

    word_count = {}
    for w in word_list:
        word_count.setdefault(w, 0)
        word_count[w] += 1
    return word_count
