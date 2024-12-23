# 1) Solicite ao usuario que digite o nome

constante_bonus = 1000

nome_usuario = input("Digite seu nome: ")

# 2) Solicite ao usuario que digite o valor do seu salario
# Converta a entrada para numero de ponto flutuante

salario = float(input("Informe seu salario: "))


# 3) Solicite ao usuario que digite o valor do bonus recebido
# Converta a entrada para numero de ponto flutuante

bonus = float(input("Informe seu bonus: "))


# 4) Calcule o valor do bonus final

resultado = constante_bonus+ salario * bonus

# 5) Imprima calculo do KPI para o usuario

print(resultado)

# 6) Imprima  a mensagem personalizada incluindo o nome de usuario, salario e bonus

print(f"O usuario: {nome_usuario} possui o bonus de: {resultado}")