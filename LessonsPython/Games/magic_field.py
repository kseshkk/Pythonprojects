question = ""
guess_word = ""
user_word = ""

question = input("введите вопрос-подсказку для загаданного слова: ")
guess_word = input("введите правильное слово: ")

user_word = "*" * len(guess_word)

print("\n" * 50)
game_step = 0

game_is_running = True
while game_is_running == True:

    game_step += 1

    print()
    print("-----------------")
    print()

    print(f"Вопрос:  {question}")
    print(f"Отгаданное слово:  {user_word}")

    letter = input("Введите предполагаемую букву в слове: ")

    if guess_word.find(letter) == -1:
        print("Такой буквы не существует")
    else:
        print("Вы угадали!")
        temp = ""
        for i in range(len(guess_word)):
            if guess_word[i] == letter:
                temp += guess_word[i]
            else:
                temp += user_word[i]
        user_word = temp 

        if user_word.find("*") == -1:
            game_is_running = False

print(f"Отгаданное слово:  {user_word}")
print("Вы угадали!")