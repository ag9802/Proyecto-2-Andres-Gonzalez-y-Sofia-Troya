import numpy as np

def main():
    try:    
        mult()
        provec()
        inverso()
        deter()
        trans()
    except TypeError:
        return False
def mult(a, b):
    try:
       if type(a) == list and type(b) == list:
           pass
       else:
           raise TypeError
       A = np.array(a)
       B = np.array(b)
       return A @ B
        
    except TypeError:
        return False

def provec(a, b):
    try:
        if type(a) == list and type(b) == list:
           pass
        else:
           raise TypeError
        A = np.array(a)
        B = np.array(b)
        C = np.vdot(A, B)
        return C
    except TypeError:
        return False

def inverso(a , b =""):
    try:
        if type(a) == list and b == "":
            A = np.mat(a)
            return A.I    
        elif type(a) == list and type(b) == list:
            A = np.mat(a)
            B = np.mat(b)
            C = np.linalg.solve(A, B)
            return C
        else:
            raise TypeError
    except TypeError:
        return False

def deter(a):
    try:
        if type(a) == list:
            pass
        else:
            return TypeError
        A =np.mat(a)
        return np.linalg.det(A)
    
    except TypeError:
        return False

def trans(a):
    try:
        if type(a) == list:
            pass
        else:
            raise TypeError
        A = np.mat(a)
        return A.T
    except TypeError:
        return False

if __name__ == "__main__":
    main()