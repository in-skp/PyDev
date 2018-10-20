fam = ["santosh", 32, "kavita", 28, "kashinath", 61, "prema", 56]

print(fam)
print(fam[-1])
print(fam[2:4])
print(fam[:4])
print(fam[4:])

fam[7] = 55
fam[0:2] = ["santomax", 31]
fam = fam + ["new", 0]


fam2 = fam
print(fam2)
fam2[0] = "santooo"
print(fam2)
print(fam)
