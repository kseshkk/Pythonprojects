file_in = open("INPUT.txt", "r", encoding="utf-8")
file_out = open("OUTPUT.txt", "w", encoding="utf-8")
N = int(file_in.readline())

if N in [1, 2, 12]:
    file_out.write("Winter")
elif N in [3, 4, 5]:
    file_out.write("Spring")
elif N in [6, 7, 8]:
    file_out.write("Summer")
elif N in [9, 10, 11]:
    file_out.write("Autumn")
else:
    file_out.write("Error")

file_in.close()
file_out.close()
