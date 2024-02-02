"""

"""
taula=[[0]*15 for i in range(5)]

for i in range(5):
    for j in range(15):
        if i == 0 or i == 4 or j == 0 or j == 14:
            taula[i][j]=1

for fila in taula:
    for elemento in fila:
        print(elemento, end='')
    print()