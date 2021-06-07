
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
    def Vel_Cir(self,motor_cir,elos=[],vel_motor=0,vel_in_rpm=True):
        if vel_in_rpm:
            vel_ang_barra1 = (math.pi*2*vel_motor)/60 #vel in rad/s
        else:
            vel_ang_barra1 = vel_motor
        vel_ponto = elos[0]*vel_ang_barra1
        vel_ang_bc = vel_ponto/motor_cir
        return vel_ang_bc,vel_ponto
    def v_pistao(self,biela_cir,vel_ang_bc):
        return vel_ang_bc*(biela_cir)
mec = Mecanismo()

motor_cir_module,biela_cir,x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept= mec.mec_BielaEx([0.127,0.508],225,-0.127)
vel_ang_bc,vel_ponto = mec.Vel_Cir(motor_cir_module,elos=[0.127,0.508],vel_motor=-50,vel_in_rpm=False)
v_pistao = mec.v_pistao(biela_cir,vel_ang_bc)
print(vel_ponto)
print(vel_ang_bc)
print(v_pistao)
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