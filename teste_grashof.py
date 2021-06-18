from Maquinas import Mecanismo
import numpy as np
mec = Mecanismo()
elos = [0.127,0.508]
ang =np.deg2rad(225)
x_motor,y_motor,x_biela,x_intercept,y_intercept,modulo_motor_cir,modulo_biela_cir= mec.mec_Biela(elos,ang,0.127)
vel_ang_ab = mec.Vel_Ang_motor(vel_motor=50,vel_in_rpm=False)
Vel_b = mec.Vel_Ponto(elos[0],vel_ang_ab)
vel_ang_bc = mec.Vel_Ang_Ponto(modulo_motor_cir,Vel_b)
Vel_c = mec.Vel_Ponto(modulo_biela_cir,vel_ang_bc)
print(Vel_b,Vel_c)