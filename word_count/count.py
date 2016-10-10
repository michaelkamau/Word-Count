def words(str_words):
    word_list = str_words.split(' ')
    word_count = {}
    for w in word_list:
        word_count.setdefault(w, 0)
        word_count[w] += 1
    return word_count
