a = int(input("insira o valor 1:"))
b = int(input("insira o valor 2:"))

def maior(x, y):
    if x > y:
        return x
    else:
        return y
    
print("O maior o valor é", maior(a, b))