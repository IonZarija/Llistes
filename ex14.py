"""

"""
preus=[]
quantS=[[] for i in range(3)]

for i in range(5):
    preu=float(input())
    preus.append(preu)
for i in range(5):
    for j in range(3):
        quant=int(input())
        quantS[j].append(quant)

for i in range(5):
    quantT=sum(quantS[j][i] for j in range(3))
    print("a")

quantS2=sum(quantS[1])
print("2")

quant13= quantS[0][2]
print("13")

recapSuc=[sum(preus[i]* quantS[j][i] for j in range(3) for i in range(5))]
for j in range(3):
    print("hola")

recapTE=sum(recapSuc)
print("RS")

sucMax = recapSuc.index(max(recapSuc))
print("S")