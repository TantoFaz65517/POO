a = int(input("insira o valor 1:"))
b = int(input("insira o valor 2:"))
c = int(input("insira o valor 3:"))

def maior(x, y, z):
    return max(x, y, z)

print("o maior valor é ", maior(a, b , c))