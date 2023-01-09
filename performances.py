import utils
import itertools
import time

def Affine4():
    affine = utils.GetData("Affine")
    t = time.time()
    wire = []
    for a in affine:
        w = False
        for l in itertools.permutations([i for i in range(4)]):
            for l_ in itertools.permutations([i for i in range(4)]):
                a_ = [utils.switch(l, a[utils.switch(l_,i)]) for i in range(len(a))]
                if(utils.ID(a_) < utils.ID(a)):
                    w = True
                    break
            if(w):
                break
        if(not w):
            wire.append(a)
    print("Affine 4 bits:", len(wire), "->", int(time.time()-t), "s")
    

def Affine5():
    affine = utils.GetData("Wire4Affine")
    t = time.time()
    wire = []
    for a in affine:
        w = False
        for l in itertools.permutations([i for i in range(5)]):
            for l_ in itertools.permutations([i for i in range(5)]):
                a_ = [utils.switch(l, a[utils.switch(l_,i)]) for i in range(len(a))]
                if(utils.ID(a_) < utils.ID(a)):
                    w = True
                    break
            if(w):
                break
        if(not w):
            wire.append(a)
    print("Affine 5 bits:", len(wire), "->", int(time.time()-t), "s")

def Linear4():
    linear = utils.GetData("Linear")
    t = time.time()
    wire = []
    for a in linear:
        w = False
        for l in itertools.permutations([i for i in range(4)]):
            for l_ in itertools.permutations([i for i in range(4)]):
                a_ = [utils.switch(l, a[utils.switch(l_,i)]) for i in range(len(a))]
                if(utils.ID(a_) < utils.ID(a)):
                    w = True
                    break
            if(w):
                break
        if(not w):
            wire.append(a)
    print("Linear 4 bits:", len(wire), "->", int(time.time()-t), "s")

def Linear5():
    affine = utils.GetData("Wire4Linear")
    t = time.time()
    wire = []
    for a in affine:
        w = False
        for l in itertools.permutations([i for i in range(5)]):
            for l_ in itertools.permutations([i for i in range(5)]):
                a_ = [utils.switch(l, a[utils.switch(l_,i)]) for i in range(len(a))]
                if(utils.ID(a_) < utils.ID(a)):
                    w = True
                    break
            if(w):
                break
        if(not w):
            wire.append(a)
    print("Linear 5 bits:", len(wire), "->", int(time.time()-t), "s")
    
def main():
    Linear4()
    Linear5()
    Affine4()
    Affine5()