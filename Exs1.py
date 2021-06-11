from Maquinas import Mecanismo
import numpy as np
mec = Mecanismo()
motor_cir,biela_cir,x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept= mec.mec_BielaEx([0.127 , 0.508],np.deg2rad(225),0.127,quadrant_shift=False)
vel_ang_ab = mec.Vel_Ang_motor(vel_motor=50,vel_in_rpm=False)
Vel_b = mec.Vel_Ponto(0.127,vel_ang_ab)
vel_ang_bc= mec.Vel_Ang(motor_cir,Vel_b)
Vel_c = mec.Vel_Ponto(biela_cir,vel_ang_bc)
print(vel_ang_ab)
print(Vel_b)
print(vel_ang_bc)
print(Vel_c)
print("A Velocidade Vb é: {}, consequentemente a velocidade Vc é: {}".format(Vel_b,Vel_c))
mec.plot_mec_BielaEx(x_motor,y_motor,x_biela,deslocamento,slope,x_intercept,y_intercept)

