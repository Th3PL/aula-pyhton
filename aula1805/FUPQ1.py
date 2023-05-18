def rest(n1, n2) :
    result = n1 % n2
    return result

print("Digite 2 números inteiros:")
num1 = float(input())
num2 = float(input())
resto = rest(num1, num2)

print(f'O resto da divisão é {resto}')

