numbers = input("Введіть числа: ").split() #зчитуєм як список цілих чисел
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
count=0
for i in range(1, len(numbers) - 1): #проходим по списку і виключаєм перший і останній елементи
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:  #перевіряєм чи поточний елемент більший за правого і лівого
        count = count + 1
print("Кількість елементів, більших за сусідів:", count)