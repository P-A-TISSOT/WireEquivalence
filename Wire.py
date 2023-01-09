import itertools
import Affine
import Linear
import utils

def getWireList4Affine():
    affine = Affine.getAffineList()[2]
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
    return wire

def getWireList5Affine():
    affine = Affine.getAffineList()[2]
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
    return wire

def getWireList4Linear():
    linear = Linear.getLinearList()[2]
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
    return wire

def getWireList5Linear():
    linear = Linear.getLinearList()[2]
    wire = []
    for a in linear:
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
    return wire