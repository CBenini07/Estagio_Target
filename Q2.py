# Escreva um programa que verifique, em uma string, a existência da 
#       letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada 
#   de sua preferência ou pode ser previamente definida no código;

txt = "quero ser contratado! :) S2"

# Converte a string para minúsculas para simplificar a contagem de 'a' e 'A'
quantidade_a = txt.lower().count('a')

if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
else:
    print("A letra 'a' não está presente na string.")