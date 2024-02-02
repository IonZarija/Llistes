"""

"""
LON=1000000
variable, paraula = [], str
longitud_paraules = []
paraules_llargues, paraules_curtes = [], []
contllarg, contcurt = 0, 0

while len(variable) != LON and paraula != "\q":
    paraula = input("Digues")
    if paraula != "\q":
        variable += [paraula]

for i in range(len(variable)):
    longitud_paraules += [len(variable[i])]
    if longitud_paraules[i] > contllarg:
        contllarg = longitud_paraules[i]
    if contcurt == 0 or longitud_paraules[i]<contcurt