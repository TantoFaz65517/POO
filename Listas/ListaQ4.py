fr = input("Digite uma frase:")
x = fr[fr.rindex(' ') + 1:].rstrip()
print(x)