file_in = open("INPUT.txt", "r")
file_out = open("OUTPUT.txt", "w")

line = file_in.readline().split()
t_room = int(line[0])
t_cond = int(line[1])

mode = file_in.readline().strip()
if mode == "freeze":
    temperature = min(t_cond, t_room)
elif mode == "heat":
    temperature = max(t_cond, t_room)
elif mode == "auto":
    temperature = t_cond
elif mode == "fan":
    temperature = t_room

file_out.write(str(temperature))

file_in.close()
file_out.close()