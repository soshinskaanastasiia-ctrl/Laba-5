s = input("Введіть слова: ")
words = [] #створюєм порожній список
for part in s.split(','): #форматуєм від зайвих пробілів і ком
    word = part.strip()
    if word != '':
        words.append(word)
words.sort(key=str.lower, reverse=True) #сортуєм слова в зворотньому порядку
result = ' '.join(words) #об'єднання відсортованих слів і вивед ення результату
print(result)