file = open("sample.txt", "w")
file.writelines(["Haloo\n", "Belajar Python\n", "Menyenangkan!\n"])
file.close()

file = open("sample.txt", "w")
file.writelines("Menulis ke dalam file\n")
file.writelines("Menggunakan Python\n")
file.close()

file = open("sample.txt", "r")
for item in file:
    print(item)