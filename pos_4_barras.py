import numpy as np

def K1(d, a):
    K1 = d / a
    return K1
def K2(d, c):
    K2 = d / c
    return K2
def K3(a, b, c, d):
    K3 = (a**2 - b**2 + c**2 + d**2) / (2*a*c)
    return K3
def A(teta2, K1, K2, K3):
    A = np.cos(teta2) - K1 - K2*np.cos(teta2) + K3
    return A
def B(teta2):
    B = -2*np.sin(teta2)
    return B
def C(K1, K2, K3, teta2):
    C = K1 - (K2 + 1)*np.cos(teta2) + K3
    return C
def teta4(A, B, C):
    teta4 = 0
    delta = B**2 - 4*A*C
    if delta > 0:
        delta = np.sqrt(delta)
        teta4_pos = 2*np.arctan((-B + delta)/(2*A))
        teta4_neg = 2*np.arctan((-B - delta)/(2*A))
        return teta4_pos,teta4_neg
    else:
        return None
def teta3(teta2, teta4, a, b, c, d):
    teta4_neg = teta4[1]
    teta4_pos = teta4[0]
    if teta4_pos == np.NaN or teta4_neg == np.NaN:
        return None
    else:
        teta3_pos_sen = np.arcsin((-a*np.sin(teta2) + c*np.sin(teta4_pos)) / b)
        teta3_neg_sen = np.arcsin((-a*np.sin(teta2) + c*np.sin(teta4_neg)) / b)
    return (teta3_pos_sen, teta3_neg_sen)
    