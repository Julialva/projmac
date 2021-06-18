from Maquinas import Mecanismo, np



C = np.sqrt(0.12**2 +0.2**2)
D = np.sqrt(0.12**2 +0.38**2)
mec = Mecanismo()
elos=[0.18,0.24,C,D]
teta4_pos,teta4_neg,teta3_pos_sen,teta3_neg_sen,ang= mec.find_tetas(elos,ang=np.deg2rad(0))

#x_motor,y_motor,x_incog,y_incog,cir_b,cir_c = mec.mec_4barras(elos,teta4_neg,ang)
#print(x_motor,y_motor,x_incog,y_incog,cir_b,cir_c )
#vel_ang_ab = mec.Vel_Ang_motor(vel_motor=10,vel_in_rpm=False)
#Vel_b = mec.Vel_Ponto(0.0508,vel_ang_ab)
#vel_ang_bc= mec.Vel_Ang(cir_b,Vel_b)
#Vel_c = mec.Vel_Ponto(cir_c,vel_ang_bc)
#vel_ang_cd = mec.Vel_Ang(0.2286,Vel_c)
for TETA in [teta4_pos,teta4_neg]:
    x_motor,y_motor,x_incog,y_incog,cir_b,cir_c = mec.mec_4barras(elos,TETA,ang)
    print(x_motor,y_motor,x_incog,y_incog,cir_b,cir_c)
    vel_ang_ab = mec.Vel_Ang_motor(vel_motor=5,vel_in_rpm=False)

    Vel_b = mec.Vel_Ponto(0.18,vel_ang_ab)
    vel_ang_bc= mec.Vel_Ang_Ponto(0.4,Vel_b)

    Vel_c = mec.Vel_Ponto(0.466,vel_ang_bc)
    vel_ang_cd = mec.Vel_Ang_Ponto(C,Vel_c)
    print("Para TETA4 = {}... \n A Velocidade Vb é: {}, consequentemente a velocidade Vc é: {} e velocidade angular Wcd é: {}".format(np.rad2deg(TETA),Vel_b,Vel_c,vel_ang_cd))
