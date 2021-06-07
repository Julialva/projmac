from Maquinas import Mecanismo

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