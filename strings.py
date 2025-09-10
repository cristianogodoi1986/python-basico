# Exemplos de manipulação de strings projeto Cristiano

nome = "Lucas Abre"
sobrenome = "Silva"

# Concatenação
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo)

# F-strings
idade = 15
print(f"{nome_completo} tem {idade} anos.")

# Operações com strings em Python
print("Maiúsculas:", nome_completo.upper())
print("Minúsculas:", nome_completo.lower())
print("Quantidade de caracteres:", len(nome_completo))
