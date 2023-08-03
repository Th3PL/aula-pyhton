def resto( n1, n2):
    rs1 = n1 // n2
    rs2 = n2 * rs1
    rs3 = n1 - n2
    return rs3

print("Digite 2 números inteiros")
num1 = int(input())
num2 = int(input())

resultado = resto(num1, num2)
print(f"Resto da divisão: {resultado}")