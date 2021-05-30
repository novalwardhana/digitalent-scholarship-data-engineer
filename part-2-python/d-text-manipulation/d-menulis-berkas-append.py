# Menulis dengan mode append
print(">>> Menulis dengan mode append")
file = open("sample.txt", "a")
file.writelines([
    "sekarang kita belajar pengolahan data dengan python\n",
    "Dengan library math\n"
])
file.close()

file = open("sample.txt", "r")
for line in file:
    print(line)
file.close()