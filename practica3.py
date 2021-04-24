import pandas as pd
v=int(input("ingresar veces que desea realizar el registro"))

df=pd.DataFrame()
for n in range (v):
	n =n+1
	print("INGRESA DATOS DEL ALUMNO")
	n = (input("nombre: "))
	a = (input("apellido: "))
	e = (input("edad: "))
	g = (input("grado: "))
	gr = (input ("grupo: "))
	c = (input ("correo: "))
	
	data =  {'nombre': [n], 'apellido': [a], 'edad': [e], 'grado': [g], 'grupo': [gr], 'correo': [c] }
	
	save=int(input("Guardar datos y salir) \n \n 1.- si \n \n 2.- no"))
	df=df.append(data,ignore_index=True)
	
	if (save == 1):
		df.to_csv('practica3.csv') 
	else:
		print ('bye')
