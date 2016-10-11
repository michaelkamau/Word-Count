def words(str_words):
    # split on spaces
    word_list = []
    if ' ' in str_words:
        # remove spaces if found
        word_list = [i for i in str_words.split() if i]
    elif '\n' in str_words:
        word_list = str_words.split('\n')
    elif '\t' in str_words:
        word_list = str_words.split('\t')
    else:
        return {str_words : 1}

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
