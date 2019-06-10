#分解单词
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words.""" #单词分类
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""#弹出后打印第一个单词
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""#打印最后一个单词
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""#打印第一个单词和第二个单词
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""#整理后，打印第一个和第二个单词
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
