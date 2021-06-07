
import numpy as np
import math
import matplotlib.pyplot as plt
class Mecanismo:
    def Calc_Mobilidade(self,elos,num_j_simples,num_j_meia=0):
        return 3*(elos - 1) - 2*num_j_simples - num_j_meia
    def num_Cirs(self,elos,pontos_fixos=2):
        return (elos*(elos-1))/pontos_fixos
    def mec_BielaEx(self,elos=[], ang=0,deslocamento=0,vert=True):
        ang = np.deg2rad(ang)
        x_motor = elos[0]*np.cos(ang)
        y_motor = elos[0]*np.sin(ang)
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
mec = Mecanismo()

motor_cir,biela_cir,x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept= mec.mec_BielaEx([0.09 , 0.300],180,0.150)
vel_ang_ab = mec.Vel_Ang_motor(vel_motor=954.96,vel_in_rpm=True)
Vel_b = mec.Vel_Ponto(0.09,vel_ang_ab)
vel_ang_bc= mec.Vel_Ang(motor_cir,Vel_b)
Vel_c = mec.Vel_Ponto(biela_cir,vel_ang_bc)
print(vel_ang_ab)
print(Vel_b)
print(vel_ang_bc)
print(Vel_c)
mec.plot_mec_BielaEx(x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept)
# def plot_mec_BielaEx(self,elos=[], ang=0,deslocamento=0,vert=True):
#         ang = np.deg2rad(ang)
#         x_motor = elos[0]*np.cos(ang)
#         y_motor = elos[0]*np.sin(ang)
#         x_biela= math.sqrt(elos[1]**2 - (deslocamento - y_motor)**2)
#         fig = plt.figure()
#         ax = plt.subplot(111)
#         ax.plot([0,x_motor],[0,y_motor])
#         ax.plot([x_motor,(x_biela+x_motor)],[y_motor,deslocamento])
        
#         ax.axline((x_motor,y_motor),slope=(y_motor/x_motor),linestyle="--",linewidth=0.5)
#         ax.axline(((x_biela+x_motor),deslocamento),slope=((deslocamento-y_motor)/((x_biela+x_motor)-x_motor)),color="purple",linestyle="--",linewidth=0.5)
#         if vert:
#             slope=90
#             ax.axline(((x_biela+x_motor),deslocamento),slope=slope,color="green",linestyle="--",linewidth=0.5)
#         else:
#             slope=0
#             ax.axline(((x_biela+x_motor),deslocamento),slope=slope,color="green",linestyle="--",linewidth=0.5)
#         b_motor = -x_motor*(y_motor/x_motor) + y_motor
        
#         b_vert_biela = -(x_biela+x_motor)*slope + deslocamento
#         x_intercept= (+b_motor-b_vert_biela)/(slope-(y_motor/x_motor))
#         y_intercept = x_intercept*(y_motor/x_motor) + b_motor
#         ax.plot(x_intercept,y_intercept,"kD")
#         plt.show()
#         motor_cir = math.sqrt((x_motor-x_intercept)**2 + (y_motor-y_intercept)**2)
#         biela_cir = math.sqrt(((x_motor+x_biela)-x_intercept)**2 + (deslocamento-y_intercept)**2)
#         return motor_cir,biela_cir