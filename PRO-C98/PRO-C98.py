def swapfile():
    file1 = input("Enter file location[1]")
    file2 = input("Enter file location[2]")
    with open(file1, "r") as a:
        data_a = a.read()
    with open(file2, "r") as b:
        data_b = b.read()
    with open(file1, "w") as a:
        a.write(data_b)
    with open(file2, "w") as b:
        b.write(data_a)
    
    s1 = open(file1)
    x = s1.read()
    s2 = open(file2)
    y = s2.read()
    print(x, y)


swapfile()

