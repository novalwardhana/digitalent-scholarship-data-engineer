# Fitur split
print(">>> Fitur .split()")
kalimat = "ani dan budi dan wati dan johan"
kalimatSplit1 = kalimat.split("dan")
print("kalimatSplit1: ", kalimatSplit1)
kalimatSplit2 = kalimat.split(" ")
print("kalimatSplit2: ", kalimatSplit2, "\n---------------\n")

# Fitur join
print(">>> Fitur .join()")
pemisah = " dan "
kalimatSplit = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(kalimatSplit)
print("kalimat: ", kalimat, "\n---------------\n")

# Fitur replace
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel", "jeruk")
print("kalimat: ", kalimat, "\n---------------\n")