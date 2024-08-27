
CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = str(input("Digite seu nome: "))

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
valor_salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_recebido = float(input("Digite o valor do seu bônus: "))

# 4) Calcule o valor do bônus final

valor_final = CONSTANTE_BONUS + valor_salario * bonus_recebido

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus

print(f"Olá seja bem-vindo {nome_usuario}! \nO seu salário é {valor_salario} e o bônus recebido foi de {bonus_recebido}. \nPortanto, o seu valor final recebido será de {valor_final}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?