
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.lib.index_tricks import nd_grid
from pos_4_barras import *
class Mecanismo:
    def Calc_Mobilidade(self,elos,num_j_simples,num_j_meia=0):
        return 3*(elos - 1) - 2*num_j_simples - num_j_meia
    def num_Cirs(self,elos,pontos_fixos=2):
        return (elos*(elos-1))/pontos_fixos
    def Vel_Ang_motor(self,vel_motor=0,vel_in_rpm=True):
        if vel_in_rpm:
            return (math.pi*2*vel_motor)/60 #vel in rad/s
        else:
            return vel_motor
    def Vel_Ponto(self,vetor,vel_ang_barra):
        return vetor*vel_ang_barra
    def Vel_Ang(self,vetor,vel_ponto):
        vel_ang = vel_ponto/vetor
        return vel_ang
    def pos_elo_ang(self,elo,ang):
        ang = np.deg2rad(ang)
        x_motor = elo*np.cos(ang)
        y_motor = elo*np.sin(ang)
        return x_motor,y_motor
    def mec_4Barras(self,elos=[],ang=0):
        k1_1 = K1(elos[3], elos[0])
        k2_1 = K2(elos[3], elos[2])
        k3_1 = K3(elos[0],elos[1], elos[2], elos[3])
        A1 = A(ang, k1_1, k2_1, k3_1)
        B1 = B(ang)
        C1 = C(k1_1, k2_1, k3_1, ang)
        teta4_pos,teta4_neg = teta4(A1, B1, C1)
        x_motor,y_motor = self.pos_elo_ang(elos[0],ang)
        x_elo2_pos,y_elo2_pos = self.pos_elo_ang(elos[2],teta4_pos)
        x_elo2_neg,y_elo2_neg = self.pos_elo_ang(elos[2],teta4_neg)
        b_motor = -x_motor*np.tan(ang) + y_motor 
        b_elo2_pos = -(elos[3]+x_elo2_pos)*np.tan(teta4_pos) + y_elo2_pos
        b_elo2_neg = -(elos[3]+x_elo2_neg)*np.tan(teta4_neg) + y_elo2_neg
        x_intercept_pos = (b_motor-b_elo2_pos)/(np.tan(teta4_pos)-np.tan(ang))
        x_intercept_neg = (b_motor-b_elo2_neg)/(np.tan(teta4_neg)-np.tan(ang))
        y_intercept_pos = x_intercept_pos*np.tan(ang)+b_motor
        y_intercept_neg = x_intercept_neg*np.tan(ang)+b_motor
        motor_cir_pos = math.sqrt((x_motor-x_intercept_pos)**2 + (y_motor-y_intercept_pos)**2)
        elo2_cir_pos = math.sqrt(((x_elo2_pos+elos[3])-x_intercept_pos)**2 + (y_elo2_pos-y_intercept_pos)**2)
        motor_cir_neg = math.sqrt((x_motor-x_intercept_neg)**2 + (y_motor-y_intercept_neg)**2)
        elo2_cir_neg = math.sqrt(((x_elo2_neg+elos[3])-x_intercept_neg)**2 + (y_elo2_neg-y_intercept_neg)**2)
        return x_motor,y_motor,x_intercept_pos,x_intercept_neg,y_intercept_pos,y_elo2_neg,x_intercept_pos,x_intercept_neg,y_intercept_pos,y_intercept_neg,motor_cir_pos,motor_cir_neg,elo2_cir_pos,elo2_cir_neg
    def mec_BielaEx(self,elos=[], ang=0,deslocamento=0,vert=True):
        x_motor,y_motor = self.pos_elo_ang(elos[0],ang)
        x_biela= math.sqrt(elos[1]**2 - (deslocamento - y_motor)**2)
        if vert:
            slope=90
        else:
            slope=0
        b_motor = -x_motor*(y_motor/x_motor) + y_motor 
        b_vert_biela = -(x_biela+x_motor)*slope + deslocamento
        x_intercept= (+b_motor-b_vert_biela)/(slope-(y_motor/x_motor))
        y_intercept = x_intercept*(y_motor/x_motor) + b_motor
        motor_cir = math.sqrt((x_motor-x_intercept)**2 + (y_motor-y_intercept)**2)
        biela_cir = math.sqrt(((x_motor+x_biela)-x_intercept)**2 + (deslocamento-y_intercept)**2)
        return motor_cir,biela_cir,x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept
    def plot_mec_BielaEx(self,x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept):
        fig = plt.figure(figsize=(10,10))
        ax = plt.subplot(111)
        ax.plot([0,x_motor],[0,y_motor])
        ax.plot([x_motor,(x_biela+x_motor)],[y_motor,deslocamento])
        ax.axline((x_motor,y_motor),slope=(y_motor/x_motor),linestyle="--",linewidth=0.5)
        ax.axline(((x_biela+x_motor),deslocamento),slope=((deslocamento-y_motor)/((x_biela+x_motor)-x_motor)),color="purple",linestyle="--",linewidth=0.5)
        ax.axline(((x_biela+x_motor),deslocamento),slope=slope,color="green",linestyle="--",linewidth=0.5)
        ax.plot(x_intercept,y_intercept,"kD")
        plt.show()

