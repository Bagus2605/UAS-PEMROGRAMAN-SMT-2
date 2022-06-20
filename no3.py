data = []

while True:
    inputUser = input("masukkan angka: ")
    if inputUser == "n":
        break
    data.append(int(inputUser))

jumlah = sum(data)
mean = jumlah/len(data)
print(mean)
