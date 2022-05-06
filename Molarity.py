import math

def Mass_in_solution():
	mw = input ("Masukkan berat molekul dari reagen dalam g/mol/ =\n")
	vol = input("Masukkan volume dalam L =\n")
	M = input ("Masukkan molaritas dalam mol/L =\n")
	Result = float(mw)*float(M)*float(vol)
	print ("Anda harus memasukkan", (Result), "gram ke larutan anda")

def Molarity():
	g = input("Masukkan gram dari reagen =\n")
	mw = input("Masukkan berat molekul dalam g/mol =\n")
	vol = input("Masukkan volume dalam L =\n")
	Result = float(g)/(float(mw)*float(vol))
	print ("Molaritas senyawa anda adalah", (Result), "M")

def Volume():
	g = input("Masukkan gram dari reagen =\n")
	mw = input("Masukaan berat molekul dalam g/mol =\n")
	M = input("Masukkan molaritas dalam mol/L =\n")
	Result = float(g)/(float(mw)*float(M))
	print ("Tambahkan "+str(Result)+ " liter untuk mendapatkan larutan dengan molaritas yang diinginkan")


Action  =  input("Apakah anda ingin menghitung 'weight' (gram), 'molarity' atau 'volume' (L untuk membuat larutan dengan M yang diketahui)?\n") 

if Action=="weight":
	Mass_in_solution()
elif Action=="molarity":
	Molarity()
elif Action=="volume":
	Volume()
else:
	print ("=====PERHATIAN!!====== HANYA MASUKKAN 'weight', 'molarity' or 'volume'.")