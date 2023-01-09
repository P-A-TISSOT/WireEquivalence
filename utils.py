import pickle

def fact(n):
    if(n == 0):
        return 1
    else:
        return n*fact(n-1)

# Création des fonctions linéaires dans le corps
def computeLinear(x,a,b,c,d):
    x = "{0:b}".format(x).zfill(4)
    s0 = (int(a[0])*int(x[0]) + int(b[0])*int(x[1]) + int(c[0])*int(x[2]) + int(d[0])*int(x[3]))%2
    s1 = (int(a[1])*int(x[0]) + int(b[1])*int(x[1]) + int(c[1])*int(x[2]) + int(d[1])*int(x[3]))%2
    s2 = (int(a[2])*int(x[0]) + int(b[2])*int(x[1]) + int(c[2])*int(x[2]) + int(d[2])*int(x[3]))%2
    s3 = (int(a[3])*int(x[0]) + int(b[3])*int(x[1]) + int(c[3])*int(x[2]) + int(d[3])*int(x[3]))%2
    return int(str(s0) + str(s1) + str(s2) + str(s3),base=2)

# Fonction permutation ?
def isP(L):
    for i in range(16):
        for j in range(i+1,16):
            if(L[i] == L[j]):
                return False
    return True

# SBox en base 16
def ID(l):
    return sum([l[j]*16**(15-j) for j in range(len(l))])

# Renvoie une liste triée dans l'ordre lexicographique
def lexicographicOrder(L):
    lex = [(sum([L[i][j]*16**(15-j) for j in range(len(L[i]))]),i) for i in range(len(L))]
    lex.sort(key=lambda x:x[0])
    return [L[lex[i][1]] for i in range(len(L))]

def addConstant(L,k):
    return [L[i]^k for i in range(len(L))]

def switch(s,x):
    x = "{0:b}".format(x).zfill(4)
    out = [0 for i in range(5)]
    i = 0
    for sw in s:
        if(sw != 4):
            out[3-i] = x[sw]
        else:
            out[3-i] = str(sum([int(x[j]) for j in range(len(x))])%2)
        i += 1
    r = ""
    for sw in range(4):
        r += out[3-sw]
    return(int(r,2))

def SaveData(data, name):
    with open("U:\Mes Documents\Equivalence Classes\\"+str(name), 'wb') as f:
        pickle.dump(data, f)

def GetData(name):
    with open("U:\Mes Documents\Equivalence Classes\\"+str(name), 'rb') as f:
        data = pickle.load(f)
    return data

def getPRESENT():
    return [12,5,6,11,9,0,10,13,3,14,15,8,4,7,1,2]

def inverse(L):
    I = [-1 for i in range(len(L))]
    p = False
    for i in range(len(L)):
        if((len(L) == 4) and (L[i] == 4)):
            p = True
        else:
            I[L[i]] = i
    if(p):
        I[I.index(-1)] = 4
    return I

def LL(S,L1,L2):
    return [switch(L1, S[switch(L2,i)]) for i in range(len(S))]