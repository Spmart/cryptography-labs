last_name = [204, 192, 208, 210, 219, 205, 215, 200, 202]
gamma = [31, 6, 13, 18, 15, 7, 4, 45, 21]

cryptogram = []
for i in range(len(last_name)):
    cryptogram.append(last_name[i] ^ gamma[i])
print(cryptogram)