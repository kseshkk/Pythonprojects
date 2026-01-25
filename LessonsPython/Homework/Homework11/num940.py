file_in = open("INPUT.txt", "r", encoding="utf-8")
file_out = open("OUTPUT.txt", "w", encoding="utf-8")
string = file_in.readline()

first_space = string.find(" ")

K = int(string[0:first_space]) - 1
S = string[first_space:].strip()

result = S[0:K] + S[K + 1:]

file_out.write(result)
file_in.close()
file_out.close()