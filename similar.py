def is_similar_by_one_letter(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False
    if word1 == '#f':
        return False

    if len(word1) < len(word2):
        word1, word2 = word2, word1

    differences = 0
    index2 = 0

    for index1 in range(len(word1)):
        if index2 >= len(word2) or word1[index1] != word2[index2]:
            differences += 1
            if len(word1) == len(word2):
                index2 += 1
        else:
            index2 += 1

        if differences > 1:
            break

    return differences <= 1

def find_similar_word(input_word, word_list):
    similar_words = [word for word in word_list if is_similar_by_one_letter(input_word, word)]

    return similar_words
