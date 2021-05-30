# Step 1: Decrypt data ke dalam list dictionary
fileHargaRumah = open("sample.txt", "r")
dataHargaRumah = fileHargaRumah.readlines()
fileHargaRumah.close()

keyHargaRumah = dataHargaRumah[0].replace("\n","").split(",")
hargaRumah = []

for baris in dataHargaRumah[1:]:
    barisHargaRumah = baris.replace("\n","").split(",")
    dictHargaRumah = dict()
    for i in range(len(barisHargaRumah)):
        dictHargaRumah[keyHargaRumah[i]] = barisHargaRumah[i]
    hargaRumah.append(dictHargaRumah)
print("Harga Rumah:", hargaRumah, "\n------------------\n")

# Step 2: Membuat fungsi get all atributes
def getAllSpecifiedAttributes(listOfDictionary, specifiedKey):
    listAttributes = []
    for data in listOfDictionary:
        attribute = data[specifiedKey]
        listAttributes.append(attribute)
    return listAttributes

# Step 3: Membuat fungsi untuk mencari minimum dan maximum value
def minValue(listAttributes):
    minAttribute = 9999
    for attr in listAttributes:
        if int(attr) < minAttribute:
            minAttribute = int(attr)
    return minAttribute

def maxValue(listAttributes):
    maxAttribute = -9999
    for attr in listAttributes:
        if int(attr) > maxAttribute:
            maxAttribute = int(attr)
    return maxAttribute

# Step 4: Transform attribute
def transformAttribute(attr, maxAttr, minAttr):
    nilaiTransformasi = (attr - minAttr) / (maxAttr - minAttr)
    return nilaiTransformasi

# Step 5: Data transform
def dataTransformation(listOfDictionary, listOfAttributeNames):
    attrInfo = {}
    for attrName in listOfAttributeNames:
        specifiedAttributes = getAllSpecifiedAttributes(listOfDictionary, attrName)
        maxAttr = maxValue(specifiedAttributes)
        minAttr = minValue(specifiedAttributes)
        attrInfo[attrName] = {'max': maxAttr, 'min': minAttr}
        dataIdx = 0
        while (dataIdx < len(listOfDictionary)):
            listOfDictionary[dataIdx][attrName] = transformAttribute(int(listOfDictionary[dataIdx][attrName]), maxAttr, minAttr)
            dataIdx += 1
    return listOfDictionary, attrInfo

# Step 6: 
def transformData(data, attrInfo):
    for keyName in attrInfo:
        data[keyName] = (data[keyName] - attrInfo[keyName]['min']) / (attrInfo[keyName]['max'] - attrInfo[keyName]['min'])
    return data

# Step 7:
def absValue(value):
    if value < 0:
        return -value
    else:
        return value

def princeBasedOnSimilarity(data, listOfData):
    prediksiHarga = 0
    perbedaanTerkecil = 999
    for dataPoint in listOfData:
        perbedaan = absValue(data['tanah'] - dataPoint['tanah'])
        perbedaan += absValue(data['bangunan'] - dataPoint['bangunan'])
        perbedaan += absValue(data['jarak_ke_pusat'] - dataPoint['jarak_ke_pusat'])
        if perbedaan < perbedaanTerkecil:
            prediksiHarga = dataPoint['harga']
            perbedaanTerkecil = perbedaan
    return prediksiHarga

# Step 8
hargaRumah, attrInfo = dataTransformation(hargaRumah, ['tanah', 'bangunan', 'jarak_ke_pusat'])
data = {'tanah': 110, 'bangunan': 80, 'jarak_ke_pusat': 35}

data = transformData(data, attrInfo)
harga  = princeBasedOnSimilarity(data, hargaRumah)
print("Prediksi harga rumah", harga)