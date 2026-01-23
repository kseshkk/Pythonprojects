symbol_as_str = input("ввести символ: ")
symbol = symbol_as_str[0]

if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
    print("это английская буква")

    if symbol >= "a" and symbol <= "z":
        print("строчная")
    else:
        print("заглавная")

elif symbol >= "0" and symbol <= "9":
    print("это цифра")

else:
    print("неизвестный символ")