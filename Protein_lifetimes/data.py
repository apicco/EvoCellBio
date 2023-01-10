import pandas as pd 
path = 'Lifetime_measurements/'

# Invagination start

I_sc = pd.read_csv( path + "Invagination_start-VS-Fim1_Sc.csv" )
I_sp = pd.read_csv( path + "Invagination_start-VS-Fim1_Sp.csv" )
I_um = pd.read_csv( path + "Invagination_start-VS-Fim1_Um.csv" )

#Ede1

Ede1_um = pd.read_csv( path + "Ede1_lifetimes_Um.csv" )
Ede1_sc = pd.read_csv( path + "Ede1_lifetimes_Sc.csv" )
Ede1_sp = pd.read_csv( path + "Ede1_lifetimes_Sp-Ede1.csv" )
Ede1_sp_Ucp8 = pd.read_csv( path + "Ede1_lifetimes_Sp-Ucp8.csv" )

#Sla1

Sla1_um = pd.read_csv( path + "Sla1_lifetimes_Um.csv" )
Sla1_sc = pd.read_csv( path + "Sla1_lifetimes_Sc.csv" )
Sla1_sp = pd.read_csv( path + "Sla1_lifetimes_Sp.csv" )

#Pan1

Pan1_um = pd.read_csv( path + "Pan1_lifetimes_Um.csv" )
Pan1_sc = pd.read_csv( path + "Pan1_lifetimes_Sc.csv" )
Pan1_sp = pd.read_csv( path + "Pan1_lifetimes_Sp.csv" )

#Wasp

Wasp_um = pd.read_csv( path + "Wasp_lifetimes_Um.csv" )
Wasp_sc = pd.read_csv( path + "Wasp_lifetimes_Sc.csv" )
Wasp_sp = pd.read_csv( path + "Wasp_lifetimes_Sp.csv" )

#Myo1

Myo1_um = pd.read_csv( path + "Myo1_lifetimes_Um.csv" )
Myo3_sc = pd.read_csv( path + "Myo3_lifetimes_Sc.csv" )
Myo5_sc = pd.read_csv( path + "Myo5_lifetimes_Sc.csv" )
Myo1_sp = pd.read_csv( path + "Myo1_lifetimes_Sp.csv" )

#Rvs167

Rvs_um = pd.read_csv( path + "Rvs167_lifetimes_Um.csv" )
Rvs_sc = pd.read_csv( path + "Rvs167_lifetimes_Sc.csv" )
Rvs_sp = pd.read_csv( path + "Rvs167_lifetimes_Sp.csv" )

#Arc18

Arc18_um = pd.read_csv( path + "Arc18_Lifetimes_Um.csv" )
Arc18_sc = pd.read_csv( path + "Arc18_Lifetimes_Sc.csv" )
Arc18_sp = pd.read_csv( path + "Arc18_Lifetimes_Sp.csv" )

#Fim1 (GFP)

Fim1_GFP_um = pd.read_csv( path + "Fim1-GFP_Lifetimes_Um.csv" )
Fim1_GFP_um_220630 = pd.read_csv( path + "Fim1-GFP_Lifetimes_Um_220630.csv" )
Fim1_GFP_sc = pd.read_csv( path + "Fim1-GFP_Lifetimes_Sc.csv" )
Fim1_GFP_sc_220630 = pd.read_csv( path + "Fim1-GFP_Lifetimes_Sc_220630.csv" )
Fim1_GFP_sp = pd.read_csv( path + "Fim1-GFP_Lifetimes_Sp.csv" )
Fim1_GFP_sp_220630 = pd.read_csv( path + "Fim1-GFP_Lifetimes_Sp_220630.csv" )

#Fim1 (RFP)

Fim1_RFP_um = pd.read_csv( path + "Fim1-RFP_Lifetimes_Um.csv" )
Fim1_RFP_um_220630 = pd.read_csv( path + "Fim1-RFP_Lifetimes_Um_220630.csv" )
Fim1_RFP_sc = pd.read_csv( path + "Fim1-RFP_Lifetimes_Sc.csv" )
Fim1_RFP_sc_220630 = pd.read_csv( path + "Fim1-RFP_Lifetimes_Sc_220630.csv" )
Fim1_RFP_sp = pd.read_csv( path + "Fim1-RFP_Lifetimes_Sp.csv" )
Fim1_RFP_sp_220630 = pd.read_csv( path + "Fim1-RFP_Lifetimes_Sp_220630.csv" )

# WASP swap

las17del_spWasp_sc = pd.read_csv( path + "las17del-spWsp1_lifetimes_Sc.csv" )
sla1del_Shd1_Las17_sc = pd.read_csv( path + "sla1del-Shd1_las17_lifetimes_Sc.csv" )
sla1del_Shd1_las17del_spWasp_sc = pd.read_csv( path + "sla1del-Shd1_las17del-spWasp_lifetimes_Sc.csv" )
sla1del_Las17_sc = pd.read_csv( path + "sla1del_Wasp_lifetimes_Sc.csv" )
sla1del_spWasp_sc = pd.read_csv( path + "sla1del_spWsp1_lifetimes_Sc.csv" )

# colors

color_Ede1 = '#F9DDBD'
color_Ede1_Ucp8 =  color_Ede1
color_Sla1 = '#EC9939'
color_Pan1 = '#F2BB7B'
color_Wasp = '#1191D1'
color_Myo1 = '#88C8E8'
color_Myo3 = color_Myo1
color_Myo5 = color_Myo1
color_Rvs = '#147C33'
color_Arc18 = '#DD5C6A'
color_Fim1 = '#CC0A20'


