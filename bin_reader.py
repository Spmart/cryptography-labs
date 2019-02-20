filename = input("Input filename:\n")
with open(filename, "rb") as f:
    text = f.read()
for char in text:
    print('{0:08b}'.format(char))
