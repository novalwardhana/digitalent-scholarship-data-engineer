# Membaca file dengan fungsi readlines()
print(">>> Membaca file dengan fungsi readlines()")
file = open("sample.txt", "r")
allLines = file.readlines()
file.close()
print(allLines, "\n---------------\n")

# Membaca file dengan looping
print(">>> Membaca file dengan looping")
file = open("sample.txt", "r")
for line in file:
    print(line)
file.close()