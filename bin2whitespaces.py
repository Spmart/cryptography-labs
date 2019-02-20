filename = input("Input filename:\n")
with open(filename, "rb") as f:
    text = f.read()
byte_chars = []
for char in text:
    byte_chars.append('{0:08b}'.format(char))
print(byte_chars)
cryptogram = []
for byte in byte_chars:
    cryptobyte = ""
    for bit in byte:
        if bit == "1":
            cryptobyte += " "
        else:
            cryptobyte += "\t"
    cryptogram.append(cryptobyte)
with open("out", "w") as f:
    for cryptobyte in cryptogram:
        f.writelines(cryptobyte + "\n")
print("Done!")
