import numpy as np

def K1(d, a):
    K1 = d / a
    print('K1: %f' % K1)
    return K1
def K2(d, c):
    K2 = d / c
    print('K2: %f' % K2)
    return K2
def K3(a, b, c, d):
    K3 = (a**2 - b**2 + c**2 + d**2) / (2*a*c)
    print('K3: %f' % K3)
    return K3
def A(teta2, K1, K2, K3):
    A = np.cos(teta2) - K1 - K2*np.cos(teta2) + K3
    print('A: %f' % A)
    return A
def B(teta2):
    B = -2*np.sin(teta2)
    print('B: %f' % B)
    return B
def C(K1, K2, K3, teta2):
    C = K1 - (K2 + 1)*np.cos(teta2) + K3
    print('C: %f' % C)
    return C
def teta4(A, B, C):
    teta4 = 0
    delta = B**2 - 4*A*C
    print('Delta: %f' % delta)
    if delta > 0:
        delta = np.sqrt(delta)
        teta4_pos = 2*np.arctan((-B + delta)/(2*A))
        teta4_neg = 2*np.arctan((-B - delta)/(2*A))
        print('SOLUÇÃO OK')
        print('Solução 1 de teta4: ', np.degrees(teta4_pos))
        print('Solução 2 de teta4: ', np.degrees(teta4_neg))
        return teta4_pos,teta4_neg
    else:
        print('SOLUÇÃO NÃO CONVÉM')
        return None
def teta3(teta2, teta4, a, b, c, d):
    teta4_neg = teta4[1]
    teta4_pos = teta4[0]
    if teta4_pos == np.NaN or teta4_neg == np.NaN:
        return None
    else:
        teta3_pos_sen = np.arcsin((-a*np.sin(teta2) + c*np.sin(teta4_pos)) / b)
        teta3_neg_sen = np.arcsin((-a*np.sin(teta2) + c*np.sin(teta4_neg)) / b)
        print('SOLUÇÕES POR SENO')
        print('Solução 1 de teta3 por seno: ', np.degrees(teta3_pos_sen))
        print('Solução 2 de teta3 por seno: ', np.degrees(teta3_neg_sen))
    return (teta3_pos_sen, teta3_neg_sen)
    