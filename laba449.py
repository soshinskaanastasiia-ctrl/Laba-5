numbers = input("Введіть числа: ").split() #зчитуєм і розбиваєм його на список окремих слів
for i in range(len(numbers)):
    numbers[i] = int(numbers[i]) #перетворюєм на цілі числа
result = [] #створюєм порожній список
for x in numbers:
    if numbers.count(x) == 1: #якшо елемент зустрічається 1 раз додаєм його до списку результатів
        result.append(x)
print(result) #виводим