my_file = open("read_this.txt")
for line in my_file.readlines():
    print(line, end='')