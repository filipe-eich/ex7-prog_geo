"""
Programa: prog_geo
Descrição: Este programa calcula uma progressão geométrica à escolha do usuário
Autor: Filipe Eich
Data: 25/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

n=""
razao=""
nesimo=""
termo=""
soma=""


#Entrada de dados

termo = float(input("\nOlá! Vamos calcular uma progressão geométrica? Comece digitando o primeiro termo da P.G.: "))
razao = float(input("\nAgora, diga a razão: "))

n = float(input("\nPor fim, defina o valor de n para calcularmos qual será o n-ésimo termo: "))


# Processamento de dados

nesimo=termo*(razao**(n-1))
soma= termo*(((razao**n)-1)/(razao-1))

#Saida de dados

print(f"\nAqui está o valor do n-ésimo termo: {nesimo}")
print(f"\nAqui está o valor da soma da P.G.: {soma}")
