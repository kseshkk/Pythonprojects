# 9.62. Дано предложение. Определить долю (в %) букв а в нем.

sentence = str(input("ввести предложение: "))
count_letters = 0

for letters in sentence:
    if letters == "а":
        count_letters += 1
print(count_letters)

result = count_letters / len(sentence) * 100
print(result)