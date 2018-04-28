
def all_words(word):
    if len(word) == 1:
        return word
    else:
        set1 = set(all_words(word[1:]))
        #print(set1)
        set2 = set()
        initial = word[0]
        
        for x in set1:
            for y in range(len(x)+1):
                set2.add(x[:y] + initial + x[y:])
        return set2


def main():
    word = input("Input word: ")
    print(len(all_words(word)))
    print(all_words(word))

if __name__ == "__main__":
    main()

