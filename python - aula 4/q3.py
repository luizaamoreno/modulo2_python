def valor_hora(salario, carga_horaria):
    return salario/(carga_horaria*4)

salario = float(input("Qual seu salário mensal? R$ "))
horas_semanais = int(input("Quantas horas você trabalha por semana? "))

print(f"O valor da hora trabalhada é {valor_hora(salario, horas_semanais)}.")