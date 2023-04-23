byte = []
zeros: int = 0
uns: int = 0

for i in range(1, 9):
   num = input(f"Digite o {i}º bit (0 ou 1):")
   byte.append(num)

for bit in byte:
    if bit == '0':
        zeros += 1
    else:
        uns += 1

print(f"O aquantidade de bit's 0 é: {zeros} e a quantidade de bit's 1 é: {uns}")