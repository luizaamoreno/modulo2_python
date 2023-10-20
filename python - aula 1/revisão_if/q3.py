sexo = str(input("""
Qual seu sexo? 
Responda com F ou M: 
""")).upper().strip() 

#função upper transforma toda a entrada recebida em maiúscula.
#função strip retira os espaços das bordas.

if sexo in 'fF':
    print("o sexo é feminino")
elif sexo in 'mM':
    print("o sexo é masculino")
else:
    print("entrada inválida. digite F ou M.")