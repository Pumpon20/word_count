def count_words(filename):
    word_count = {}

    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count

def main():
    filename = input("Введите имя файла для анализа: ")
    result = count_words(filename)

    print("Результаты подсчета слов:")
    for word, count in result.items():
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()
