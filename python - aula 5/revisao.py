def maior_dos_dois(x:int,y:int): #NÃO precisa colocar o "int"
    if x > y:
        return f"O {x} é maior que o {y}."
    elif y > x:
        return f"O {y} é maior que o {x}."
    else:
        return f"Os números são iguais"
    
print(maior_dos_dois(8,6))