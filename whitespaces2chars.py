filename = input("Input filename:\n")
with open(filename, "r") as f:
    cryptotext = f.readlines()
print(cryptotext)
byte_chars = []
for cryptobyte in cryptotext:
    byte = ""
    for bit in cryptobyte:
        if bit == " ":
            byte += "1"
        elif bit == "\t":
            byte += "0"
        else:
            pass
    byte_chars.append(byte)
print(byte_chars)
for byte in byte_chars:
    print(int(byte, 2))
