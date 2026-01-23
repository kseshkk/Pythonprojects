# 9.15. Дано слово. Вывести на экран его k-й символ.

word = str(input("введите слово: "))
symbol = int(input("введите номер символа: "))
result = word[symbol - 1]
print(result)