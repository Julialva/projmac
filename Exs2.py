from Maquinas import Mecanismo
import numpy as np
mec = Mecanismo()

elo2 = np.sqrt(pow(0.12,2) + pow(0.2,2))
print(elo2)
elo3 = np.sqrt(pow(0.12,2) + pow(0.38,2))
teta4_pos,teta4_neg,ang = mec.find_teta4(elos=[0.0508,0.1778,0.2286,0.1524],ang=np.deg2rad(30))
x_motor,y_motor,x_incog,y_incog,cir_b,cir_c = mec.mec_4barras([0.0508,0.1778,0.2286,0.1524],teta4_neg,np.deg2rad(30))
vel_ang_ab = mec.Vel_Ang_motor(vel_motor=10,vel_in_rpm=False)
Vel_b = mec.Vel_Ponto(0.0508,vel_ang_ab)
vel_ang_bc= mec.Vel_Ang(cir_b,Vel_b)
Vel_c = mec.Vel_Ponto(cir_c,vel_ang_bc)
vel_ang_cd = mec.Vel_Ang(0.2286,Vel_c)
print(vel_ang_ab)
print(Vel_b)
print(vel_ang_bc)
print(Vel_c)
print(vel_ang_cd)