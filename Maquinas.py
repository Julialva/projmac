
import numpy as np
import math
import matplotlib.pyplot as plt
class Mecanismo:
    def Calc_Mobilidade(self,elos,num_j_simples,num_j_meia=0):
        return 3*(elos - 1) - 2*num_j_simples - num_j_meia
    def num_Cirs(self,elos,pontos_fixos=2):
        return (elos*(elos-1))/pontos_fixos
    def plot_mec_BielaEx(self,elos=[], ang=0,deslocamento=0,vert=True):
        ang = np.deg2rad(ang)
        x_motor = elos[0]*np.cos(ang)
        y_motor = elos[0]*np.sin(ang)
        x_biela= math.sqrt(elos[1]**2 - (deslocamento - y_motor)**2)
        print(x_biela)
        fig = plt.figure()
        ax = plt.subplot(111)
        ax.plot([0,x_motor],[0,y_motor])
        ax.plot([x_motor,(x_biela+x_motor)],[y_motor,deslocamento])
        #ax.axvline(x=(x_motor+x_biela),linestyle="--",linewidth=0.5)
        ax.axline((x_motor,y_motor),slope=(y_motor/x_motor),linestyle="--",linewidth=0.5)
        ax.axline(((x_biela+x_motor),deslocamento),slope=((deslocamento-y_motor)/((x_biela+x_motor)-x_motor)),color="purple",linestyle="--",linewidth=0.5)
        if vert:
            ax.axline(((x_biela+x_motor),deslocamento),slope=90,color="green",linestyle="--",linewidth=0.5)
        else:
            ax.axline(((x_biela+x_motor),deslocamento),slope=0,color="green",linestyle="--",linewidth=0.5)
        plt.show()

#    def Vel_Cir(elos=[],vel_motor=0,vel_in_rpm=True):
#         if vel_in_rpm:
#             vel_ang_barra1 = (np.pi()*2*vel_motor)/60 #vel in rad/s
#         else:
#             vel_ang_barra1 = vel_motor
#         vel_ponto = elos[0]*vel_ang_barra1
#         #cir_ponto =
#         vel_ang_prox_barra = vel_ponto 
mec = Mecanismo()
print(mec.Calc_Mobilidade(elos=8, num_j_simples=10))
print(mec.num_Cirs(8,4))
mec.plot_mec_BielaEx([127,508],225,-127)
