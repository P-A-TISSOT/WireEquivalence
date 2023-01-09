import utils
def getAffineList():
    complete = []                                                               # Fonctions affines sur 4 bits
    for a in range(16):                                    
        a = "{0:b}".format(a).zfill(4)
        for b in range(16):
            b = "{0:b}".format(b).zfill(4)
            for c in range(16):
                c = "{0:b}".format(c).zfill(4)
                for d in range(16):
                    d = "{0:b}".format(d).zfill(4)
                    tmp = []
                    for x in range(16):
                        tmp.append(utils.computeLinear(x, a, b, c, d))
                    for k in range(16):
                        complete.append(utils.addConstant(tmp, k))
    permutations = []                                                           # Permutations affines
    for l in complete:
        if(utils.isP(l)):
            permutations.append(l)
    return complete, permutations, utils.lexicographicOrder(permutations)       # Ajout du tri lexicographique des permutations affines