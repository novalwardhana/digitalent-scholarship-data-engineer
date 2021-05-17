# menulis ke file dengan mode write
print(">>> Menulis file dengan mode append")
file = open("sample.txt", "w")
file.write("Sekarang saya belajar python\n")
file.write("Dengan mode w (write) \n")
file.close()

file = open("sample.txt", "r")
for line in file:
    print(line)
file.close()