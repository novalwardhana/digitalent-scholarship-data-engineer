# Fitur find
print(">>> Fitur .find()")
teks = "Jeruk malang adalah jeruk termanis dibanding jeruk-jeruk lainnya"
print("teks: ", teks)
print("Teks find Apel: ", teks.find("Apel"))
print("Teks find adalah: ", teks.find("adalah"))
print("Teks find mangga: ", teks.find("Mangga"))
print("Teks find malang: ", teks.find("malang"), "\n---------------\n")

# Fitur count
print(">>> Fitur .count()")
teks = "Jambu malang adalah jambu termanis dibanding jambu-jambu lainnya"
kemunculanKataJambu = teks.count("Jambu")
kemunculanKataAdalah = teks.count("adalah")
kemunculanKataManggis = teks.count("manggis")
kemunculanKataMalang = teks.count("malang")
print("Kemunculan kata Jambu: ", kemunculanKataJambu)
print("Kemunculan kata adalah: ", kemunculanKataAdalah)
print("Kemunculan kata manggis: ", kemunculanKataManggis)
print("Kemunculan kata malang: ", kemunculanKataMalang, "\n---------------\n")
