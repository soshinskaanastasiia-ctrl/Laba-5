a, b = map(int, input("Введіть a і b: ").split()) #зчитуєм і перетворюєм на цілі числа
rows = [[i * j for j in range(b)] for i in range(a)] #створюєм список,де кожен елемент є добутком його індексів
print(rows) #виводим
