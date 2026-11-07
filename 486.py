a,b,c=map(int, input("Введіть a b c через пробіл: ").split()) #зчитуєм 3 цілих числа
array=[[[0 for k in range(c)] for j in range(b)] for i in range(a)] #cтворюєм тривимірний масив і виводим його
print(array)
