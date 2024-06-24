st = "Python"
a_bytes = bytes(st, "ascii")
binary_converted = " ".join(["{0:b}".format(x) for x in a_bytes])
print("The Binary Represntation is:", binary_converted)


chaine = "Hello world"
unbit = bytes(chaine, "ascii")
conversion_en_binaire = " ".join(["{0:b}".format(x) for x in unbit])
print("On a donc: ", conversion_en_binaire)
print(type(conversion_en_binaire))
print(type(unbit))
print(unbit)
print(conversion_en_binaire)
binaire = 0b0101
print(type(binaire))
print(binaire)
print(bin(binaire))

caracters = "hello"
print(caracters)
one_bit = bytes(caracters, "ascii")
print(one_bit)
passage_binaire = "".join(["{0:b}".format(x) for x in one_bit])
print(passage_binaire)
en_binaire = int(passage_binaire, 2)
print(en_binaire)
print(bin(en_binaire))
un_binaire = 0b10110
print(bin(un_binaire ^ en_binaire))
