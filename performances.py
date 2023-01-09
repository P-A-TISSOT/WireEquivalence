import Wire
import time

def performances():
    t = time.time()
    Wire.getWireList4Linear()
    print("Linear4:", time.time()-t)
    t = time.time()
    Wire.getWireList5Linear()
    print("Linear5:", time.time()-t)
    t = time.time()
    Wire.getWireList4Affine()
    print("Affine4:", time.time()-t)
    t = time.time()
    Wire.getWireList4Affine()
    print("Affine5:", time.time()-t)
