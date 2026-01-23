# 9.90. Дано предложение. Все буквы е в нем заменить буквой и.

sentence = str(input("ввести предложение: "))

for _ in sentence:
    new_sentence = sentence.replace("е", "и")

print(new_sentence)