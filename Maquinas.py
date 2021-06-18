
import numpy as np
import math
import matplotlib.pyplot as plt
from pos_4_barras import *
class Mecanismo:
    def grashof(self,elos):
        aux_elos = elos
        elo_maior = max(elos)
        elo_menor = min(elos)
        elos.remove(max(aux_elos))
        elos.remove(min(aux_elos))
        elos_restantes = sum(aux_elos)
        is_grashof =((elo_maior+elo_menor) <= elos_restantes)
        tipo = None
        if is_grashof:
            if (elos[0] or elos[2] == min(elos)):
                tipo = "a"
                return is_grashof, tipo
            elif (elos[3] == min(elos)):
                tipo = "b"
                return is_grashof, tipo
            elif (elos[1] == min(elos)):
                tipo = "c"
                return is_grashof, tipo
        else:
            return is_grashof,tipo
    def Calc_Mobilidade(self,elos,num_j_simples,num_j_meia=0):
        return 3*(elos - 1) - 2*num_j_simples - num_j_meia
    def Calc_Cirs(self,elos,pontos_fixos=2):
        return (elos*(elos-1))/pontos_fixos
    def Vel_Ang_motor(self,vel_motor=0,vel_in_rpm=True):
        if vel_in_rpm:
            return (math.pi*2*vel_motor)/60 #vel in rad/s
        else:
            return vel_motor
    def Vel_Ponto(self,vetor,vel_ang_barra):
        return vetor*vel_ang_barra
    def Vel_Ang_Ponto(self,vetor,vel_ponto):
        vel_ang = vel_ponto/vetor
        return vel_ang
    def pos_elo_ang(self,elo,ang):
            x_motor = elo*np.cos(ang)
            y_motor = elo*np.sin(ang)
            return x_motor,y_motor
    def find_tetas(self,elos=[],ang=0):
        k1_1 = K1(elos[3], elos[0])
        k2_1 = K2(elos[3], elos[2])
        k3_1 = K3(elos[0],elos[1], elos[2], elos[3])
        A1 = A(ang, k1_1, k2_1, k3_1)
        B1 = B(ang)
        C1 = C(k1_1, k2_1, k3_1, ang)
        teta4_neg,teta4_pos = teta4(A1, B1, C1)
        teta3_pos_sen,teta3_neg_sen = teta3(ang, [teta4_neg,teta4_pos], elos[0], elos[1], elos[2], elos[3])
        return teta4_pos,teta4_neg,teta3_pos_sen,teta3_neg_sen,ang
    def mec_4barras(self,elos,teta4,ang):
        x_motor,y_motor = self.pos_elo_ang(elos[0],ang)
        x_incog,y_incog = self.pos_elo_ang(elos[2],teta4)
        y_incog = y_incog+0.12
        x_incog = x_incog+elos[3]
        b_motor = -x_motor*np.tan(ang)+y_motor
        b_incog = -(x_incog)*np.tan(teta4) + y_incog
        x_intercept = (b_incog-b_motor)/(np.tan(ang)-np.tan(teta4))
        y_intercept = x_intercept*np.tan(ang)+b_motor
        modulo_cir_b = math.sqrt(pow(x_motor-x_intercept,2) + pow(y_motor-y_intercept,2))
        modulo_cir_c = math.sqrt(pow(x_incog-x_intercept,2) + pow(y_incog-y_intercept,2))
        return x_motor,y_motor,x_incog,y_incog,modulo_cir_b,modulo_cir_c
    def mec_Biela(self,elos=[], ang=0,deslocamento=0):
        slope=90
        x_motor,y_motor = self.pos_elo_ang(elos[0],ang)
        x_biela= math.sqrt(elos[1]**2 - (deslocamento-y_motor)**2)
        x_biela = x_motor+x_biela
        b_motor = -x_motor*np.tan(ang) + y_motor 
        b_vert_biela = -(x_biela)*slope + deslocamento
        x_intercept= (+b_motor-b_vert_biela)/(slope-np.tan(ang))
        y_intercept = x_intercept*np.tan(ang) + b_motor
        modulo_motor_cir = math.sqrt((x_motor-x_intercept)**2 + (y_motor-y_intercept)**2)
        modulo_biela_cir = math.sqrt((x_biela-x_intercept)**2 + (deslocamento-y_intercept)**2)
        return x_motor,y_motor,x_biela,x_intercept,y_intercept,modulo_motor_cir,modulo_biela_cir
    def find_fi(self,elos=[], ang=0):
        #find fi
        return np.arccos(math.sqrt(1 - (pow(elos[0],2)/pow(elos[1],2))*pow(np.sin(ang),2)))
    def plot_mec_Biela(self,x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept):
        fig = plt.figure(figsize=(10,10))
        ax = plt.subplot(111)
        ax.plot([0,x_motor],[0,y_motor])
        ax.plot([x_motor,(x_biela)],[y_motor,deslocamento])
        ax.axline((x_motor,y_motor),slope=(y_motor/x_motor),color="purple",linestyle="--",linewidth=0.5)
        ax.axline(((x_biela),deslocamento),slope=((deslocamento-y_motor)/((x_biela+x_motor)-x_motor)),color="purple",linestyle="--",linewidth=0.5)
        ax.axline(((x_biela),deslocamento),slope=slope,color="purple",linestyle="--",linewidth=0.5)
        ax.plot(x_intercept,y_intercept,"kD")
        plt.show()

