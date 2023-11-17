def maior_dos_tres(x:int,y:int,z:int): #NÃO precisa colocar o "int"
    if x > y and x > z:
        return f"O {x} é maior que o {y} e {z}."
    elif y > x and y > z:
        return f"O {y} é maior que o {x} e {z}."
    elif z > x and z > y:
        return f"O {z} é maior que o {x} e {y}."
    elif x == y and x > z:
        return f"O primeiro e segundo número são iguais ({x}) e são maiores que {z}."
    elif x == z and x > y:
        return f"O primeiro e terceiro número são iguais ({x}) e são maiores que {y}."
    elif y == z and y > x:
        return f"O segundo e terceiro número são iguais ({y}) e são maiores que {x}."
    else:
        return f"Os três números são iguais"
    
a = int(input("Digite um número inteiro: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

maior = maior_dos_tres(a,b,c)

print(maior)