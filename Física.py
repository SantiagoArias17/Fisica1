import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import math 
from PIL import Image
import numpy as np
import warnings
warnings.filterwarnings('ignore')    


imagen1 = Image.open('TCONV.jpg')
imagen2 = Image.open('CRECTANGULARES.jpg')
imagen3 = Image.open('CPOLARES.jpg')
imagen4 = Image.open('CGEOGRAFICAS.jpg')
imagen5 = Image.open('VECTORES.jpg')
imagen6 = Image.open('DESCOMPOSICION.jpg')
imagen7 = Image.open('ANGDIR.jpg')
imagen8 = Image.open('MPARALELOGRAMO.jpg')
imagen9 = Image.open('MPOLIGONO.jpg')
imagen10 = Image.open('VPRELATIVA.jpg')
imagen11 = Image.open('VERTICAL1.jpg')
imagen12 = Image.open('VERTICAL2.jpg')
imagen13 = Image.open('VERTICAL3.jpg')
imagen14 = Image.open('LEYEJ1.jpg')
imagen15 = Image.open('LEYEJ1DCL.jpg')
imagen16 = Image.open('LEYEJ2.jpg')
imagen17 = Image.open('LEYEJ3.jpg')
imagen18 = Image.open('LEYEJ4.jpg')
imagen19 = Image.open('LEYEJ5.jpg')
imagen20 = Image.open('LEYEJ6.jpg')
imagen21 = Image.open('LEYEJ7.jpg')
imagen22 = Image.open('LEYEJ8.jpg')
imagen23 = Image.open('LEYEJ9.jpg')
imagen24 = Image.open('LEYEJ10.jpg')
imagen25 = Image.open('FMC1.jpg')
imagen26 = Image.open('FMC2.jpg')
imagen27 = Image.open('FMC3.jpg')
imagen28 = Image.open('FMC4.jpg')
imagen29 = Image.open('FMC5.jpg')
imagen30 = Image.open('FMC6.jpg')
imagen31 = Image.open('TORQUE1.jpg')
imagen32 = Image.open('TORQUE2.jpg')
imagen33 = Image.open('TORQUE3.jpg')
imagen34 = Image.open('TORQUE4.jpg')
imagen35 = Image.open('TORQUE5.jpg')
imagen36 = Image.open('TORQUE6.jpg')
imagen37 = Image.open('TORQUE7.jpg')

st.title("PhysiCalc: Física y Cálculos")

with st.sidebar:
	selected = option_menu(
		menu_title= "Menú Principal",
		options= ["Introducción", "Vectores", "Cinemática", "Dinámica", "Autor"],
		icons= ["camera-video-fill","arrow-up-right-square-fill","car-front-fill","apple","person-vcard-fill"]
	)

if selected == "Introducción":
	st.title(f"Video Introductorio")
	video_file = open('Introduccion.mp4', 'rb')
	video_bytes = video_file.read()
	st.video(video_bytes, format='video/mp4')



if selected == "Vectores":
	st.title(f"{selected}")
	#st.subheader("1° BACHILLERATO")
	MENU=st.sidebar.radio("VECTORES ",("Sistema de Unidades","Sistemas de Coordenadas en el plano", "Vectores en el plano", "Operaciones con vectores", "Vector Posición Relativa"))
	if MENU == "Sistema de Unidades":	
		check_database1=st.checkbox("Tipos de Magnitudes, unidades, símbolos", value=False)
		# SISTEMA DE UNIDADES
		if check_database1 == True:
			
			st.subheader('Magnitudes Fundamentales')
			df1 = pd.DataFrame()
			magnitud = ['Longitud', 'Masa', 'Tiempo', 'Temperatura', 'Cantidad de substancia', 'Intensidad luminosa', 'Intensidad de corriente']
			unidad =  ['metro', 'kilogramo', 'segundo', 'kelvin', 'mol', 'candela', 'amperio']
			símbolo = ['m', 'kg', 's', '°k', 'mol', 'cd', 'A']
			dimensión = ['L', 'M', 'T', 'θ', 'N', ' ', 'I']
			df1['MAGNITUD'] = magnitud
			df1['UNIDAD'] = unidad
			df1['SÍMBOLO'] = símbolo
			df1['DIMENSIÓN'] = dimensión
			st.write(df1)

			df2 = pd.DataFrame()
			st.subheader('Magnitudes Derivadas')
			magnitud2 = ['Velocidad', 'Aceleración', 'Fuerza', 'Densidad', 'Energía']
			unidad2 =  ['metro/segundo', 'metro/segundo²', 'Newton', 'kilogramo/metro³', 'Joule']
			símbolo2 = ['m/s', 'm/s²', 'N', 'kg/m³', 'J']
			dimensión2 = ['LT^-1', 'LT-²', 'MLT-²', 'ML-³', 'ML²T-²']
			df2['MAGNITUD'] = magnitud2
			df2['UNIDAD'] = unidad2
			df2['SÍMBOLO'] = símbolo2
			df2['DIMENSIÓN'] = dimensión2
			st.write(df2)

			df3 = pd.DataFrame()
			st.subheader('Magnitudes Suplementarias')
			magnitud3 = ['Ángulo plano', 'Ángulo sólido']
			unidad3 =  ['Radián', 'Estereoradián']
			símbolo3 = ['rad', 'Sr']
			dimensión3 = ['α', 'ω']
			df3['MAGNITUD'] = magnitud3
			df3['UNIDAD'] = unidad3
			df3['SÍMBOLO'] = símbolo3
			df3['DIMENSIÓN'] = dimensión3
			st.write(df3)

		check_database2=st.checkbox("Tabla de Conversión de Unidades", value=False)
		# Tabla de Conversión de Unidades
		
		if check_database2 == True:
			st.image(imagen1, width = 500)
			
		check_database21=st.checkbox("Prefijos en el Sistema Internacional", value=False)
		# Tabla de Conversión de Unidades
		
		if check_database21 == True:
			df31 = pd.DataFrame()
			prefijos = ['tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'deci', 'centi', 'mili', 'micro', 'nano', 'pico']
			símbolosi =  ['T', 'G', 'M', 'K', 'H', 'D', 'd', 'c', 'm', 'μ', 'n', 'p']
			factor = ['1 000 000 000 000', '1 000 000 000', '1 000 000', '1 000', '100', '10', '0.1', '0.01', '0.001', '0.000 001', '0.000 000 001', '0.000 000 000 001']
			df31['PREFIJOS'] = prefijos
			df31['SÍMBOLO'] = símbolosi
			df31['FACTOR DE MULTIPLICACIÓN'] = factor
			st.write(df31)

		check_database3=st.checkbox("**Calculadora para Conversión de Unidades**", value=False)
		if check_database3 == True:
			
			longitud= st.checkbox("Longitud", value=False)
			
			if longitud == True:
				choice_lon = st.selectbox("Escoja las unidades a convertir", ["km a m", "dm a m", "cm a m", "mm a m"])
				if choice_lon == "km a m":
					L1=st.number_input("Ingrese el valor que desea convertir de km a m")
					Lc1 = L1*1000
					st.write("El valor en metros es: ", round(Lc1,2), "m")
				if choice_lon == "dm a m":
					L2=st.number_input("Ingrese el valor que desea convertir de dm a m")
					Lc2 = L2/10
					st.write("El valor en metros es: ", round(Lc2,2), "m")
				if choice_lon == "cm a m":
					L3=st.number_input("Ingrese el valor que desea convertir de cm a m")
					Lc3 = L3/100
					st.write("El valor en metros es: ", round(Lc3,2), "m")
				if choice_lon == "mm a m":
					L4=st.number_input("Ingrese el valor que desea convertir de mm a m")
					Lc4 = L4/1000
					st.write("El valor en metros es: ", round(Lc4,2), "m")
					
			masa= st.checkbox("Masa", value=False)
			
			if masa == True:
				choice_masa = st.selectbox("Escoja las unidades a convertir", ["g a kg", "lb a kg", "oz a kg"])
				if choice_masa == "g a kg":
					M1=st.number_input("Ingrese el valor que desea convertir de g a kg")
					Mc1 = M1/1000
					st.write("El valor en kilogramo es: ", round(Mc1,2), "kg")
				if choice_masa == "lb a kg":
					M2=st.number_input("Ingrese el valor que desea convertir de lb a kg")
					Mc2 = M2/2.204
					st.write("El valor en kilogramo es: ", round(Mc2,2), "kg")
				if choice_masa == "oz a kg":
					M3=st.number_input("Ingrese el valor que desea convertir de oz a kg")
					Mc3 = M3*0.028
					st.write("El valor en kilogramo es: ", round(Mc3,3), "kg")
					
			tiempo= st.checkbox("Tiempo", value=False)
			
			if tiempo == True:
				choice_tiempo = st.selectbox("Escoja las unidades a convertir", ["año a s", "días a s", "horas a s", "minutos a s"])
				if choice_tiempo == "año a s":
					T1=st.number_input("Ingrese el valor que desea convertir de año a s", 0.0)
					Tc1 = T1*31536000
					st.write("El valor en segundos es: ", round(Tc1,2), "s")
				if choice_tiempo == "días a s":
					T2=st.number_input("Ingrese el valor que desea convertir de días a s", 0.0)
					Tc2 = T2*24*3600
					st.write("El valor en segundos es: ", round(Tc2,2), "s")
				if choice_tiempo == "horas a s":
					T3=st.number_input("Ingrese el valor que desea convertir de horas a s", 0.0)
					Tc3 = T3*3600
					st.write("El valor en segundos es: ", round(Tc3,2), "s")	
				if choice_tiempo == "minutos a s":
					T4=st.number_input("Ingrese el valor que desea convertir de minutos a s", 0.0)
					Tc4 = T4*60
					st.write("El valor en segundos es: ", round(Tc4,2), "s")	


			velocidad= st.checkbox("Velocidad", value=False)
			
			if velocidad == True:
				choice_velocidad = st.selectbox("Escoja las unidades a convertir", ["km/h a m/s", "ft/s a m/s", "milla/h a m/s"])
				if choice_velocidad == "km/h a m/s":
					V1=st.number_input("Ingrese el valor que desea convertir de km/h a m/s")
					Vc1 = V1*1000/3600
					st.write("El valor en metros/segundos es: ", round(Vc1,2), "m/s")
				if choice_velocidad == "ft/s a m/s":
					V2=st.number_input("Ingrese el valor que desea convertir de ft/s a m/s")
					Vc2 = V2*0.3048
					st.write("El valor en metros/segundos es: ", round(Vc2,2), "m/s")
				if choice_velocidad == "milla/h a m/s":
					V3=st.number_input("Ingrese el valor que desea convertir de milla/h a m/s")
					Vc3 = V3/2.237
					st.write("El valor en metros/segundos es: ", round(Vc3,2), "m/s")
					
			angulo= st.checkbox("Ángulo", value=False)
			
			if angulo == True:
				choice_angulo = st.selectbox("Escoja las unidades a convertir", ["grados a radianes", "radianes a grados"])
				if choice_angulo == "grados a radianes":
					A1=st.number_input("Ingrese el valor que desea convertir de grados a radianes")
					Ac1 = A1*3.1416/180
					st.write("El valor en radianes es: ", round(Ac1,2), "rad")
				if choice_angulo == "radianes a grados":
					A2=st.number_input("Ingrese el valor que desea convertir de radianes a grados")
					Ac2 = A2*180/3.1416
					st.write("El valor en grados es: ", round(Ac2,2), "°")
					

	if MENU == "Sistemas de Coordenadas en el plano":	
		check_sc1=st.checkbox("Coordenadas Rectangulares", value=False)
		# Coordenadas Rectangulares
		if check_sc1 == True:
			st.image(imagen2, width = 800, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 9")

			st.markdown('Su representación gráfica se lo realiza mediante un par ordenado (x;y),')
			st.markdown("donde **x** es el valor de posición en el plano para el eje de las abscisas y")
			st.markdown("**y** es el valor de posición en el plano para el eje de las ordenadas.")

			ejmcr= st.checkbox("GRAFICAR COORDENADAS RECTANGULARES EN EL PLANO CARTESIANO", value=False)
			
			if ejmcr == True:

				Xr=st.number_input("Ingrese el valor del eje de las abscisas, x", -1000.00)
				Yr=st.number_input("Ingrese el valor del eje de las ordenadas, y", -1000.00)

				Csup = [Xr, 0]
				Cobj = [Yr, 0]

				df = pd.DataFrame((zip(Csup,Cobj)), index = [ 'Coordenadas Superficie', 'Coordenadas Objetivo'], columns = ['X', 'Y'])
				# Etiquetar los puntos
				ids = [(Xr, Yr) ,"Origen"]
				def add_value_label2(x_list,y_list):
					for i, txt in enumerate(ids):
						plt.annotate(txt, (x_list[i],y_list[i]))
				fig = plt.figure(figsize=(10, 4))
				plt.scatter(df['X'], df['Y'])
				add_value_label2(df['X'], df['Y'])
				plt.plot(df['X'], df['Y'], color = 'orange')
				plt.title("Coordenadas Rectangulares en el Plano Cartesiano")
				plt.xlabel("Eje de las X")
				plt.ylabel("Eje de las Y")
				st.pyplot(fig)

		check_sc2=st.checkbox("Coordenadas Polares", value=False)
		# Coordenadas Polares
		if check_sc2 == True:
			st.image(imagen3, width = 800, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 10")

			st.markdown('Su representación gráfica se lo realiza mediante un par ordenado (r;Φ),')
			st.markdown("donde **r** es la distancia desde el origen al punto y")
			st.markdown("**Φ** es el ángulo polar medido desde el eje polar hasta el radio vector, en sentido antihorario.")

			ejmcp= st.checkbox("GRAFICAR COORDENADAS POLARES EN EL PLANO CARTESIANO", value=False)
			
			if ejmcp == True:

				rp=st.number_input("Ingrese el valor del radio vector, r", 0.1)
				Φp=st.number_input("Ingrese el ángulo polar, Φ en °",0)
				st.write("El par ordenado es: ", "(", rp,";", Φp,"°",")")

				Xp = float(rp)* math.cos(math.radians(Φp))
				Yp = float(rp)* math.sin(math.radians(Φp))

				Csup = [Xp, 0]
				Cobj = [Yp, 0]

				dfcp = pd.DataFrame((zip(Csup,Cobj)), index = [ 'Coordenadas Superficie', 'Coordenadas Objetivo'], columns = ['X', 'Y'])
				# Etiquetar los puntos
				ids = [(round(Xp,2), round(Yp,2)) ,"Origen"]
				def add_value_label2(x_list,y_list):
					for i, txt in enumerate(ids):
						plt.annotate(txt, (x_list[i],y_list[i]))
				fig = plt.figure(figsize=(10, 4))
				plt.scatter(dfcp['X'], dfcp['Y'])
				add_value_label2(dfcp['X'], dfcp['Y'])
				plt.plot(dfcp['X'], dfcp['Y'], color = 'orange')
				plt.title("Coordenadas Polares en el Plano Cartesiano")
				plt.xlabel("Eje de las X")
				plt.ylabel("Eje de las Y")
				st.pyplot(fig)

		check_sc3=st.checkbox("Coordenadas Geográficas", value=False)
		# Coordenadas Polares
		if check_sc3 == True:
			st.image(imagen4, width = 800, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 11")

			st.markdown('Su representación gráfica se lo realiza mediante un par ordenado (r;rumbo),')
			st.markdown("donde **r** es la distancia desde el origen al punto y")
			st.markdown("**rumbo** es la dirección medida a partir del Norte o Sur.")
			st.markdown("**Nota:** Para representar el rumbo, en primer lugar se hace referencia al Norte o Sur, luego el ángulo y por último la posición Este u Oeste.")

			ejmcg= st.checkbox("GRAFICAR COORDENADAS GEOGRÁFICAS EN EL PLANO CARTESIANO", value=False)
			
			if ejmcg == True:

				rg=st.number_input("Ingrese el valor de la distancia, r", 1)
				choice_rumb = st.selectbox("Escoja el rumbo N-S", ["Norte", "Sur"])
				if choice_rumb == "Norte":
					Φg=st.number_input("Ingrese el ángulo de dirección del rumbo, Φ en °",1)
					choice_rumb2 = st.selectbox("Escoja E-O", ["Este", "Oeste"])
					if choice_rumb2 == "Este":
						ag= 90 - Φg
					else: 
						ag= 90 + Φg	 

					st.write("El par ordenado es: ", "(", rg,";",choice_rumb, Φg,"°",choice_rumb2,")")
					Xg = float(rg)* math.cos(math.radians(ag))
					Yg = float(rg)* math.sin(math.radians(ag))

					Csup = [Xg, 0]
					Cobj = [Yg, 0]

					dfcg = pd.DataFrame((zip(Csup,Cobj)), index = [ 'Coordenadas Superficie', 'Coordenadas Objetivo'], columns = ['X', 'Y'])
					# Etiquetar los puntos
					ids = [(round(Xg,2), round(Yg,2)) ,"Origen"]
					def add_value_label2(x_list,y_list):
						for i, txt in enumerate(ids):
							plt.annotate(txt, (x_list[i],y_list[i]))
					fig = plt.figure(figsize=(10, 4))
					plt.scatter(dfcg['X'], dfcg['Y'])
					add_value_label2(dfcg['X'], dfcg['Y'])
					plt.plot(dfcg['X'], dfcg['Y'], color = 'orange')
					plt.title("Coordenadas Geográficas en el Plano Cartesiano")
					plt.xlabel("Eje de las X")
					plt.ylabel("Eje de las Y")
					st.pyplot(fig)

				if choice_rumb == "Sur":
					Φg2=st.number_input("Ingrese el ángulo de dirección del rumbo, Φ en °",0)
					choice_rumb3 = st.selectbox("Escoja E-O", ["Este", "Oeste"])
					if choice_rumb3 == "Este":
						ag2= 270 + Φg2
					else: 
						ag2= 270 - Φg2	 
					st.write("El par ordenado es: ", "(", rg,";",choice_rumb, Φg2,"°",choice_rumb3,")")
					Xg2 = float(rg)* math.cos(math.radians(ag2))
					Yg2 = float(rg)* math.sin(math.radians(ag2))

					Csup = [Xg2, 0]
					Cobj = [Yg2, 0]

					dfcg2 = pd.DataFrame((zip(Csup,Cobj)), index = [ 'Coordenadas Superficie', 'Coordenadas Objetivo'], columns = ['X', 'Y'])
					# Etiquetar los puntos
					ids = [(round(Xg2,2), round(Yg2,2)) ,"Origen"]
					def add_value_label2(x_list,y_list):
						for i, txt in enumerate(ids):
							plt.annotate(txt, (x_list[i],y_list[i]))
					fig = plt.figure(figsize=(10, 4))
					plt.scatter(dfcg2['X'], dfcg2['Y'])
					add_value_label2(dfcg2['X'], dfcg2['Y'])
					plt.plot(dfcg2['X'], dfcg2['Y'], color = 'orange')
					plt.title("Coordenadas Geográficas en el Plano Cartesiano")
					plt.xlabel("Eje de las X")
					plt.ylabel("Eje de las Y")
					st.pyplot(fig)
				

	if MENU == "Vectores en el plano":

		vectores=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if vectores=="Teoría":
			st.subheader("CARACTERÍSTICAS DE UN VECTOR")
			st.image(imagen5, width = 850, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 18")
			st.subheader("DESCOMPOSICIÓN DE UN VECTOR EN EL PLANO:")
			st.image(imagen6, width = 750, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 21")
			# Componentes de un vector
			comp=st.checkbox("Componentes de un vector", value=False)
			if comp == True:
				st.latex(r'''
				    	\cos(\alpha)  = \frac{A_x}{A} \Rightarrow {\color{red}A_x} = A \cdot \cos(\alpha)
				   		''')
				st.latex(r'''
				    	\sin(\alpha)  = \frac{A_y}{A} \Rightarrow {\color{red}A_y} = A \cdot \sin(\alpha) 
				   		''')

			# Magnitud
			magnitudv=st.checkbox("Magnitud en función de sus componentes", value=False)
			if magnitudv == True:
				st.latex(r'''
				    	A^2 = (A_x)^2 + (A_y)^2
				   		''')
				st.latex(r'''
				    	{\color{red}A} = \sqrt{(A_x)^2 + (A_y)^2}
				   		''')

			# Dirección
			direccionv=st.checkbox("Dirección en función de sus componentes", value=False)
			if direccionv == True:
				st.latex(r'''
				    	{\color{red}\tan(\theta)} = \frac{A_y}{A_x}
				   		''')

			# Ángulos directores
			angdir=st.checkbox("Ángulos directores", value=False)
			if angdir == True:
				st.image(imagen7, width = 500, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 23")
				st.latex(r'''
				    	\cos({\color{red}\alpha})  = \frac{A_x}{A} 
				   		''')
				st.latex(r'''
				    	\cos({\color{red}\beta})  = \frac{A_y}{A}  
				   		''')
			# Vectores unitarios
			vuni=st.checkbox("Vectores unitarios", value=False)
			if vuni == True:
				st.latex(r'''
				    	{\color{red}\vec {\mu}_A} = \frac{A_x}{A}   \vec{i} + \frac{A_y}{A} \vec{j}
				   		''')
				st.latex(r'''
				    	{\color{red}\vec {\mu}_A} = \cos(\alpha)   \vec{i} + \cos(\beta) \vec{j}
				   		''')

			# Vectores base
			vbase=st.checkbox("Vector en función de los vectores base", value=False)
			if vbase == True:
				st.latex(r'''
				    	{\color{red}\vec {A}} = A_x \vec{i} + A_y \vec{j}
				   		''')
				
		if vectores=="Ejercicio Práctico":
			modang=st.checkbox("En función de su módulo y ángulo", value=False)
			if modang == True:
				st.subheader("INGRESO DE DATOS")
				módulo = st.number_input('Ingrese el módulo del vector ', 0.10)
				dirvect = st.number_input('Ingrese la dirección del vector, θ en ° ', 0.00)
				Ax = float(módulo)* math.cos(math.radians(dirvect))
				Ay = float(módulo)* math.sin(math.radians(dirvect))
				Uax= float(Ax)/float(módulo)
				Uay= float(Ay)/float(módulo)
				alpha_vect= float(math.degrees(math.acos(Uax)))
				beta_vect= float(math.degrees(math.acos(Uay)))
				st.subheader("RESULTADOS")
				st.write("Las componentes del vector son: $A_x$ =", round(Ax,2), "y $A_y$ =" , round(Ay,2))
				st.write("Las coordenadas del vector son: = (", round(Ax,2), ";" , round(Ay,2), ")")
				st.write("Los ángulos directores del vector son: α =", round(alpha_vect,2), "° y 𝛽 =" , round(beta_vect,2), "°")
				st.write("El vector en función de sus vectores base es: = (", round(Ax,2), "i +" , round(Ay,2), "j )")
				st.write("Los vectores unitarios son: $μ$ = (", round(Uax,2), "i +" , round(Uay,2), "j )")
			
			coorec=st.checkbox("En función de sus coordenadas rectangulares", value=False)
			if coorec == True:
				st.subheader("INGRESO DE DATOS")
				Crx = st.number_input('Ingrese la coordenada en el eje X del vector', -10000.00)
				Cry = st.number_input('Ingrese la coordenada en el eje Y del vector', -10000.00)
				Cr = float(Crx**2) + float(Cry**2) 
				módulocr = float(math.sqrt(float(Cr)))

				UCrax= float(Crx)/float(módulocr)
				UCray= float(Cry)/float(módulocr)
				alpha_vectCr= float(math.degrees(math.acos(UCrax)))
				beta_vectCr= float(math.degrees(math.acos(UCray)))
				dirCr = float(math.degrees(math.atan(float(Cry)/float(Crx))))
				if (Crx>0) and (Cry>0):
					θCr = dirCr
				elif (Crx<0) and (Cry>0):
					θCr = dirCr + 180
				elif (Crx<0) and (Cry<0):
					θCr = dirCr + 180
				elif (Crx>0) and (Cry<0):
					θCr = dirCr + 360	
				st.subheader("RESULTADOS")
				st.write("Las componentes del vector son: $A_x$ =", round(Crx,2), "y $A_y$ =" , round(Cry,2))
				st.write("La dirección del vector es: θ =", round(θCr,2), "°")
				st.write("Las coordenadas del vector son: = (", round(Crx,2), ";" , round(Cry,2), ")")
				st.write("El módulo del vector es: =", round(módulocr,2))
				st.write("Los ángulos directores del vector son: α =", round(alpha_vectCr,2), "° y 𝛽 =" , round(beta_vectCr,2), "°")
				st.write("El vector en función de sus vectores base es: = (", round(Crx,2), "i +" , round(Cry,2), "j )")
				st.write("Los vectores unitarios son: $μ$ = (", round(UCrax,2), "i +" , round(UCray,2), "j )")


	if MENU == "Operaciones con vectores":	
		opvec=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if opvec=="Teoría":
			# Adición de vectores
			adición=st.checkbox("Adición de vectores", value=False)
			if adición == True:
				st.subheader("MÉTODO DEL PARALELOGRAMO")
				st.image(imagen8, width = 700, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 40")
				st.latex(r'''
				    	\vec{\color{red}R}  = \vec{A} + \vec{B} 
				   		''')
				st.latex(r'''
				    	\text{El módulo del vector Resultante es: } {\color{red}R}  = \sqrt{A^2 + B^2 + (2\cdot A \cdot B \cdot \cos(\theta))}
				   		''')
				st.latex(r'''
				    	{\color{red}1}  = 180° - \theta
				   		''')
				st.latex(r'''
				    	\text{El ángulo se puede calcular mediante la Ley de Senos: }\frac{\sin(1)}{R} = \frac{\sin({\color{red}2})}{A}  
				   		''')
			
				st.subheader("MÉTODO DEL POLIGONO")
				st.image(imagen9, width = 700, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 40")
						
				st.subheader("MÉTODO ALGEBRAICO")
				st.latex(r'''
				    	\text{Se requiere que los vectores se encuentren expresados en función de sus vectores base,} 
				   		''')
				st.latex(r'''
				    	\text{luego se realiza la suma de dos o más vectores:} 
				   		''')
				st.latex(r'''
				    	\vec{A} = A_x\vec{i} + A_y\vec{j} 
				   		''')
				st.latex(r'''
				    	\vec{B} = B_x\vec{i} + B_y\vec{j} 
				   		''')
				st.latex(r'''
				    	\vec{C} = C_x\vec{i} + C_y\vec{j} 
				   		''')
				st.latex(r'''
				    	------------------------
				   		''')
				st.latex(r'''
				    	\vec{\color{red}R} = \vec{A}+\vec{B}+\vec{C} = (A_x+B_x+C_x)\vec{i} + (A_y+B_y+C_y)\vec{j} 
				   		''')
			# Diferencia de vectores
			diferencia=st.checkbox("Diferencia de vectores", value=False)
			if diferencia == True:
				st.latex(r'''
				    	\text{La diferencia o sustracción de vectores es un caso particular de la suma de vectores.} 
				   		''')
				st.latex(r'''
				    	\text{Se conoce también como la suma de un vector con el negativo(-) de otro: } 
				   		''')
				st.latex(r'''
				    	\vec{A} - \vec{B} = \vec{A} + ( - \vec{B})
				   		''')
				st.latex(r'''
				    	\text{No se cumple la propiedad conmutativa en la diferencia de vectores:} 
				   		''')
				st.latex(r'''
				    	\vec{A} - \vec{B} \neq \vec{B} - \vec{A}
				   		''')
			# Multiplicación de un escalar por un vector
			mescalar=st.checkbox("Multiplicación de un escalar por un vector", value=False)
			if mescalar == True:
				st.latex(r'''
				    	\text{La multiplicación de un escalar (k) por un vector } \vec{A}, 
				   		''')
				st.latex(r'''
				    	\text{se obtiene del producto entre k (veces) por las componentes de A:} 
				   		''')
				st.latex(r'''
				    	k\cdot\vec{A} = k\cdot(A_x\vec{i}+A_y\vec{j})
				   		''')
				st.latex(r'''
				    	k\cdot\vec{A} = k\cdot A_x\vec{i}+k\cdot A_y\vec{j}
				   		''')
			# Producto Escalar o Producto Punto
			mesop=st.checkbox("Producto Escalar o Producto Punto", value=False)
			if mesop == True:
				st.latex(r'''
				    	\text{Se define como el producto de los módulos de dos vectores dados,}
				   		''')
				st.latex(r'''
				    	\text{y por el coseno del ángulo que forman entre ellos. El resultado es un escalar:} 
				   		''')
				st.latex(r'''
				    	\vec{A} \cdot \vec{B} = {\color{red} A \cdot B \cdot  \cos(\theta)}
				   		''')
				st.latex(r'''
				    	\text{a. El producto escalar entre dos vectores paralelos:}
				   		''')
				st.latex(r'''
				    	\text{Si} (\theta) = 0° \Rightarrow {\color{red}\vec{A} \cdot \vec{B} = A \cdot B} 
				   		''')
				st.latex(r'''
				    	\text{Si} (\theta) = 180° \Rightarrow {\color{red}\vec{A} \cdot \vec{B} = - A \cdot B} 
				   		''')
				st.latex(r'''
				    	\text{b. El producto escalar entre dos vectores perpendiculares:}
				   		''')
				st.latex(r'''
				    	\text{Si} (\theta) = 90° \Rightarrow {\color{red}\vec{A} \cdot \vec{B} = 0}
				   		''')
				st.latex(r'''
				    	\text{c. El producto escalar dos vectores iguales:}
				   		''')
				st.latex(r'''
				    	(\theta) = 0° \Rightarrow {\color{red}\vec{A} \cdot \vec{A} = A^2}
				   		''')
				st.latex(r'''
				    	\text{d. El producto escalar entre dos vectores en función de sus vectores base:}
				   		''')
				st.latex(r'''
				    	{\color{blue}\vec{i} \cdot \vec{i} = \vec{j} \cdot \vec{j} = 1}
				   		''')
				st.latex(r'''
				    	{\color{blue}\vec{i} \cdot \vec{j} = \vec{j} \cdot \vec{i} = 0}
				   		''')
				st.latex(r'''
				    	\vec{A} \cdot \vec{B} = (A_x\vec{i}+A_y\vec{j}) \cdot (B_x\vec{i}+B_y\vec{j})
				   		''')
				st.latex(r'''
				    	{\color{red}\vec{A} \cdot \vec{B} = A_x \cdot B_x + A_y \cdot B_y}
				   		''')
			# Producto Vectorial
			mprovec=st.checkbox("Producto Vectorial", value=False)
			if mprovec == True:
				st.latex(r'''
				    	\text{Se define como el producto de los módulos de dos vectores dados,}
				   		''')
				st.latex(r'''
				    	\text{y por el seno del ángulo que forman entre ellos. El resultado es otro vector:} 
				   		''')
				st.latex(r'''
				    	\vec{A} \times \vec{B} = {\color{red} \vec{C}}
				   		''')
				st.latex(r'''
				    	\vec{C} = {\color{red} A \cdot B \cdot  \sin(\theta)}
				   		''')
				st.latex(r'''
				    	\text{a. El producto vectorial entre dos vectores paralelos:}
				   		''')
				st.latex(r'''
				    	\text{Si} (\theta) = 0° \Rightarrow {\color{red}| \vec{A} \times \vec{B}| = 0} 
				   		''')
				st.latex(r'''
				    	\text{Si} (\theta) = 180° \Rightarrow {\color{red}| \vec{A} \times \vec{B}| = 0}
				   		''')
				st.latex(r'''
				    	\text{b. El producto vectorial entre dos vectores perpendiculares:}
				   		''')
				st.latex(r'''
				    	\text{Si} (\theta) = 90° \Rightarrow {\color{red}| \vec{A} \times \vec{B}| = A \cdot B}
				   		''')
				st.latex(r'''
				    	\text{c. El producto vectorial entre dos vectores iguales:}
				   		''')
				st.latex(r'''
				    	(\theta) = 0° \Rightarrow {\color{red}| \vec{A} \times \vec{A}| = 0}
				   		''')
				st.latex(r'''
				    	\text{d. El producto vectorial entre dos vectores en función de sus vectores base:}
				   		''')
				st.latex(r'''
				    	{\color{blue}\vec{i} \times \vec{i} = \vec{j} \times \vec{j} = \vec{k} \times \vec{k} = 0}
				   		''')
				st.latex(r'''
				    	{\color{red}\vec{i} \times \vec{j} = \vec{k}} \text{  ;  } {\color{green}\vec{j} \times \vec{i} = - \vec{k}}
				   		''')
				st.latex(r'''
				    	{\color{red}\vec{j} \times \vec{k} = \vec{i}} \text{  ;  } {\color{green}\vec{k} \times \vec{j} = - \vec{i}}
				   		''')
				st.latex(r'''
				    	{\color{red}\vec{k} \times \vec{i} = \vec{j}} \text{  ;  } {\color{green}\vec{i} \times \vec{k} = - \vec{j}}
				   		''')
				
				st.latex(r'''
				    	\vec{A} \times \vec{B} = (A_x\vec{i}+A_y\vec{j}) \times (B_x\vec{i}+B_y\vec{j})
				   		''')
				st.latex(r'''
				    	{\color{red}\vec{A} \times \vec{B} = (A_x \cdot B_y)\vec{k} - (A_y \cdot B_x) \vec{k}}
				   		''')	

		if opvec=="Ejercicio Práctico":
			# Adición de vectores
			adiciónej=st.checkbox("Adición de vectores", value=False)
			if adiciónej == True:
				mpara=st.checkbox("A: MÉTODO DEL PARALELOGRAMO", value=False)
				if mpara == True:
					st.subheader("INGRESO DE DATOS")
					Amp = st.number_input('Ingrese el módulo del primer vector ', 0.1)
					Bmp = st.number_input('Ingrese el módulo del segundo vector ', 0.1)
					𝛉mp = st.number_input('Ingrese el ángulo que forman los dos vectores, θ en ° ')
					R = math.sqrt(float(Amp**2)+float(Bmp**2)+float(2*Amp*Bmp*math.cos(math.radians(𝛉mp))))
					unomp = 180 - float(𝛉mp)
					mpd=float(Amp/R)* math.sin(math.radians(unomp))
					dosmp = float(math.degrees(math.asin(mpd)))
					st.subheader("RESULTADOS")
					st.write("El vector resultante es: $R$ = ", round(R,2))
					st.write("La dirección del vector resultante es = ", round(dosmp,2), "°")
					
				malge=st.checkbox("A: MÉTODO ALGEBRAICO", value=False)
				if malge == True:
					st.subheader("INGRESO DE DATOS")
					list_al1 = np.array(['i'])
					list_al2 = np.array(['i','j'])
					list_al3 = np.array(['i','j','k'])
					A=[]
					B=[]
					C=[]
					Ra=[]
					N1 = int(st.number_input("Digite el tamaño de los Vectores: [1-3] "))
					if N1 == 1:
						for f in range (0,len(list_al1)):
							x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al1[f])))
							A.append(x1)
						for f in range (0,len(list_al1)):
							x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al1[f])))
							B.append(x1)
						for f in range (0,len(list_al1)):
							x1= float(st.number_input(" Digite la componente {} del tercer vector: " .format(list_al1[f])))
							C.append(x1)
						for f in range (0,len(list_al1)):
							Ra.append(A[f]+B[f]+C[f])
						st.subheader("RESULTADOS")
						st.write("Primer vector:",*A)
						st.write("Segundo vector:",*B)
						st.write("Tercer vector:",*C)
						st.write("Vector Suma:",*Ra)
					elif N1 == 2:
						for f in range (0,len(list_al2)):
							x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al2[f])))
							A.append(x1)
						for f in range (0,len(list_al2)):
							x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al2[f])))
							B.append(x1)
						for f in range (0,len(list_al2)):
							x1= float(st.number_input(" Digite la componente {} del tercer vector: " .format(list_al2[f])))
							C.append(x1)
						for f in range (0,len(list_al2)):
							Ra.append(A[f]+B[f]+C[f])
						st.subheader("RESULTADOS")
						st.write("Primer vector:",*A)
						st.write("Segundo vector:",*B)
						st.write("Tercer vector:",*C)
						st.write("Vector Suma:",*Ra)
					elif N1 == 3:
						for f in range (0,len(list_al3)):
							x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al3[f])))
							A.append(x1)
						for f in range (0,len(list_al3)):
							x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al3[f])))
							B.append(x1)
						for f in range (0,len(list_al3)):
							x1= float(st.number_input(" Digite la componente {} del tercer vector: " .format(list_al3[f])))
							C.append(x1)
						for f in range (0,len(list_al3)):
							Ra.append(A[f]+B[f]+C[f])
						st.subheader("RESULTADOS")
						st.write("Primer vector:",*A )
						st.write("Segundo vector:",*B )
						st.write("Tercer vector:",*C )
						st.write("Vector Suma:",*Ra)

			difej=st.checkbox("Diferencia de vectores", value=False)
			if difej == True:
				mpara=st.checkbox("B: MÉTODO DEL PARALELOGRAMO", value=False)
				if mpara == True:
					st.subheader("INGRESO DE DATOS")
					Amp = st.number_input('Ingrese el módulo del primer vector ', 0.1)
					Bmp = st.number_input('Ingrese el módulo del segundo vector ', 0.1)
					𝛉mp = st.number_input('Ingrese el ángulo que forman los dos vectores, θ en ° ', 1)
					R = math.sqrt(float(Amp**2)+float(Bmp**2)-float(2*Amp*Bmp*math.cos(math.radians(𝛉mp))))
					mpd=float(Bmp/R)* math.sin(math.radians(𝛉mp))
					dosmp = float(math.degrees(math.asin(mpd)))
					st.subheader("RESULTADOS")
					st.write("El vector resultante es: $R$ = ", round(R,2))
					#st.write("La dirección del vector resultante es = ", round(dosmp,2), "°")
					
				malge=st.checkbox("B: MÉTODO ALGEBRAICO", value=False)
				if malge == True:
					st.subheader("INGRESO DE DATOS")
					list_al1 = np.array(['i'])
					list_al2 = np.array(['i','j'])
					list_al3 = np.array(['i','j','k'])
					A=[]
					B=[]
					C=[]
					Ra=[]
					N11 = int(st.number_input("Ingrese el tamaño de los Vectores: (1-3) "))
					if N11 == 1:
						for f in range (0,len(list_al1)):
							x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al1[f])))
							A.append(x1)
						for f in range (0,len(list_al1)):
							x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al1[f])))
							B.append(x1)
						for f in range (0,len(list_al1)):
							x1= float(st.number_input(" Digite la componente {} del tercer vector: " .format(list_al1[f])))
							C.append(x1)
						for f in range (0,len(list_al1)):
							Ra.append(A[f]-B[f]-C[f])
						st.subheader("RESULTADOS")
						st.write("Primer vector:",*A)
						st.write("Segundo vector:",*B)
						st.write("Tercer vector:",*C)
						st.write("Vector Resta:",*Ra)
					elif N11 == 2:
						for f in range (0,len(list_al2)):
							x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al2[f])))
							A.append(x1)
						for f in range (0,len(list_al2)):
							x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al2[f])))
							B.append(x1)
						for f in range (0,len(list_al2)):
							x1= float(st.number_input(" Digite la componente {} del tercer vector: " .format(list_al2[f])))
							C.append(x1)
						for f in range (0,len(list_al2)):
							Ra.append(A[f]-B[f]-C[f])
						st.subheader("RESULTADOS")
						st.write("Primer vector:",*A)
						st.write("Segundo vector:",*B)
						st.write("Tercer vector:",*C)
						st.write("Vector Resta:",*Ra)
					elif N11 == 3:
						for f in range (0,len(list_al3)):
							x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al3[f])))
							A.append(x1)
						for f in range (0,len(list_al3)):
							x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al3[f])))
							B.append(x1)
						for f in range (0,len(list_al3)):
							x1= float(st.number_input(" Digite la componente {} del tercer vector: " .format(list_al3[f])))
							C.append(x1)
						for f in range (0,len(list_al3)):
							Ra.append(A[f]-B[f]-C[f])
						st.subheader("RESULTADOS")
						st.write("Primer vector:",*A )
						st.write("Segundo vector:",*B )
						st.write("Tercer vector:",*C )
						st.write("Vector Resta:",*Ra)

			# Multiplicación de un escalar por un vector
			mescalarej=st.checkbox("Multiplicación de un escalar por un vector", value=False)
			if mescalarej == True:				
				st.subheader("INGRESO DE DATOS")
				listk1= np.array(['i'])
				listk2= np.array(['i','j'])
				listk3= np.array(['i','j','k'])
				k=[]
				Rk=[]
				esc= st.number_input("Ingrese el valor del escalar")
				Nk = int(st.number_input("Digite el tamaño del vector: [1-3] "))
				if Nk == 1:
					for f in range (0,len(listk1)):
						x1= float(st.number_input(" Digite la componente {} del vector: " .format(listk1[f])))
						k.append(x1)
					for f in range (0,len(listk1)):
						Rk.append(k[f]*esc)
					st.subheader("RESULTADOS")
					st.write("El vector resultante es:",*Rk)
				elif Nk == 2:
					for f in range (0,len(listk2)):
						x1= float(st.number_input(" Digite la componente {} del vector: " .format(listk2[f])))
						k.append(x1)
					for f in range (0,len(listk2)):
						Rk.append(k[f]*esc)
					st.subheader("RESULTADOS")
					st.write("El vector resultante es:",*Rk)
				elif Nk == 3:
					for f in range (0,len(listk3)):
						x1= float(st.number_input(" Digite la componente {} del vector: " .format(listk3[f])))
						k.append(x1)
					for f in range (0,len(listk3)):
						Rk.append(k[f]*esc)
					st.subheader("RESULTADOS")
					st.write("El vector resultante es:",*Rk)

			# Producto Escalar o Producto Punto
			def dot_product(V1, V2):
					if len(V1) != len(V2):
						raise ValueError("Los vectores deben tener la misma longitud para realizar el producto punto.")
					return sum(a * b for a, b in zip(V1, V2))

			def main():
				list_al1 = np.array(['i'])
				list_al2 = np.array(['i','j'])
				list_al3 = np.array(['i','j','k'])
				V1=[]
				V2=[]
				
				N2 = int(st.number_input("Digite el tamaño de los Vectores: [1-3] "))
				if N2 == 1:
					for f in range (0,len(list_al1)):
						x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al1[f])))
						V1.append(x1)
					for f in range (0,len(list_al1)):
						x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al1[f])))
						V2.append(x1)
				elif N2 == 2:
					for f in range (0,len(list_al2)):
						x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al2[f])))
						V1.append(x1)
					for f in range (0,len(list_al2)):
						x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al2[f])))
						V2.append(x1)
				elif N2 == 3:
					for f in range (0,len(list_al3)):
						x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al3[f])))
						V1.append(x1)
					for f in range (0,len(list_al3)):
						x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al3[f])))
						V2.append(x1)
				try:
					result = dot_product(V1, V2)
					st.write(f"El producto punto de los vectores es:", result)
				except ValueError as e:
					st.error(str(e))

			mespuntoej=st.checkbox("Producto Escalar o Producto Punto", value=False)
			if mespuntoej == True:				
				main()

			# Producto Vectorial
			def cross_product(V1, V2):
					if len(V1) != 3 or len(V2) != 3:
						raise ValueError("Ambos vectores deben tener exactamente 3 componentes para realizar el producto vectorial.")

					result_vector = [
						V1[1] * V2[2] - V1[2] * V2[1],
						V1[2] * V2[0] - V1[0] * V2[2],
						V1[0] * V2[1] - V1[1] * V2[0]
					]
					return result_vector

			def main_cross():
				list_al1 = np.array(['i'])
				list_al2 = np.array(['i','j'])
				list_al3 = np.array(['i','j','k'])
				V1=[]
				V2=[]
				
				N21 = int(st.number_input("Ingrese el tamaño de las componenetes de los Vectores: [1-3] "))
				if N21 == 1:
					for f in range (0,len(list_al1)):
						x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al1[f])))
						V1.append(x1)
					for f in range (0,len(list_al1)):
						x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al1[f])))
						V2.append(x1)
				elif N21 == 2:
					for f in range (0,len(list_al2)):
						x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al2[f])))
						V1.append(x1)
					for f in range (0,len(list_al2)):
						x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al2[f])))
						V2.append(x1)
				elif N21 == 3:
					for f in range (0,len(list_al3)):
						x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al3[f])))
						V1.append(x1)
					for f in range (0,len(list_al3)):
						x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al3[f])))
						V2.append(x1)
				try:
					result = cross_product(V1, V2)
					st.write(f"El producto vectorial de los vectores es:", *result)
				except ValueError as e:
					st.error(str(e))
			mvecej=st.checkbox("Producto Vectorial", value=False)
			if mvecej == True:
				main_cross()	


	if MENU == "Vector Posición Relativa":	
		vpr=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if vpr=="Teoría":
			st.image(imagen10, width = 700, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 66")
			st.latex(r'''
					    	{\color{red}\vec{r}_{B/A} = \vec{r}_B - \vec{r}_A} 
					   		''')
			st.latex(r'''
					    	{\color{red}\vec{r}_{A/B} = \vec{r}_A - \vec{r}_B} 
					   		''')
		if vpr=="Ejercicio Práctico":
			st.subheader("INGRESO DE DATOS")
			list_al1 = np.array(['i'])
			list_al2 = np.array(['i','j'])
			list_al3 = np.array(['i','j','k'])
			A1=[]
			B1=[]
			Rvpr=[]
			Rvpr2=[]
			Nvrp = int(st.number_input("Ingrese el tamaño de las componentes de los Vectores: (1-3) "))
			if Nvrp == 1:
				for f in range (0,len(list_al1)):
					x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al1[f])))
					A1.append(x1)
				for f in range (0,len(list_al1)):
					x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al1[f])))
					B1.append(x1)
				for f in range (0,len(list_al1)):
					Rvpr.append(A1[f]-B1[f])
					Rvpr2.append(B1[f]-A1[f])
				st.subheader("RESULTADOS")
				st.write("Primer vector:",*A1)
				st.write("Segundo vector:",*B1)
				st.write("El Vector Posición Relativa del 1° con respecto al 2° es:",*Rvpr)
				st.write("El Vector Posición Relativa del 2° con respecto al 1° es:",*Rvpr2)
			elif Nvrp == 2:
				for f in range (0,len(list_al2)):
					x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al2[f])))
					A1.append(x1)
				for f in range (0,len(list_al2)):
					x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al2[f])))
					B1.append(x1)
				for f in range (0,len(list_al2)):
					Rvpr.append(A1[f]-B1[f])
					Rvpr2.append(B1[f]-A1[f])
				st.subheader("RESULTADOS")
				st.write("Primer vector:",*A1)	
				st.write("Segundo vector:",*B1)
				st.write("El Vector Posición Relativa del 1° con respecto al 2° es:",*Rvpr)
				st.write("El Vector Posición Relativa del 2° con respecto al 1° es:",*Rvpr2)
			elif Nvrp == 3:
				for f in range (0,len(list_al3)):
					x1= float(st.number_input(" Digite la componente {} del primer vector: " .format(list_al3[f])))
					A1.append(x1)
				for f in range (0,len(list_al3)):
					x1= float(st.number_input(" Digite la componente {} del segundo vector: " .format(list_al3[f])))
					B1.append(x1)
				for f in range (0,len(list_al3)):
					Rvpr.append(A1[f]-B1[f])
					Rvpr2.append(B1[f]-A1[f])
				st.subheader("RESULTADOS")
				st.write("Primer vector:",*A1)
				st.write("Segundo vector:",*B1)
				st.write("El Vector Posición Relativa del 1° con respecto al 2° es:",*Rvpr)
				st.write("El Vector Posición Relativa del 2° con respecto al 1° es:",*Rvpr2)



if selected == "Cinemática":
	st.title(f"{selected}")
	#st.subheader("1° BACHILLERATO")
	MENU2=st.sidebar.radio("Cinemática ",("Terminología General","Mov. Rectilíneo", "Mov. Vertical y Caída Libre", "Mov. Circular", "Mov. Parabólico"))
	if MENU2 == "Terminología General":	
		term=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if term=="Teoría":
			definicion=st.checkbox("DEFINICIÓN", value=False)
			if definicion == True:
				st.latex(r'''
						\text{Es una rama de la Física que estudia y analiza el movimiento de un cuerpo,}
				   		''')
				st.latex(r'''
						\text{es decir, el cambio de posición con respecto a un sistema de referencia.}
				   		''')
			particula=st.checkbox("PARTÍCULA", value=False)
			if particula == True:
				st.latex(r'''
						\text{Una partícula se define como un cuerpo cuyas dimensiones son considerablemente diminutas,}
				   		''')
				st.latex(r'''
						\text{en comparación con las demás dimensiones involucradas en el fenómeno que está siendo analizado.}
				   		''')
			sisref=st.checkbox("SISTEMA DE REFERENCIA", value=False)
			if sisref == True:
				st.latex(r'''
						\text{Es un cuerpo o partícula que, en conjunto con un sistema de coordenadas, posibilita}
				   		''')
				st.latex(r'''
						\text{la identificación de la posición de otro cuerpo o partícula en un momento específico.}
				   		''')	
			vdes=st.checkbox("VECTOR DESPLAZAMIENTO", value=False)
			if vdes == True:
				st.latex(r'''
						(\vec{\Delta}r): \text{ Es una magnitud vectorial y el cambio que experimenta la posición}
				   		''')
				st.latex(r'''
						\text{de una partícula en un determinado intervalo de tiempo.}
				   		''')	
				st.latex(r'''
						\vec{\Delta}r = \vec{r_f} - \vec{r_o} 
				   		''')
				st.latex(r'''
						\vec{r_f}: \text{Es la posición final de la partícula.} 
				   		''')		
				st.latex(r'''
						\vec{r_o}: \text{Es la posición inicial de la partícula.} 
				   		''')
				st.latex(r'''
						\text{Unidades en el S.I. }: {\color{red}m}
				   		''')
			reposo=st.checkbox("REPOSO", value=False)
			if reposo == True:
				st.latex(r'''
						\text{Se dice que una partícula se encuentra en reposo durante un intervalo de tiempo,}
				   		''')
				st.latex(r'''
						\text{cuando su posición no varía dentro del mismo sistema de referencia.}
				   		''')	
			trayectoria=st.checkbox("TRAYECTORIA", value=False)
			if trayectoria == True:
				st.latex(r'''
						\text{Se refiere a la ruta que se forma al conectar las diferentes posiciones que ha ocupado}
				   		''')
				st.latex(r'''
						\text{la partícula mientras se desplaza de un punto a otro en el espacio.}
				   		''')	
			disrec=st.checkbox("DISTANCIA RECORRIDA", value=False)
			if disrec == True:
				st.latex(r'''
						(d): \text{Es la longitud que se mide a lo largo del recorrido que la partícula sigue al moverse de una posición a otra.}
				   		''')
				st.latex(r'''
						\text{Se lo puede calcular como el módulo del desplazamiento.} \Rightarrow |\vec{\Delta}r|
				   		''')	
				st.latex(r'''
						\text{Unidades en el S.I. }: {\color{red}m}
				   		''')
			velocidadm=st.checkbox("VELOCIDAD", value=False)
			if velocidadm == True:
				st.latex(r'''
						(\vec{\upsilon}): \text{ Es una magnitud vectorial y es el cambio de posición con respecto al tiempo}
				   		''')
				st.latex(r'''
						\vec{\upsilon} = \frac{\vec{\Delta}r}{\Delta t}
				   		''')
				st.latex(r'''
						\Delta t = t_f - t_o
				   		''')	
				st.latex(r'''
						{\color{red}\text{Velocidad media:}}  
				   		''')		
				st.latex(r'''
						Si: \Delta t >> 0  \Rightarrow \vec{\upsilon}_m = \frac{\vec{\Delta}r}{\Delta t}
				   		''')
				st.latex(r'''
						{\color{red}\text{Velocidad instantánea:}}  
				   		''')		
				st.latex(r'''
						\vec{\upsilon}_i = \vec{\upsilon} = \lim\limits_{\Delta t \to 0}(\frac{\vec{\Delta}r}{\Delta t} )
				   		''')
				st.latex(r'''
						\text{Unidades en el S.I. }: {\color{red}\frac{m}{s}}
				   		''')

			rapidezm=st.checkbox("RAPIDEZ", value=False)
			if rapidezm == True:
				st.latex(r'''
						(\upsilon): \text{Es una magnitud escalar y es la relación entre la distancia recorrida y el intervalo de tiempo}
				   		''')
				st.latex(r'''
						\upsilon = \frac{d}{\Delta t}
				   		''')
				st.latex(r'''
						\Delta_t = t_f - t_o
				   		''')	
				st.latex(r'''
						{\color{red}\text{Rapidez media:}}  
				   		''')		
				st.latex(r'''
						Si: \Delta t >> 0  \Rightarrow \upsilon_m = \frac{d}{\Delta t}
				   		''')
				st.latex(r'''
						{\color{red}\text{Rapidez instantánea:}}  
				   		''')		
				st.latex(r'''
						\upsilon_i = \upsilon = \lim\limits_{\Delta t \to 0}(\frac{d}{\Delta t} )
				   		''')
				st.latex(r'''
						\text{Se lo puede calcular como el módulo de la velocidad.} \Rightarrow \upsilon =|{\color{red}\vec{\upsilon}}|
				   		''')
				st.latex(r'''
						\text{Unidades en el S.I. }: {\color{red}\frac{m}{s}}
				   		''')

			aceleracionm=st.checkbox("ACELERACIÓN", value=False)
			if aceleracionm == True:
				st.latex(r'''
						(\vec{a}): \text{ Es una magnitud vectorial y es la variación de la velocidad con respecto al tiempo}
				   		''')
				st.latex(r'''
						\vec{a} = \frac{\vec{\Delta}\upsilon}{\Delta t} = \frac{\vec{\upsilon}_f - \vec{\upsilon}_o}{t_f - t_o}
				   		''')
				st.latex(r'''
						{\color{red}\text{Aceleración media:}}  
				   		''')		
				st.latex(r'''
						Si: \Delta t >> 0  \Rightarrow \vec{a}_m = \frac{\vec{\Delta}\upsilon}{\Delta t}
				   		''')
				st.latex(r'''
						{\color{red}\text{Aceleración instantánea:}}  
				   		''')		
				st.latex(r'''
						\vec{a_i} = \vec{a} = \lim\limits_{\Delta t \to 0}(\frac{\vec{\Delta}\upsilon}{\Delta t} )
				   		''')
				st.latex(r'''
						{\color{blue}\text{Componentes de la aceleración}}  
				   		''')		
				st.latex(r'''
						\vec{a} = \vec{a_T} + \vec{a_C} 
				   		''')
				st.latex(r'''
						\vec{a_T}: \text{aceleración tangencial, es el cambio en módulo de la velocidad, su dirección es tangente a la velocidad}  
				   		''')	
				st.latex(r'''
						\vec{a_C}: \text{aceleración centrípeta, es el cambio en la dirección de la velocidad, su dirección es perpendicular a la velocidad}  
				   		''')	
				st.latex(r'''
						\text{Unidades en el S.I. }: {\color{red}\frac{m}{s^2}}
				   		''')
		

		if term=="Ejercicio Práctico":
			vdes1=st.checkbox("VECTOR DESPLAZAMIENTO", value=False)
			if vdes1 == True:
				st.latex(r'''
						\vec{\Delta}r = \vec{r_f} - \vec{r_o} 
				   		''')
				st.subheader("INGRESO DE DATOS")
				list_al1c = np.array(['i'])
				list_al2c = np.array(['i','j'])
				list_al3c = np.array(['i','j','k'])
				V1c=[]
				V2c=[]
				Rc=[]
				Nc = int(st.number_input("Ingrese el tamaño de las componentes para los 2 vectores posición: [1-3] "))
				if Nc == 1:
					for fc in range (0,len(list_al1c)):
						x1c= float(st.number_input(" Digite la componente {} del Vector Posición Inicial, en metros" .format(list_al1c[fc])))
						V1c.append(x1c)
					for fc in range (0,len(list_al1c)):
						x1c= float(st.number_input(" Digite la componente {} del Vector Posición Final, en metros" .format(list_al1c[fc])))
						V2c.append(x1c)
					for fc in range (0,len(list_al1c)):
						Rc.append(V2c[fc]-V1c[fc])
					st.subheader("RESULTADOS")
					vector_po = "   ".join(["**{:.2f}** ({})".format(V1c[i], list_al1c[i]) for i in range(len(V1c))])
					st.write("Vector Posición Inicial:", vector_po, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_pf = "   ".join(["**{:.2f}** ({})".format(V2c[i], list_al1c[i]) for i in range(len(V2c))])
					st.write("Vector Posición Final:", vector_pf, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_desplazamiento0 = "   ".join(["**{:.2f}** ({})".format(Rc[i], list_al1c[i]) for i in range(len(Rc))])
					st.write("El Desplazamiento es:", vector_desplazamiento0, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					st.write("El módulo del desplazamiento es:", "**{:.2f}**".format(np.linalg.norm(Rc)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				elif Nc == 2:
					for fc in range (0,len(list_al2c)):
						x1c= float(st.number_input(" Digite la componente {} del Vector Posición Inicial, en metros" .format(list_al2c[fc])))
						V1c.append(x1c)
					for fc in range (0,len(list_al2c)):
						x1c= float(st.number_input(" Digite la componente {} del Vector Posición Final, en metros" .format(list_al2c[fc])))
						V2c.append(x1c)
					for fc in range (0,len(list_al2c)):
						Rc.append(V2c[fc]-V1c[fc])
					st.subheader("RESULTADOS")
					vector_po = "   ".join(["**{:.2f}** ({})".format(V1c[i], list_al2c[i]) for i in range(len(V1c))])
					st.write("Vector Posición Inicial:", vector_po, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_pf = "   ".join(["**{:.2f}** ({})".format(V2c[i], list_al2c[i]) for i in range(len(V2c))])
					st.write("Vector Posición Final:", vector_pf, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_desplazamiento0 = "   ".join(["**{:.2f}** ({})".format(Rc[i], list_al2c[i]) for i in range(len(Rc))])
					st.write("El Desplazamiento es:", vector_desplazamiento0, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					st.write("El módulo del desplazamiento es:", "**{:.2f}**".format(np.linalg.norm(Rc)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				elif Nc == 3:
					for fc in range (0,len(list_al3c)):
						x1c= float(st.number_input(" Digite la componente {} del Vector Posición Inicial, en metros" .format(list_al3c[fc])))
						V1c.append(x1c)
					for fc in range (0,len(list_al3c)):
						x1c= float(st.number_input(" Digite la componente {} del Vector Posición Final, en metros" .format(list_al3c[fc])))
						V2c.append(x1c)
					for fc in range (0,len(list_al3c)):
						Rc.append(V2c[fc]-V1c[fc])
					st.subheader("RESULTADOS")
					vector_po = "   ".join(["**{:.2f}** ({})".format(V1c[i], list_al3c[i]) for i in range(len(V1c))])
					st.write("Vector Posición Inicial:", vector_po, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_pf = "   ".join(["**{:.2f}** ({})".format(V2c[i], list_al3c[i]) for i in range(len(V2c))])
					st.write("Vector Posición Final:", vector_pf, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_desplazamiento0 = "   ".join(["**{:.2f}** ({})".format(Rc[i], list_al3c[i]) for i in range(len(Rc))])
					st.write("El Desplazamiento es:", vector_desplazamiento0, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					st.write("El módulo del desplazamiento es:", "**{:.2f}**".format(np.linalg.norm(Rc)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
			
			disrec1=st.checkbox("DISTANCIA RECORRIDA", value=False)
			if disrec1 == True:
				st.latex(r'''
						d = \upsilon \cdot \Delta t 
				   		''')
				st.subheader("INGRESO DE DATOS")
				raprec = st.number_input('Ingrese la rapidez con la que se mueve la partícula, en (m/s)', 0.0001)
				trec = st.number_input('Digite el intervalo de tiempo, en (s)', 0.0001)
				drec = float(raprec) * float(trec) 
				st.write("La distancia recorrida por la partícula es: **{:.2f}**".format(drec), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)

			velocidadm1=st.checkbox("VELOCIDAD", value=False)
			if velocidadm1 == True:
				
				st.latex(r'''
						\vec{\upsilon} = \frac{\vec{\Delta}r}{\Delta t}
				   		''')
				st.subheader("INGRESO DE DATOS")
				list_al1cv = np.array(['i'])
				list_al2cv = np.array(['i','j'])
				list_al3cv = np.array(['i','j','k'])
				V1cv=[]
				Rcv=[]
				tv= st.number_input('Digite el intervalo del tiempo, en (s)', 0.0001)
				Ncv = int(st.number_input("Ingrese el tamaño de las componentes para el Desplazamiento: [1-3] "))
				if Ncv == 1:
					for fcv in range (0,len(list_al1cv)):
						x1cv= float(st.number_input(" Digite la componente {} del Desplazamiento, en metros" .format(list_al1cv[fcv])))
						V1cv.append(x1cv)
					for fcv in range (0,len(list_al1cv)):
						Rcv.append(V1cv[fcv]/tv)
					st.subheader("RESULTADOS")
					vector_desplazamiento = "   ".join(["**{:.2f}** ({})".format(V1cv[i], list_al1cv[i]) for i in range(len(V1cv))])
					st.write("Vector Desplazamiento:", vector_desplazamiento, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_velocidad = "   ".join(["**{:.2f}** ({})".format(Rcv[i], list_al1cv[i]) for i in range(len(Rcv))])
					st.write("La Velocidad es:", vector_velocidad, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					st.write("El módulo de la velocidad es:", "**{:.2f}**".format(np.linalg.norm(Rcv)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				elif Ncv == 2:
					for fcv in range (0,len(list_al2cv)):
						x1cv= float(st.number_input(" Digite la componente {} del Desplazamiento, en metros" .format(list_al2cv[fcv])))
						V1cv.append(x1cv)
					for fcv in range (0,len(list_al2cv)):
						Rcv.append(V1cv[fcv]/tv)
					st.subheader("RESULTADOS")
					vector_desplazamiento = "   ".join(["**{:.2f}** ({})".format(V1cv[i], list_al2cv[i]) for i in range(len(V1cv))])
					st.write("Vector Desplazamiento:", vector_desplazamiento, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_velocidad = "   ".join(["**{:.2f}** ({})".format(Rcv[i], list_al2cv[i]) for i in range(len(Rcv))])
					st.write("La Velocidad es:", vector_velocidad, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					st.write("El módulo de la velocidad es:", "**{:.2f}**".format(np.linalg.norm(Rcv)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)

				elif Ncv == 3:
					for fcv in range (0,len(list_al3cv)):
						x1cv= float(st.number_input(" Digite la componente {} del Desplazamiento, en metros" .format(list_al3cv[fcv])))
						V1cv.append(x1cv)
					for fcv in range (0,len(list_al3cv)):
						Rcv.append(V1cv[fcv]/tv)
					st.subheader("RESULTADOS")
					vector_desplazamiento = "   ".join(["**{:.2f}** ({})".format(V1cv[i], list_al3cv[i]) for i in range(len(V1cv))])
					st.write("Vector Desplazamiento:", vector_desplazamiento, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					vector_velocidad = "   ".join(["**{:.2f}** ({})".format(Rcv[i], list_al3cv[i]) for i in range(len(Rcv))])
					st.write("La Velocidad es:", vector_velocidad, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					st.write("El módulo de la velocidad es:", "**{:.2f}**".format(np.linalg.norm(Rcv)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)

			rapidezm1=st.checkbox("RAPIDEZ", value=False)
			if rapidezm1 == True:
				st.latex(r'''
						\upsilon = \frac{d}{\Delta t}
				   		''')
				st.subheader("INGRESO DE DATOS")
				drecej = st.number_input('Ingrese la distancia recorrida por la partícula, en (m)', 0.00)
				trecej = st.number_input('Ingrese el intervalo de tiempo, en (s)', 0.0001)
				rej = float(drecej) / float(trecej) 
				st.write("La rapidez a la que se mueve la partícula es: **{:.2f}**".format(rej), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)

			aceleracionm1=st.checkbox("ACELERACIÓN", value=False)
			if aceleracionm1 == True:
				
				st.latex(r'''
						\vec{a} = \frac{\vec{\Delta}\upsilon}{\Delta t} = \frac{\vec{\upsilon}_f - \vec{\upsilon}_o}{t_f - t_o}
				   		''')
				
				st.subheader("INGRESO DE DATOS")
				list_al1ca = np.array(['i'])
				list_al2ca = np.array(['i','j'])
				list_al3ca = np.array(['i','j','k'])
				V1ca=[]
				V2ca=[]
				Rca=[]
				ta= st.number_input('Ingrese el intervalo del tiempo, en (s)', 0.0001)
				Nca = int(st.number_input("Ingrese el tamaño de las componentes para los vectores, Velocidad Inicial y Final: [1-3] "))
				if Nca == 1:
					for fca in range (0,len(list_al1ca)):
						x1ca= float(st.number_input(" Digite la componente {} de la Velocidad Inicial, (m/s)" .format(list_al1ca[fca])))
						V1ca.append(x1ca)
					for fca in range (0,len(list_al1ca)):
						x1ca= float(st.number_input(" Digite la componente {} de la Velocidad Final, (m/s)" .format(list_al1ca[fca])))
						V2ca.append(x1ca)
					for fca in range (0,len(list_al1ca)):
						Rca.append((V2ca[fca] - V1ca[fca])/ta)
					st.subheader("RESULTADOS")
					vector_vo = "   ".join(["**{:.2f}** ({})".format(V1ca[i], list_al1ca[i]) for i in range(len(V1ca))])
					st.write("Vector Velocidad Inicial:", vector_vo, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					vector_vf = "   ".join(["**{:.2f}** ({})".format(V2ca[i], list_al1ca[i]) for i in range(len(V2ca))])
					st.write("Vector Velocidad Final:", vector_vf, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					vector_aceleracion = "   ".join(["**{:.2f}** ({})".format(Rca[i], list_al1ca[i]) for i in range(len(Rca))])
					st.write("La Aceleración es:", vector_aceleracion, "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
					st.write("El módulo de la aceleración es:", "**{:.2f}**".format(np.linalg.norm(Rca)), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				elif Nca == 2:
					for fca in range (0,len(list_al2ca)):
						x1ca= float(st.number_input(" Digite la componente {} de la Velocidad Inicial, (m/s)" .format(list_al2ca[fca])))
						V1ca.append(x1ca)
					for fca in range (0,len(list_al2ca)):
						x1ca= float(st.number_input(" Digite la componente {} de la Velocidad Final, (m/s)" .format(list_al2ca[fca])))
						V2ca.append(x1ca)
					for fca in range (0,len(list_al2ca)):
						Rca.append((V2ca[fca] - V1ca[fca])/ta)
					st.subheader("RESULTADOS")
					vector_vo = "   ".join(["**{:.2f}** ({})".format(V1ca[i], list_al2ca[i]) for i in range(len(V1ca))])
					st.write("Vector Velocidad Inicial:", vector_vo, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					vector_vf = "   ".join(["**{:.2f}** ({})".format(V2ca[i], list_al2ca[i]) for i in range(len(V2ca))])
					st.write("Vector Velocidad Final:", vector_vf, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					vector_aceleracion = "   ".join(["**{:.2f}** ({})".format(Rca[i], list_al2ca[i]) for i in range(len(Rca))])
					st.write("La Aceleración es:", vector_aceleracion, "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
					st.write("El módulo de la aceleración es:", "**{:.2f}**".format(np.linalg.norm(Rca)), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)

				elif Nca == 3:
					for fca in range (0,len(list_al3ca)):
						x1ca= float(st.number_input(" Digite la componente {} de la Velocidad Inicial, (m/s)" .format(list_al3ca[fca])))
						V1ca.append(x1ca)
					for fca in range (0,len(list_al3ca)):
						x1ca= float(st.number_input(" Digite la componente {} de la Velocidad Final, (m/s)" .format(list_al3ca[fca])))
						V2ca.append(x1ca)
					for fca in range (0,len(list_al3ca)):
						Rca.append((V2ca[fca] - V1ca[fca])/ta)
					st.subheader("RESULTADOS")
					vector_vo = "   ".join(["**{:.2f}** ({})".format(V1ca[i], list_al3ca[i]) for i in range(len(V1ca))])
					st.write("Vector Velocidad Inicial:", vector_vo, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					vector_vf = "   ".join(["**{:.2f}** ({})".format(V2ca[i], list_al3ca[i]) for i in range(len(V2ca))])
					st.write("Vector Velocidad Final:", vector_vf, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					vector_aceleracion = "   ".join(["**{:.2f}** ({})".format(Rca[i], list_al3ca[i]) for i in range(len(Rca))])
					st.write("La Aceleración es:", vector_aceleracion, "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
					st.write("El módulo de la aceleración es:", "**{:.2f}**".format(np.linalg.norm(Rca)), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)

	if MENU2 == "Mov. Rectilíneo":	
		movrec=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if movrec=="Teoría":
			mru=st.checkbox("Movimiento Rectilíneo Uniforme", value=False)
			if mru == True:
				st.latex(r'''
						\text{Es el movimiento que realiza un móvil cuando la velocidad } {\color{red}\vec{\upsilon}}  
				   		''')
				st.latex(r'''
						 \text{ permanece constante en módulo, dirección y sentido:}
				   		''')
				st.latex(r'''
						{\color{red}\vec{\upsilon}} = \frac{\vec{\Delta}r}{\Delta t} = {\color{red}cte}
				   		''')
				st.latex(r'''
						\vec{\Delta}r = \vec{\upsilon} \cdot \Delta t 
				   		''')
				st.latex(r'''
						\vec{r_f} = \vec{r_o} + \vec{\upsilon} \cdot \Delta t
				   		''')
				st.latex(r'''
						\text{Si } {\color{red}\vec{\upsilon}} \text{ es constante:}
				   		''')
				st.latex(r'''
						{\color{red}\vec{a}} = \frac{\vec{\Delta\upsilon}} {\Delta t} \Rightarrow {\color{red}\vec{a}} = 0
				   		''')

			mruv=st.checkbox("Movimiento Rectilíneo Uniformemente Variado", value=False)
			if mruv == True:
				st.latex(r'''
						\text{Es el movimiento de un móvil cuya aceleración } {\color{red}\vec{a}} 
				   		''')
				st.latex(r'''
						\text{ permanece constante en módulo, dirección y sentido:}
				   		''')
				st.latex(r'''
						{\color{red}\vec{a}} = \frac{\vec{\Delta \upsilon}}{\Delta t} = {\color{red}cte}
				   		''')
				st.latex(r'''
						\vec{\Delta \upsilon} = \vec{a} \cdot \Delta t 
				   		''')
				st.latex(r'''
						{\color{red}\text{FORMULARIO CON MAGNITUDES ESCALARES}}
				   		''')
				st.latex(r'''
						\text{Si la rapidez aumenta }{\color{blue}(+)}  \text{ Si la rapidez disminuye }{\color{blue}(-)}
				   		''')
				st.latex(r'''
						{\color{green}(d)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o \pm a \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(a)} \Rightarrow {\color{red}d} = (\frac{\upsilon_o + \upsilon_f}{2}) \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(\upsilon_f)} \Rightarrow {\color{red}d} = \upsilon_o \cdot t \pm \frac{a\cdot t^2}{2}
				   		''')
				st.latex(r'''
						{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o + 2 \cdot a \cdot d
				   		''')
				st.latex(r'''
						\text{NOTA: La variable con color verde significa que es la que no se toma en cuenta en el ejercicio, como: }  
						''')
				st.latex(r'''
						{\color{green}(d) , (a), (\upsilon_f), (t)} 
				   		''')
		if movrec=="Ejercicio Práctico":
			mru1=st.checkbox("Movimiento Rectilíneo Uniforme", value=False)
			if mru1 == True:
				velocidadm1=st.checkbox("VELOCIDAD", value=False)
				if velocidadm1 == True:
					st.latex(r'''
							\vec{\upsilon} = \frac{\vec{\Delta}r}{\Delta t}
					   		''')
					st.subheader("INGRESO DE DATOS")
					list_al1cv = np.array(['i'])
					list_al2cv = np.array(['i','j'])
					list_al3cv = np.array(['i','j','k'])
					V1cv=[]
					Rcv=[]
					tv= st.number_input('Digite el intervalo del tiempo, en (s)', 0.0001)
					Ncv = int(st.number_input("Ingrese el tamaño de las componentes para el Desplazamiento: [1-3] "))
					if Ncv == 1:
						for fcv in range (0,len(list_al1cv)):
							x1cv= float(st.number_input(" Digite la componente {} del Desplazamiento, en metros" .format(list_al1cv[fcv])))
							V1cv.append(x1cv)
						for fcv in range (0,len(list_al1cv)):
							Rcv.append(V1cv[fcv]/tv)
						st.subheader("RESULTADOS")
						vector_desplazamiento = "   ".join(["**{:.2f}** ({})".format(V1cv[i], list_al1cv[i]) for i in range(len(V1cv))])
						st.write("Vector Desplazamiento:", vector_desplazamiento, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						vector_velocidad = "   ".join(["**{:.2f}** ({})".format(Rcv[i], list_al1cv[i]) for i in range(len(Rcv))])
						st.write("La Velocidad es:", vector_velocidad, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
						st.write("El módulo de la velocidad es:", "**{:.2f}**".format(np.linalg.norm(Rcv)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					elif Ncv == 2:
						for fcv in range (0,len(list_al2cv)):
							x1cv= float(st.number_input(" Digite la componente {} del Desplazamiento, en metros" .format(list_al2cv[fcv])))
							V1cv.append(x1cv)
						for fcv in range (0,len(list_al2cv)):
							Rcv.append(V1cv[fcv]/tv)
						st.subheader("RESULTADOS")
						vector_desplazamiento = "   ".join(["**{:.2f}** ({})".format(V1cv[i], list_al2cv[i]) for i in range(len(V1cv))])
						st.write("Vector Desplazamiento:", vector_desplazamiento, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						vector_velocidad = "   ".join(["**{:.2f}** ({})".format(Rcv[i], list_al2cv[i]) for i in range(len(Rcv))])
						st.write("La Velocidad es:", vector_velocidad, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
						st.write("El módulo de la velocidad es:", "**{:.2f}**".format(np.linalg.norm(Rcv)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)

					elif Ncv == 3:
						for fcv in range (0,len(list_al3cv)):
							x1cv= float(st.number_input(" Digite la componente {} del Desplazamiento, en metros" .format(list_al3cv[fcv])))
							V1cv.append(x1cv)
						for fcv in range (0,len(list_al3cv)):
							Rcv.append(V1cv[fcv]/tv)
						st.subheader("RESULTADOS")
						vector_desplazamiento = "   ".join(["**{:.2f}** ({})".format(V1cv[i], list_al3cv[i]) for i in range(len(V1cv))])
						st.write("Vector Desplazamiento:", vector_desplazamiento, "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						vector_velocidad = "   ".join(["**{:.2f}** ({})".format(Rcv[i], list_al3cv[i]) for i in range(len(Rcv))])
						st.write("La Velocidad es:", vector_velocidad, "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
						st.write("El módulo de la velocidad es:", "**{:.2f}**".format(np.linalg.norm(Rcv)), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
			
			mru1=st.checkbox("Movimiento Rectilíneo Uniformemente Variado", value=False)
			if mru1 == True:
				dwrong=st.checkbox("La variable que no se toma en cuenta es (d)", value=False)
				if dwrong == True:
					aum1=st.selectbox(" Variación de la rapidez: ", ("La rapidez aumenta", "La rapidez disminuye"))
					if aum1=="La rapidez aumenta":
						st.latex(r'''
							{\color{green}(d)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o + a \cdot t
					   		''')
						st.subheader("INGRESO DE DATOS")
						romruv = st.number_input('Ingrese la rapidez inicial, en (m/s)', 0.00)
						amruv = st.number_input('Ingrese la aceleración, en (m/s²)', 0.10)
						tmruv = st.number_input('Ingrese el tiempo, en (s)', 0.0001)
						rfmruv = float(romruv) + (float(amruv)*float(tmruv)) 
						st.write("La Rapidez Final es: **{:.2f}**".format(rfmruv), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					if aum1=="La rapidez disminuye":
						st.latex(r'''
							{\color{green}(d)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o - a \cdot t
					   		''')
						st.subheader("INGRESO DE DATOS")
						romruv = st.number_input('Ingrese la rapidez inicial, en (m/s)', 0.00)
						amruv = st.number_input('Ingrese la aceleración, en (m/s²)', 0.10)
						tmruv = st.number_input('Ingrese el tiempo, en (s)', 0.0001)
						rfmruv = float(romruv) - (float(amruv)*float(tmruv)) 
						st.write("La Rapidez Final es: **{:.2f}**".format(rfmruv), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				
				awrong=st.checkbox("La variable que no se toma en cuenta es (a)", value=False)
				if awrong == True:
					st.latex(r'''
						{\color{green}(a)} \Rightarrow {\color{red}d} = (\frac{\upsilon_o + \upsilon_f}{2}) \cdot t
						''')
					st.subheader("INGRESO DE DATOS")
					romruv2 = st.number_input('Ingrese la rapidez inicial, (m/s)', 0.00)
					rfmruv2 = st.number_input('Ingrese la rapidez final, (m/s)', 0.10)
					tmruv2 = st.number_input('Ingrese el tiempo, (s)', 0.0001)
					dmruv2 = ((float(romruv2) + float(rfmruv2))/2) * float(tmruv2) 
					st.write("La Distancia recorrida es: **{:.2f}**".format(dmruv2), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					
				vwrong=st.checkbox("La variable que no se toma en cuenta es (υf)", value=False)
				if vwrong == True:
					aum2=st.selectbox(" Variación en la rapidez: ", ("La rapidez aumenta", "La rapidez disminuye"))
					if aum2=="La rapidez aumenta":
						st.latex(r'''
							{\color{green}(\upsilon_f)} \Rightarrow {\color{red}d} = \upsilon_o \cdot t + \frac{a\cdot t^2}{2}
							''')
						st.subheader("INGRESO DE DATOS")
						romruv3 = st.number_input('Digite la rapidez inicial, en (m/s)', 0.00)
						amruv3 = st.number_input('Digite la aceleración, en (m/s²)', 0.10)
						tmruv3 = st.number_input('Digite el tiempo, en (s)', 0.0001)
						dmruv3 = (float(romruv3)*float(tmruv3)) + ((float(amruv3)*float(tmruv3**2))/2) 
						st.write("La Distancia recorrida es: **{:.2f}**".format(dmruv3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					
					if aum2=="La rapidez disminuye":
						st.latex(r'''
							{\color{green}(\upsilon_f)} \Rightarrow {\color{red}d} = \upsilon_o \cdot t - \frac{a\cdot t^2}{2}
							''')
						st.subheader("INGRESO DE DATOS")
						romruv3 = st.number_input('Digite la rapidez inicial, en (m/s)', 0.00)
						amruv3 = st.number_input('Digite la aceleración, en (m/s²)', 0.10)
						tmruv3 = st.number_input('Digite el tiempo, en (s)', 0.0001)
						dmruv3 = (float(romruv3)*float(tmruv3)) - ((float(amruv3)*float(tmruv3**2))/2) 
						st.write("La Distancia recorrida es: **{:.2f}**".format(dmruv3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					
				twrong=st.checkbox("La variable que no se toma en cuenta es (t)", value=False)
				if twrong == True:
					st.latex(r'''
						{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o + 2 \cdot a \cdot d
				   		''')
					st.subheader("INGRESO DE DATOS")
					romruv4 = st.number_input('Digite la rapidez inicial, (m/s)', 0.00)
					amruv4 = st.number_input('Digite la aceleración, (m/s²)', 0.10)
					dmruv4 = st.number_input('Digite la distancia, (m)', 0.0001)
					rfmruv4 = math.sqrt(float(romruv4**2) + (2 * float(amruv4) * float(dmruv4)))
					st.write("La Rapidez Final es: **{:.2f}**".format(rfmruv4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)


	if MENU2 == "Mov. Vertical y Caída Libre":	
		movvert=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if movvert=="Teoría":
			definicionvert=st.checkbox("DEFINICIÓN", value=False)
			if definicionvert == True:
				st.latex(r'''
						\text{Los objetos describen una trayectoria vertical.}  
				   		''')
				st.latex(r'''
						 \text{ Los objetos se mueven únicamente bajo la influencia de la gravedad una vez que son liberados.}
				   		''')
				st.latex(r'''
						{\color{red}\text{ACELERACIÓN }}{\color{red} (g)} 
				   		''')
				st.latex(r'''
						\text{Indica la variación de la velocidad por unidad de tiempo, y se toma el valor de la gravedad.}  
				   		''')
				st.latex(r'''
						{\color{red}(g)} = 9.8 m/s² = \frac{9.8 m/s}{1 s} 
				   		''')
				st.latex(r'''
						\text{Se puede decir que: por cada 1s que pase, recorre 9.8m/s}
				   		''')
				st.latex(r'''
						{\color{red}\text{FORMULARIO CON MAGNITUDES ESCALARES}}
				   		''')
				st.latex(r'''
						\text{Si el móvil baja }{\color{blue}(+)}  \text{ Si el móvil sube }{\color{blue}(-)}
				   		''')
				st.latex(r'''
						{\color{green}(h)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o \pm g \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(g)} \Rightarrow {\color{red}h} = (\frac{\upsilon_o + \upsilon_f}{2}) \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(\upsilon_f)} \Rightarrow {\color{red}h} = \upsilon_o \cdot t \pm \frac{g\cdot t^2}{2}
				   		''')
				st.latex(r'''
						{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o + 2 \cdot g \cdot h
				   		''')
				st.latex(r'''
						\text{NOTA: La variable con color verde significa que es la que no se toma en cuenta en el ejercicio, como: }  
						''')
				st.latex(r'''
						{\color{green}(h) , (g), (\upsilon_f), (t)} 
				   		''')
			mvertcaso1=st.checkbox("CASO I", value=False)
			if mvertcaso1 == True:
				st.subheader("Cuando un cuerpo se deja caer:")
				st.latex(r'''
						\text{La velocidad inicial } {\color{red}(\upsilon_o)} = \text{0 m/s}
				   		''')
				st.image(imagen11, width = 450)
			mvertcaso2=st.checkbox("CASO II", value=False)
			if mvertcaso2 == True:
				st.subheader("Cuando un cuerpo es lanzado hacia abajo:")
				st.latex(r'''
						\text{La velocidad inicial } {\color{red}(\upsilon_o)} \neq \text{0 m/s}
				   		''')
				st.image(imagen12, width = 450)
			mvertcaso3=st.checkbox("CASO III", value=False)
			if mvertcaso3 == True:
				st.subheader("Cuando un cuerpo es lanzado hacia arriba:")
				st.latex(r'''
						\text{La velocidad inicial } {\color{red}(\upsilon_o)} \neq \text{0 m/s}
				   		''')
				st.image(imagen13, width = 650)	
				st.latex(r'''
						\text{a. En la altura máxima, la rapidez instantánea es cero:} 
				   		''')
				st.latex(r'''
						{\color{red}\upsilon_B} = {\color{red}0} 
				   		''')
				st.latex(r'''
						\text{b. En un mismo nivel, la rapidez de subida es igual a la rapidez de bajada:} 
				   		''')
				st.latex(r'''
						{\color{red}\upsilon_A} = {\color{red}\upsilon_C}
				   		''')
				st.latex(r'''
						\text{c. Entre dos niveles, el tiempo de subida es igual al tiempo de bajada:} 
				   		''')
				st.latex(r'''
						{\color{red}t_{AB}} = {\color{red}t_{BC}}
				   		''')
		
		if movvert=="Ejercicio Práctico":
			hwrong=st.checkbox("(h) es la variable que no se toma en cuenta", value=False)
			if hwrong == True:
				baja1=st.selectbox(" Variación en la rapidez: ", ("El móvil baja", "El móvil sube"))
				if baja1=="El móvil baja":
					st.latex(r'''
						{\color{green}(h)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o + g \cdot t
				   		''')
					st.subheader("INGRESO DE DATOS")
					romv = st.number_input('Ingrese la rapidez inicial, en (m/s)', 0.00)
					tmv = st.number_input('Ingrese el tiempo, en (s)', 0.0001)
					rfmv = float(romv) + (9.8 *float(tmv)) 
					st.write("La Rapidez Final es: **{:.2f}**".format(rfmv), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				if baja1=="El móvil sube":
					st.latex(r'''
						{\color{green}(h)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o - g \cdot t
				   		''')
					st.subheader("INGRESO DE DATOS")
					romv = st.number_input('Ingrese la rapidez inicial, en (m/s)', 0.00)
					tmv = st.number_input('Ingrese el tiempo, en (s)', 0.0001)
					rfmv = float(romv) - (9.8 *float(tmv)) 
					st.write("La Rapidez Final es: **{:.2f}**".format(rfmv), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
			
			gwrong=st.checkbox("(g) es la variable que no se toma en cuenta", value=False)
			if gwrong == True:
				st.latex(r'''
					{\color{green}(g)} \Rightarrow {\color{red}h} = (\frac{\upsilon_o + \upsilon_f}{2}) \cdot t
					''')
				st.subheader("INGRESO DE DATOS")
				romv2 = st.number_input('Ingrese la rapidez inicial, (m/s)', 0.00)
				rfmv2 = st.number_input('Ingrese la rapidez final, (m/s)', 0.10)
				tmv2 = st.number_input('Ingrese el tiempo, (s)', 0.0001)
				hmv2 = ((float(romv2) + float(rfmv2))/2) * float(tmv2) 
				st.write("La altura es: **{:.2f}**".format(hmv2), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
				
			vwrong2=st.checkbox("(υf) es la variable que no se toma en cuenta", value=False)
			if vwrong2 == True:
				baja2=st.selectbox(" Variación de la rapidez: ", ("El móvil baja", "El móvil sube"))
				if baja2=="El móvil baja":
					st.latex(r'''
						{\color{green}(\upsilon_f)} \Rightarrow {\color{red}h} = \upsilon_o \cdot t + \frac{g\cdot t^2}{2}
						''')
					st.subheader("INGRESO DE DATOS")
					romv3 = st.number_input('Digite la rapidez inicial, en (m/s)', 0.00)
					tmv3 = st.number_input('Digite el tiempo, en (s)', 0.0001)
					hmv3 = (float(romv3)*float(tmv3)) + ((9.8 *float(tmv3**2))/2) 
					st.write("La altura es: **{:.2f}**".format(hmv3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
				
				if baja2=="El móvil sube":
					st.latex(r'''
						{\color{green}(\upsilon_f)} \Rightarrow {\color{red}h} = \upsilon_o \cdot t - \frac{g\cdot t^2}{2}
						''')
					st.subheader("INGRESO DE DATOS")
					romv3 = st.number_input('Digite la rapidez inicial, en (m/s)', 0.00)
					tmv3 = st.number_input('Digite el tiempo, en (s)', 0.0001)
					hmv3 = (float(romv3)*float(tmv3)) - ((9.8 *float(tmv3**2))/2) 
					st.write("La altura es: **{:.2f}**".format(hmv3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
				
			twrong2=st.checkbox("(t) es la variable que no se toma en cuenta", value=False)
			if twrong2 == True:
				st.latex(r'''
					{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o + 2 \cdot g \cdot h
			   		''')
				st.subheader("INGRESO DE DATOS")
				romv4 = st.number_input('Digite la rapidez inicial, (m/s)', 0.00)
				hmv4 = st.number_input('Digite la altura, (m)', 0.0001)
				rfmv4 = math.sqrt(float(romv4**2) + (2 * 9.8 * float(hmv4)))
				st.write("La Rapidez Final es: **{:.2f}**".format(rfmv4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)

	if MENU2 == "Mov. Circular":	
		movcirc=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if movcirc=="Teoría":
			mcu=st.checkbox("Movimiento Circular Uniforme", value=False)
			if mcu == True:
				st.latex(r'''
						\text{Es el movimiento que realiza un objeto describiendo una trayectoria circular con rapidez constante. }  
				   		''')
				st.latex(r'''
						{\color{red}\text{RAPIDEZ TANGENCIAL }} {\color{red}(\upsilon)}
				   		''')
				st.latex(r'''
						\text{Indica la longitud de arco que el objeto recorre por cada unidad de tiempo.}
				   		''')
				st.latex(r'''
						{\color{red}\text{VELOCIDAD TANGENCIAL }} {\color{red}(\vec{\upsilon})}
				   		''')
				st.latex(r'''
						\text{Es una magnitud vectorial. Se define mediante módulo y dirección. } {\color{blue}|\vec{\upsilon}| = \upsilon}
				   		''')
				st.latex(r'''
						{\color{red}\text{ACELERACIÓN CENTRÍPETA }} {\color{red}(\vec{a}_c)}
				   		''')
				st.latex(r'''
						\text{Siempre que hay variación de la velocidad aparece la aceleración, y tiene dirección hacia el centro de la circunferencia. } 
				   		''')
				st.latex(r'''
						{\color{red}\text{RAPIDEZ ANGULAR }} {\color{red}(\omega)}
				   		''')
				st.latex(r'''
						\text{Indica el ángulo que el radio de giro barre por cada unidad de tiempo. } 
				   		''')
				st.latex(r'''
						{\color{red}\text{PERÍODO }} {\color{red}(T)}
				   		''')
				st.latex(r'''
						\text{Es el tiempo empleado en recorrer una vuelta completa. } 
				   		''')
				st.latex(r'''
						{\color{red}\text{FRECUENCIA }} {\color{red}(f)}
				   		''')
				st.latex(r'''
						\text{Es el número de revoluciones por unidad de tiempo. } 
				   		''')
				
				st.latex(r'''
						{\color{red}\text{FORMULARIO}}
				   		''')
				st.latex(r'''
						{\color{red}\theta} = \omega \cdot  t 
				   		''')
				st.latex(r'''
						{\color{red}L} = \upsilon \cdot  t  \text{     ;     } {\color{red}L} = \omega \cdot  R 
				   		''')
				st.latex(r'''
						{\color{red}\upsilon} = \omega \cdot  R 
				   		''')
				st.latex(r'''
						{\color{red}a_c} = \frac {\upsilon² } {R }   \text{     ;     }   {\color{red} a_c} = \omega² \cdot  R 
				   		''')
				st.latex(r'''
						{\color{red}T} = \frac{2\pi} {\omega} 
				   		''')
				st.latex(r'''
						{\color{red}f} = \frac{1} {T}
				   		''')
				
				st.text("DONDE:")
				st.latex(r'''
						{\color{red}\theta} = \text{ Posición angular, (rad)}  
				   		''')
				st.latex(r'''
						{\color{red}\upsilon} = \text{ Rapidez tangencial, (m/s)}  
				   		''')
				st.latex(r'''
						{\color{red}\omega} = \text{ Rapidez angular, (rad/s)}  
				   		''')
				st.latex(r'''
						{\color{red}L} = \text{ Longitud de arco de la circunferencia, (m)}  
				   		''')
				st.latex(r'''
						{\color{red}R} = \text{ Radio de la circunferencia, (m)}  
				   		''')
				st.latex(r'''
						{\color{red}a_c} = \text{ Aceleración centrípeta, (m/s²)}  
				   		''')
				st.latex(r'''
						{\color{red}t} = \text{ Tiempo, (s)}  
				   		''')
				st.latex(r'''
						{\color{red}T} = \text{ Período, (s)}  
				   		''')
				st.latex(r'''
						{\color{red}f} = \text{ Frecuencia, (Hz)}  
				   		''')
				
				
				

			mcuv=st.checkbox("Movimiento Circular Uniformemente Variado", value=False)
			if mcuv == True:
				st.latex(r'''
						\text{Es el movimiento que realiza un objeto describiendo una trayectoria circular con aceleración angular constante. }  
				   		''')
				st.latex(r'''
						{\color{red}\text{ACELERACIÓN }} {\color{red}(\vec{a})}
				   		''')
				st.latex(r'''
						|{\color{red} \vec{a}}| = \sqrt{a_T² + a_c²} 
				   		''')
				st.latex(r'''
						{\color{red}\text{ACELERACIÓN TANGENCIAL }} {\color{red}(\vec{a}_T)}
				   		''')
				st.latex(r'''
						\text{Cuando cambia el módulo de la velocidad. } 
				   		''')
				st.latex(r'''
						{\color{red}\text{ACELERACIÓN CENTRÍPETA }} {\color{red}(\vec{a}_c)}
				   		''')
				st.latex(r'''
						\text{Cuando cambia la dirección de la velocidad. } 
				   		''')
				st.latex(r'''
						{\color{red}\text{POSICIÓN ANGULAR }} {\color{red}(\theta)}
				   		''')
				st.latex(r'''
						\text{Es el ángulo que existe entre el vector posición de una partícula y un eje de referencia (x). }  \Rightarrow 180° = \pi rad 
				   		''')
				st.latex(r'''
						{\color{red}\text{DESPLAZAMIENTO ANGULAR }} {\color{red}(\Delta\theta)}
				   		''')
				st.latex(r'''
						\text{Es la variación entre la posición angular final y la posición angular inicial de una partícula. }  \Rightarrow \Delta\theta = \theta_f - \theta_o
				   		''')
				st.latex(r'''
						{\color{red}\text{RAPIDEZ ANGULAR }} {\color{red}(\omega)}
				   		''')
				st.latex(r'''
						\text{Indica el ángulo que el radio de giro barre por cada unidad de tiempo. } \Rightarrow 1 rev = 2\pi rad
				   		''')
				st.latex(r'''
						{\color{red}\text{ACELERACIÓN ANGULAR }} {\color{red}(\alpha)}
				   		''')
				st.latex(r'''
						\text{Es la razón entre la variación de la velocidad angular que experimenta una partícula y el intervalo de tiempo. } \Rightarrow \alpha = \frac {\Delta\omega}{\Delta t}
				   		''')
				st.latex(r'''
						{\color{red}\text{FÓRMULAS ANGULARES}}
				   		''')
				st.latex(r'''
						\text{La rapidez angular aumenta }{\color{blue}(+)}  \text{ La rapidez angular disminuye }{\color{blue}(-)}
				   		''')
				st.latex(r'''
						{\color{green}(\theta)} \Rightarrow {\color{red}\omega_f} = \omega_o \pm \alpha \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(\alpha)} \Rightarrow {\color{red}\theta} = (\frac{\omega_o + \omega_f}{2}) \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(\omega_f)} \Rightarrow {\color{red}\theta} = \omega_o \cdot t \pm \frac{\alpha \cdot t^2}{2}
				   		''')
				st.latex(r'''
						{\color{green}(t)} \Rightarrow {\color{red}\omega^2_f} = \omega^2_o \pm 2 \cdot \alpha \cdot \theta
				   		''')
				st.latex(r'''
						\text{NOTA: La variable con color verde significa que es la que no se toma en cuenta en el ejercicio, como: }  
						''')
				st.latex(r'''
						{\color{green}(\theta) , (\alpha), (\omega_f), (t)} 
				   		''')
				st.text("DONDE:")
				st.latex(r'''
						{\color{red}\theta} = \text{ Posición angular, (rad)}  
				   		''')
				st.latex(r'''
						{\color{red}\omega_o} = \text{ Rapidez angular inicial, (rad/s)}  
				   		''')
				st.latex(r'''
						{\color{red}\omega_f} = \text{ Rapidez angular final, (rad/s)}  
				   		''')
				st.latex(r'''
						{\color{red}\alpha} = \text{ Aceleración angular, (rad/s²)}  
				   		''')
				st.latex(r'''
						{\color{red}t} = \text{ Tiempo, (s)}  
				   		''')
				st.latex(r'''
						{\color{red}\text{FÓRMULAS TANGENCIALES}}
				   		''')
				st.latex(r'''
						\text{La rapidez tangencial aumenta }{\color{blue}(+)}  \text{ La rapidez tangencial disminuye }{\color{blue}(-)}
				   		''')
				st.latex(r'''
						{\color{green}(L)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o \pm a_T \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(a_T)} \Rightarrow {\color{red}L} = (\frac{\upsilon_o + \upsilon_f}{2}) \cdot t
				   		''')
				st.latex(r'''
						{\color{green}(\upsilon_f)} \Rightarrow {\color{red}L} = \upsilon_o \cdot t \pm \frac{a_T \cdot t^2}{2}
				   		''')
				st.latex(r'''
						{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o \pm 2 \cdot a_T \cdot L
				   		''')
				st.latex(r'''
						\text{NOTA: La variable con color verde significa que es la que no se toma en cuenta en el ejercicio, como: }  
						''')
				st.latex(r'''
						{\color{green}(L) , (a_T), (\upsilon_f), (t)} 
				   		''')

				st.text("DONDE:")
				st.latex(r'''
						{\color{red}L} = \text{ Longitud de arco, (m)}  
				   		''')
				st.latex(r'''
						{\color{red}\upsilon_o} = \text{ Rapidez tangencial inicial, (m/s)}  
				   		''')
				st.latex(r'''
						{\color{red}\upsilon_f} = \text{ Rapidez tangencial final, (m/s)}  
				   		''')
				st.latex(r'''
						{\color{red}a_T} = \text{ Aceleración tangencial, (m/s²)}  
				   		''')
				st.latex(r'''
						{\color{red}t} = \text{ Tiempo, (s)}  
				   		''')


		if movcirc=="Ejercicio Práctico":
			mcu1=st.checkbox("Movimiento Circular Uniforme", value=False)
			if mcu1 == True:
				posang=st.checkbox("POSICIÓN ANGULAR", value=False)
				if posang == True:
					st.latex(r'''
							{\color{red}\theta} = \omega \cdot  t 
					   		''')
					st.subheader("INGRESO DE DATOS")
					ωmc = st.number_input('Ingrese la rapidez angular, en (rad/s)', 0.00)
					tmc = st.number_input('Digite el tiempo, en (s)', 0.0001)
					θmc = float(ωmc)*float(tmc) 
					st.write("La posición angular es: **{:.2f}**".format(θmc), "<span style='color: red;'>**rad**</span>", unsafe_allow_html=True)
				Lang=st.checkbox("LONGITUD DE ARCO", value=False)
				if Lang == True:
					tab1L, tab2L = st.tabs(["DATOS: (𝑣) y (t)","DATOS: (θ) y (R)"])
					with tab1L:
						st.latex(r'''
								{\color{red}L} = \upsilon \cdot  t 
						   		''')
						st.subheader("INGRESO DE DATOS")
						𝑣mc = st.number_input('Ingrese la rapidez tangencial, en (m/s)', 0.00)
						tmc2 = st.number_input('Ingrese el tiempo, en (s)', 0.0001)
						Lmc = float(𝑣mc)*float(tmc2) 
						st.write("La longitud de arco es: **{:.2f}**".format(Lmc), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					with tab2L:
						st.latex(r'''
								{\color{red}L} = \theta \cdot  R 
						   		''')
						st.subheader("INGRESO DE DATOS")
						θmc2 = st.number_input('Ingrese la posición angular, en (rad)', 0.00)
						Rmc = st.number_input('Ingrese el radio, en (m)', 0.00)
						Lmc2 = float(θmc2)*float(Rmc) 
						st.write("La longitud de arco es: **{:.2f}**".format(Lmc2), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
				𝑣tan=st.checkbox("RAPIDEZ TANGENCIAL", value=False)
				if 𝑣tan == True:
					st.latex(r'''
							{\color{red}\upsilon} = \omega \cdot  R 
					   		''')
					st.subheader("INGRESO DE DATOS")
					ωmc2 = st.number_input('Ingrese la rapidez angular, (rad/s)', 0.00)
					Rmc2 = st.number_input('Ingrese el radio, (m)', 0.00)
					𝑣tanmc = float(ωmc2)*float(Rmc2) 
					st.write("La rapidez tangencial es: **{:.2f}**".format(𝑣tanmc), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				acent=st.checkbox("ACELERACIÓN CENTRÍPETA", value=False)
				if acent == True:
					tab1ac, tab2ac = st.tabs(["DATOS: (𝑣) y (R)","DATOS: (ω) y (R)"])
					with tab1ac:
						st.latex(r'''
								{\color{red}a_c} = \frac {\upsilon²} {R} 
						   		''')
						st.subheader("INGRESO DE DATOS")
						𝑣mc2 = st.number_input('Ingrese la rapidez tangencial, (m/s)', 0.00)
						Rmc3 = st.number_input('Digite el radio, en (m)', 0.0001)
						acmc = (float(𝑣mc2)**2) / float(Rmc3) 
						st.write("La aceleración centrípeta es: **{:.2f}**".format(acmc), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
					with tab2ac:
						st.latex(r'''
								{\color{red}a_c} = \omega² \cdot R 
						   		''')
						st.subheader("INGRESO DE DATOS")
						ωmc3 = st.number_input('Digite la rapidez angular, (m/s)', 0.00)
						Rmc4 = st.number_input('Digite el radio, (m)', 0.00)
						acmc2 = float(ωmc3)*float(Rmc4) 
						st.write("La aceleración centrípeta es: **{:.2f}**".format(acmc2), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				Tcir=st.checkbox("PERÍODO Y FRECUENCIA", value=False)
				if Tcir == True:
					st.latex(r'''
							{\color{red}T} = \frac{2\pi}{\omega} \Rightarrow	{\color{red}f} = \frac{1} {T} 
					   		''')
					st.subheader("INGRESO DE DATOS")
					ωTmc = st.number_input('Ingrese el valor de la rapidez angular, (rad/s)', 0.01)
					Tmc = float(2*math.pi)/float(ωTmc) 
					fmc = float(1/Tmc)
					st.write("El Período es: **{:.2f}**".format(Tmc), "<span style='color: red;'>**s**</span>", unsafe_allow_html=True)
					st.write("La Frecuencia es: **{:.2f}**".format(fmc), "<span style='color: red;'>**Hz**</span>", unsafe_allow_html=True)

			mcuv1=st.checkbox("Movimiento Circular Uniformemente Variado", value=False)
			if mcuv1 == True:
				def generate_widget_key(name):
					return f"{name}_{id(name)}"
				
				tab1, tab2 = st.tabs(["Ecuaciones Angulares","Ecuaciones Tangenciales"])
				with tab1:

					θwrong=st.checkbox("La variable que no se toma en cuenta es (θ)", value=False)
					if θwrong == True:
						raaum1=st.selectbox(" Variación de la rapidez angular: ", ("La rapidez angular aumenta", "La rapidez angular disminuye"))
						if raaum1=="La rapidez angular aumenta":
							st.latex(r'''
								{\color{green}(\theta)} \Rightarrow {\color{red}\omega_f} = \omega_o + \alpha \cdot t
						   		''')
							st.subheader("INGRESO DE DATOS")
							ωomcuv = st.number_input('Ingrese la rapidez angular inicial, en (rad/s)', 0.00, key=generate_widget_key("rapidez_angular1a"))
							αmcuv = st.number_input('Ingrese la aceleración angular, en (rad/s²)', 0.01, key=generate_widget_key("aceleración_angular1a"))
							tmcuv = st.number_input('Ingrese el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecangular1a"))
							ωfmcuv = float(ωomcuv) + (float(αmcuv)*float(tmcuv)) 
							st.write("La Rapidez Angular Final es: **{:.2f}**".format(ωfmcuv), "<span style='color: red;'>**rad/s**</span>", unsafe_allow_html=True)
						if raaum1=="La rapidez angular disminuye":
							st.latex(r'''
								{\color{green}(\theta)} \Rightarrow {\color{red}\omega_f} = \omega_o - \alpha \cdot t
						   		''')
							st.subheader("INGRESO DE DATOS")
							ωomcuv = st.number_input('Ingrese la rapidez angular inicial, en (rad/s)', 0.00, key=generate_widget_key("rapidez_angular1d"))
							αmcuv = st.number_input('Ingrese la aceleración angular, en (rad/s²)', 0.00, key=generate_widget_key("aceleración_angular1d"))
							tmcuv = st.number_input('Ingrese el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecangular1d"))
							ωfmcuv = float(ωomcuv) - (float(αmcuv)*float(tmcuv)) 
							st.write("La Rapidez Angular Final es: **{:.2f}**".format(ωfmcuv), "<span style='color: red;'>**rad/s**</span>", unsafe_allow_html=True)
					
					αwrong=st.checkbox("La variable que no se toma en cuenta es (α)", value=False)
					if αwrong == True:
						st.latex(r'''
							{\color{green}(\alpha)} \Rightarrow {\color{red}\theta} = (\frac{\omega_o + \omega_f}{2}) \cdot t
							''')
						st.subheader("INGRESO DE DATOS")
						ωomcuv2 = st.number_input('Ingrese la rapidez angular inicial, (rad/s)', 0.00, key=generate_widget_key("rapidez_angular2a"))
						ωfmcuv2 = st.number_input('Ingrese la rapidez angular final, (rad/s)', 0.01, key=generate_widget_key("rapidezf_angular2a"))
						tmcuv2 = st.number_input('Ingrese el tiempo, (s)', 0.0001, key=generate_widget_key("tiempo_ecangular2a"))
						θmcuv2 = ((float(ωomcuv2) + float(ωfmcuv2))/2) * float(tmcuv2) 
						st.write("La Posición Angular es: **{:.2f}**".format(θmcuv2), "<span style='color: red;'>**rad**</span>", unsafe_allow_html=True)
						
					ωwrong=st.checkbox("La variable que no se toma en cuenta es (ωf)", value=False)
					if ωwrong == True:
						angaum2=st.selectbox(" Variación en la rapidez angular: ", ("La rapidez angular aumenta", "La rapidez angular disminuye"))
						if angaum2=="La rapidez angular aumenta":
							st.latex(r'''
								{\color{green}(\omega_f)} \Rightarrow {\color{red}\theta} = \omega_o \cdot t + \frac{\alpha \cdot t^2}{2}
								''')
							st.subheader("INGRESO DE DATOS")
							ωomcuv3 = st.number_input('Digite la rapidez angular inicial, en (rad/s)', 0.00, key=generate_widget_key("rapidez_angular3a"))
							αmcuv3 = st.number_input('Digite la aceleración angular, en (rad/s²)', 0.01, key=generate_widget_key("aceleración_angular3a"))
							tmcuv3 = st.number_input('Digite el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecangular3a"))
							θmcuv3 = (float(ωomcuv3)*float(tmcuv3)) + ((float(αmcuv3)*float(tmcuv3**2))/2) 
							st.write("La Posición Angular es: **{:.2f}**".format(θmcuv3), "<span style='color: red;'>**rad**</span>", unsafe_allow_html=True)
						
						if angaum2=="La rapidez angular disminuye":
							st.latex(r'''
								{\color{green}(\omega_f)} \Rightarrow {\color{red}\theta} = \omega_o \cdot t - \frac{\alpha \cdot t^2}{2}
								''')
							st.subheader("INGRESO DE DATOS")
							ωomcuv3 = st.number_input('Digite la rapidez angular inicial, en (rad/s)', 0.00, key=generate_widget_key("rapidez_angular3d"))
							αmcuv3 = st.number_input('Digite la aceleración angular, en (rad/s²)', 0.00, key=generate_widget_key("aceleración_angular3d"))
							tmcuv3 = st.number_input('Digite el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecangular3d"))
							θmcuv3 = (float(ωomcuv3)*float(tmcuv3)) - ((float(αmcuv3)*float(tmcuv3**2))/2) 
							st.write("La Posición Angular es: **{:.2f}**".format(θmcuv3), "<span style='color: red;'>**rad**</span>", unsafe_allow_html=True)
						
					tanguwrong=st.checkbox("La variable que no se toma en cuenta es (t)", value=False)
					if tanguwrong == True:
						angaum3=st.selectbox(" Variación para la rapidez angular: ", ("La rapidez angular aumenta", "La rapidez angular disminuye"))
						if angaum3=="La rapidez angular aumenta":
							st.latex(r'''
								{\color{green}(t)} \Rightarrow {\color{red}\omega^2_f} = \omega^2_o + 2 \cdot \alpha \cdot \theta
						   		''')
							st.subheader("INGRESO DE DATOS")
							ωomcuv4 = st.number_input('Digite la rapidez angular inicial, (rad/s)', 0.00, key=generate_widget_key("rapidez_angular4a"))
							αmcuv4 = st.number_input('Digite la aceleración angular, (rad/s²)', 0.01, key=generate_widget_key("aceleración_angular4a"))
							θmcuv4 = st.number_input('Digite la posición angular, (rad)', 0.0001, key=generate_widget_key("posición_angular4a"))
							ωfmcuv4 = math.sqrt(float(ωomcuv4**2) + (2 * float(αmcuv4) * float(θmcuv4)))
							st.write("La Rapidez Angular Final es: **{:.2f}**".format(ωfmcuv4), "<span style='color: red;'>**rad/s**</span>", unsafe_allow_html=True)
						if angaum3=="La rapidez angular disminuye":
							st.latex(r'''
								{\color{green}(t)} \Rightarrow {\color{red}\omega^2_f} = \omega^2_o - 2 \cdot \alpha \cdot \theta
						   		''')
							st.subheader("INGRESO DE DATOS")
							ωomcuv4 = st.number_input('Digite la rapidez angular inicial, (rad/s)', 0.00, key=generate_widget_key("rapidez_angular4d"))
							αmcuv4 = st.number_input('Digite la aceleración angular, (rad/s²)', 0.01, key=generate_widget_key("aceleración_angular4d"))
							θmcuv4 = st.number_input('Digite la posición angular, (rad)', 0.0001, key=generate_widget_key("posición_angular4d"))

							cocientemcuv = 2 * αmcuv4 * θmcuv4
							cocienteωomcuv4 = ωomcuv4 ** 2

							if cocientemcuv > cocienteωomcuv4:
							    st.write("La multiplicación de (2*α*θ) debe ser menor o igual que (<=) ωo². No existe la raíz cuadrada de un número negativo")
							else:
							    ωfmcuv4 = math.sqrt(cocienteωomcuv4 - cocientemcuv)
							    st.write("La Rapidez Angular Final es: **{:.2f}**".format(ωfmcuv4), "<span style='color: red;'>**rad/s**</span>", unsafe_allow_html=True)

				with tab2:

					L2wrong=st.checkbox("La variable que no se toma en cuenta es (L)", value=False)
					if L2wrong == True:
						taum1=st.selectbox(" Variación de la rapidez tangencial: ", ("La rapidez tangencial aumenta", "La rapidez tangencial disminuye"))
						if taum1=="La rapidez tangencial aumenta":
							st.latex(r'''
								{\color{green}(L)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o + a_T \cdot t
						   		''')
							st.subheader("INGRESO DE DATOS")
							votmcuv = st.number_input('Ingrese la rapidez tangencial inicial, en (m/s)', 0.00, key=generate_widget_key("rapidez_tangencial1a"))
							atmcuv = st.number_input('Ingrese la aceleración tangencial, en (m/s²)', 0.01, key=generate_widget_key("aceleración_tangencial1a"))
							ttmcuv = st.number_input('Ingrese el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ectangencial1a"))
							vftmcuv = float(votmcuv) + (float(atmcuv)*float(ttmcuv)) 
							st.write("La Rapidez Tangencial Final es: **{:.2f}**".format(vftmcuv), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
						if taum1=="La rapidez tangencial disminuye":
							st.latex(r'''
								{\color{green}(L)} \Rightarrow {\color{red}\upsilon_f} = \upsilon_o - a_T \cdot t
						   		''')
							st.subheader("INGRESO DE DATOS")
							votmcuv = st.number_input('Ingrese la rapidez tangencial inicial, en (m/s)', 0.00, 0.00, key=generate_widget_key("rapidez_tangencial1d"))
							atmcuv = st.number_input('Ingrese la aceleración tangencial, en (m/s²)', 0.01, key=generate_widget_key("aceleración_tangencial1d"))
							ttmcuv = st.number_input('Ingrese el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ectangencial1d"))
							vftmcuv = float(votmcuv) - (float(atmcuv)*float(ttmcuv)) 
							st.write("La Rapidez Tangencial Final es: **{:.2f}**".format(vftmcuv), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					
					atwrong=st.checkbox("La variable que no se toma en cuenta es (aT)", value=False)
					if atwrong == True:
						st.latex(r'''
							{\color{green}(a_T)} \Rightarrow {\color{red}L} = (\frac{\upsilon_o + \upsilon_f}{2}) \cdot t
							''')
						st.subheader("INGRESO DE DATOS")
						votmcuv2 = st.number_input('Ingrese la rapidez tangencial inicial, (m/s)', 0.00, key=generate_widget_key("rapidez_tangencial2a"))
						vftmcuv2 = st.number_input('Ingrese la rapidez tangencial final, (m/s)', 0.01, key=generate_widget_key("rapidezf_tangencial2a"))
						ttmcuv2 = st.number_input('Ingrese el tiempo, (s)', 0.0001, key=generate_widget_key("tiempo_ectangencial2a"))
						Ltmcuv2 = ((float(votmcuv2) + float(vftmcuv2))/2) * float(ttmcuv2) 
						st.write("La Longitud de arco es: **{:.2f}**".format(Ltmcuv2), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						
					vtwrong=st.checkbox("La variable que no se toma en cuenta es (𝑣f)", value=False)
					if vtwrong == True:
						taum2=st.selectbox(" Variación en la rapidez tangencial: ", ("La rapidez tangencial aumenta", "La rapidez tangencial disminuye"))
						if taum2=="La rapidez tangencial aumenta":
							st.latex(r'''
								{\color{green}(\upsilon_f)} \Rightarrow {\color{red}L} = \upsilon_o \cdot t + \frac{a_T \cdot t^2}{2}
								''')
							st.subheader("INGRESO DE DATOS")
							votmcuv3 = st.number_input('Digite la rapidez tangencial inicial, en (m/s)', 0.00, key=generate_widget_key("rapidez_tangencial3a"))
							atmcuv3 = st.number_input('Digite la aceleración tangencial, en (m/s²)', 0.01, key=generate_widget_key("aceleración_tangencial3a"))
							ttmcuv3 = st.number_input('Digite el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ectangencial3a"))
							Ltmcuv3 = (float(votmcuv3)*float(ttmcuv3)) + ((float(atmcuv3)*float(ttmcuv3**2))/2) 
							st.write("La Longitud de arco es: **{:.2f}**".format(Ltmcuv3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						
						if taum2=="La rapidez tangencial disminuye":
							st.latex(r'''
								{\color{green}(\upsilon_f)} \Rightarrow {\color{red}L} = \upsilon_o \cdot t - \frac{a_T \cdot t^2}{2}
								''')
							st.subheader("INGRESO DE DATOS")
							votmcuv3 = st.number_input('Digite la rapidez tangencial inicial, en (m/s)', 0.00, key=generate_widget_key("rapidez_tangencial3d"))
							atmcuv3 = st.number_input('Digite la aceleración tangencial, en (m/s²)', 0.01, key=generate_widget_key("aceleración_tangencial3d"))
							ttmcuv3 = st.number_input('Digite el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ectangencial3d"))
							Ltmcuv3 = (float(votmcuv3)*float(ttmcuv3)) - ((float(atmcuv3)*float(ttmcuv3**2))/2) 
							st.write("La Longitud de arco es: **{:.2f}**".format(Ltmcuv3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						
					ttuwrong=st.checkbox("La variable a no tomar en cuenta es (t)", value=False)
					if ttuwrong == True:
						taum3=st.selectbox(" Variación para la tangencial angular: ", ("La rapidez tangencial aumenta", "La rapidez tangencial disminuye"))
						if taum3=="La rapidez tangencial aumenta":
							st.latex(r'''
								{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o + 2 \cdot a_T \cdot L
						   		''')
							st.subheader("INGRESO DE DATOS")
							votmcuv4 = st.number_input('Digite la rapidez tangencial inicial, (m/s)', 0.00, key=generate_widget_key("rapidez_tangencial4a"))
							atmcuv4 = st.number_input('Digite la aceleración tangencial, (m/s²)', 0.01, key=generate_widget_key("aceleración_tangencial4a"))
							Ltmcuv4 = st.number_input('Digite la longitud de arco, (m)', 0.0001, key=generate_widget_key("longitud_tangencial4a"))
							vftmcuv4 = math.sqrt(float(votmcuv4**2) + (2 * float(atmcuv4) * float(Ltmcuv4)))
							st.write("La Rapidez Tangencial Final es: **{:.2f}**".format(vftmcuv4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
						if taum3=="La rapidez tangencial disminuye":
							st.latex(r'''
								{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_f} = \upsilon^2_o - 2 \cdot a_T \cdot L
						   		''')
							st.subheader("INGRESO DE DATOS")
							votmcuv4 = st.number_input('Digite la rapidez tangencial inicial, (m/s)', 0.00, key=generate_widget_key("rapidez_tangencial4d"))
							atmcuv4 = st.number_input('Digite la aceleración tangencial, (m/s²)', 0.01, key=generate_widget_key("aceleración_tangencial4d"))
							Ltmcuv4 = st.number_input('Digite la longitud de arco, (m)', 0.0001, key=generate_widget_key("longitud_tangencial4d"))

							cocientetmcuv = 2 * atmcuv4 * Ltmcuv4
							cocientevotmcuv4 = votmcuv4 ** 2

							if cocientetmcuv > cocientevotmcuv4:
								st.write("La multiplicación de (2 . aT . L) debe ser menor o igual que (<=) 𝑣o². No existe la raíz cuadrada de un número negativo")
							else:
								vftmcuv4 = math.sqrt(cocientevotmcuv4 - cocientetmcuv)
								st.write("La Rapidez Tangencial Final es: **{:.2f}**".format(vftmcuv4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
	
	if MENU2 == "Mov. Parabólico":	
		movpar=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if movpar=="Teoría":	
			st.latex(r'''
					\text{La trayectoria que describen los proyectiles es una curva llamada parábola. }  
			  		''')
			st.latex(r'''
					\text{Los proyectiles se mueven únicamente bajo la influencia de la gravedad una vez que son liberados. }  
			  		''')
			st.latex(r'''
					{\color{red}\text{Es un movimiento compuesto por:}}
			   		''')
			st.latex(r'''
					\text{En la dirección horizontal: } {\color{red}\text{ MRU}} \Rightarrow {\color{blue}\upsilon_x = \text{constante}}
			   		''')
			st.latex(r'''
					\text{En la dirección vertical: } {\color{red}\text{ MVCL}} \Rightarrow {\color{blue}\upsilon_y = \text{cambia}}
			   		''')
			st.latex(r'''
					{\color{red}\text{FORMULARIO }} {\color{red}(Movimiento \quad Horizontal)} 
			   		''')
			st.latex(r'''
					{\color{red}\text{ d}} = \upsilon_ox \cdot t
			   		''')
			st.latex(r'''
					{\color{red}\text{FORMULARIO }} {\color{red}(Movimiento \quad Vertical)}
			   		''')
			st.latex(r'''
						\text{El móvil baja }{\color{blue}(+)}  \text{ El móvil sube }{\color{blue}(-)}
				   		''')
			st.latex(r'''
					{\color{green}(h)} \Rightarrow {\color{red}\upsilon_{fy}} = \upsilon_{oy} \pm g \cdot t
			   		''')
			st.latex(r'''
					{\color{green}(g)} \Rightarrow {\color{red}h} = (\frac{\upsilon_{oy} + \upsilon_{fy}}{2}) \cdot t
			   		''')
			st.latex(r'''
					{\color{green}(\upsilon_{fy})} \Rightarrow {\color{red}h} = \upsilon_{oy} \cdot t \pm \frac{g \cdot t^2}{2}
			   		''')
			st.latex(r'''
					{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_{fy}} = \upsilon^2_{oy} \pm 2 \cdot g \cdot h
			   		''')
			st.latex(r'''
					\text{NOTA: La variable con color verde significa que es la que no se toma en cuenta en el ejercicio, como: }  
					''')
			st.latex(r'''
					{\color{green}(h) , (g), (\upsilon_{fy}), (t)} 
			   		''')
			st.text("DONDE:")
			st.latex(r'''
					{\color{red}h} = \text{ Altura, (m)}  
			   		''')
			st.latex(r'''
					{\color{red}\upsilon_{oy}} = \text{ Rapidez inicial en el eje y, (m/s)}  
			   		''')
			st.latex(r'''
					{\color{red}\upsilon_{fy}} = \text{ Rapidez final en el eje y, (m/s)}  
			   		''')
			st.latex(r'''
					{\color{red}g} = \text{ Gravedad: 9.8 (m/s²)}  
			   		''')
			st.latex(r'''
					{\color{red}t} = \text{ Tiempo, (s)}  
			   		''')

		if movpar=="Ejercicio Práctico":	
			def generate_widget_key(name):
					return f"{name}_{id(name)}"		
			tabpar1, tabpar2 = st.tabs(["Movimiento Horizontal","Movimiento Vertical"])
			with tabpar1:	
				st.latex(r'''
						{\color{red}d} = \upsilon_{ox} \cdot t
						''')
				st.subheader("INGRESO DE DATOS")
				vxmparabólico = st.number_input('Ingrese la rapidez en el eje x, (m/s)', 0.00, key=generate_widget_key("rapidez_parabólico0s"))
				tvuelomparabólico = st.number_input('Ingrese el tiempo, (s)', 0.0001, key=generate_widget_key("tiempo_ecparabólico0s"))
				dmparabólico = float(vxmparabólico)* float(tvuelomparabólico) 
				st.write("La distancia recorrida es: **{:.2f}**".format(dmparabólico), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
			with tabpar2:
				hpar=st.checkbox("La variable a no tomar en cuenta es (h)", value=False)
				if hpar == True:
					paraum1=st.selectbox(" Sentido de rapidez del móvil: ", ("El móvil sube", "El móvil baja"))
					if paraum1=="El móvil sube":
						st.latex(r'''
							{\color{green}(h)} \Rightarrow {\color{red}\upsilon_{fy}} = \upsilon_{oy} + g \cdot t
					   		''')
						st.subheader("INGRESO DE DATOS")
						votmp = st.number_input('Ingrese la rapidez inicial en el eje y, en (m/s)', 0.00, key=generate_widget_key("rapidez_par1s"))
						ttmp = st.number_input('Ingrese el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecpar1s"))
						vftmp = float(votmp) + (9.8*float(ttmp)) 
						st.write("La Rapidez Final en el eje y es: **{:.2f}**".format(vftmp), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					if paraum1=="El móvil baja":
						st.latex(r'''
							{\color{green}(h)} \Rightarrow {\color{red}\upsilon_{fy}} = \upsilon_{oy} - g \cdot t
					   		''')
						st.subheader("INGRESO DE DATOS")
						votmp = st.number_input('Ingrese la rapidez inicial en el eje y, en (m/s)', 0.00, key=generate_widget_key("rapidez_par1b"))
						ttmp = st.number_input('Ingrese el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecpar1b"))
						vftmp = float(votmp) - (9.8*float(ttmp)) 
						st.write("La Rapidez Final en el eje y es: **{:.2f}**".format(vftmp), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				
				gpar=st.checkbox("La variable a no tomar en cuenta es (g)", value=False)
				if gpar == True:
					st.latex(r'''
						{\color{green}(g)} \Rightarrow {\color{red}h} = (\frac{\upsilon_{oy} + \upsilon_{fy}}{2}) \cdot t
						''')
					st.subheader("INGRESO DE DATOS")
					votmp2 = st.number_input('Ingrese la rapidez inicial en el eje y, (m/s)', 0.00, key=generate_widget_key("rapidez_par2s"))
					vftmp2 = st.number_input('Ingrese la rapidez final en el eje y, (m/s)', 0.01, key=generate_widget_key("rapidezf_par2s"))
					ttmp2 = st.number_input('Ingrese el tiempo, (s)', 0.0001, key=generate_widget_key("tiempo_ecpar2s"))
					htmp2 = ((float(votmp2) + float(vftmp2))/2) * float(ttmp2) 
					st.write("La altura es: **{:.2f}**".format(htmp2), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					
				vfypar=st.checkbox("La variable a no tomar en cuenta es (𝑣fy)", value=False)
				if vfypar == True:
					paraum2=st.selectbox(" Sentido en la rapidez del móvil: ", ("El móvil sube", "El móvil baja"))
					if paraum2=="El móvil sube":
						st.latex(r'''
							{\color{green}(\upsilon_{fy})} \Rightarrow {\color{red}h} = \upsilon_{oy} \cdot t + \frac{g \cdot t^2}{2}
							''')
						st.subheader("INGRESO DE DATOS")
						votmp3 = st.number_input('Digite la rapidez inicial en el eje y, en (m/s)', 0.00, key=generate_widget_key("rapidez_par3s"))
						ttmp3 = st.number_input('Digite el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecpar3s"))
						htmp3 = (float(votmp3)*float(ttmp3)) + ((9.8 *float(ttmp3**2))/2) 
						st.write("La altura es: **{:.2f}**".format(htmp3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
						
					if paraum2=="El móvil baja":
						st.latex(r'''
							{\color{green}(\upsilon_{fy})} \Rightarrow {\color{red}h} = \upsilon_{oy} \cdot t - \frac{g \cdot t^2}{2}
							''')
						st.subheader("INGRESO DE DATOS")
						votmp3 = st.number_input('Digite la rapidez inicial en el eje y, en (m/s)', 0.00, key=generate_widget_key("rapidez_par3b"))
						ttmp3 = st.number_input('Digite el tiempo, en (s)', 0.0001, key=generate_widget_key("tiempo_ecpar3b"))
						htmp3 = (float(votmp3)*float(ttmp3)) - ((9.8 *float(ttmp3**2))/2) 
						st.write("La altura es: **{:.2f}**".format(htmp3), "<span style='color: red;'>**m**</span>", unsafe_allow_html=True)
					
				tpar=st.checkbox("La variable a no tomar en cuenta es (t)", value=False)
				if tpar == True:
					paraum3=st.selectbox(" Sentido para la rapidez del móvil: ", ("El móvil sube", "El móvil baja"))
					if paraum3=="El móvil sube":
						st.latex(r'''
							{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_{fy}} = \upsilon^2_{oy} + 2 \cdot g \cdot h
					   		''')
						st.subheader("INGRESO DE DATOS")
						votmp4 = st.number_input('Digite la rapidez inicial en el eje y, (m/s)', 0.00, key=generate_widget_key("rapidez_par4s"))
						htmp4 = st.number_input('Digite la altura, (m)', 0.00, key=generate_widget_key("altura_par4s"))
						vftmp4 = math.sqrt(float(votmp4**2) + (2 * 9.8 * float(htmp4)))
						st.write("La Rapidez Final en el eje y es: **{:.2f}**".format(vftmp4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
					if paraum3=="El móvil baja":
						st.latex(r'''
							{\color{green}(t)} \Rightarrow {\color{red}\upsilon^2_{fy}} = \upsilon^2_{oy} - 2 \cdot g \cdot h
					   		''')
						st.subheader("INGRESO DE DATOS")
						votmp4 = st.number_input('Digite la rapidez inicial en el eje y, (m/s)', 0.00, key=generate_widget_key("rapidez_par4b"))
						htmp4 = st.number_input('Digite la altura, (m)', 0.00, key=generate_widget_key("altura_par4b"))
						cocientetmp = 2 * 9.8 * htmp4
						cocientevotmp4 = votmp4 ** 2
						if cocientetmp > cocientevotmp4:
							st.write("La multiplicación de (2 . g . h) debe ser menor o igual que (<=) 𝑣oy². No existe la raíz cuadrada de un número negativo")
						else:
							vftmp4 = math.sqrt(cocientevotmp4 - cocientetmp)
							st.write("La Rapidez Final en el eje y es: **{:.2f}**".format(vftmp4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
if selected == "Dinámica":
	st.title(f"{selected}")
	#st.subheader("1° BACHILLERATO")
	MENU3=st.sidebar.radio("Dinámica ",("Fuerzas","Leyes de Newton", "Fuerzas en el Mov. Circular", "Equilibrio de un sólido"))
	if MENU3 == "Fuerzas":	
		din=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if din=="Teoría":
			definiciondin=st.checkbox("DEFINICIÓN", value=False)
			if definiciondin == True:
				st.latex(r'''
						\text{Es una rama de la Física que estudia y analiza el movimiento de un cuerpo, con relación a las causas que lo generan.}
				   		''')
				st.latex(r'''
						\text{Es decir, la interacción de un cuerpo con otros que se encuentran a su alrededor.}
				   		''')

			fuerza=st.checkbox("FUERZA", value=False)
			if fuerza == True:
				st.latex(r'''
						\text{La interacción entre dos o más cuerpos es medida por esta magnitud. Existen varios tipos de fuerzas:}
				   		''')
				tabfuerza1, tabfuerza2, tabfuerza3, tabfuerza4, tabfuerza5 = st.tabs(["Peso","Normal","Fricción o rozamiento", "Elástica", "Tensión"])
				with tabfuerza1:	
					st.latex(r'''
							\text{Es la fuerza ejercida por la Tierra para atraer a todos los objetos hacia su centro.}
				   			''')
					st.latex(r'''
							\text{Su dirección es perpendicular a la horizontal, vertical hacia abajo.}
				   			''')
					st.latex(r'''
							{\color{red}\vec{Peso}} = m \cdot \vec{g}
				   			''')
					st.latex(r'''
							{\color{blue}m}: \text{Es la masa de un cuerpo.} 
					   		''')		
					st.latex(r'''
							{\color{blue}\vec{g}}: \text{Es la aceleración de la gravedad,} = {\color{blue} 9.8 } \text { m/s²}
					   		''')
					st.latex(r'''
							\text{Unidades en el S.I. }: {\color{red}[N]} 
					   		''')
				with tabfuerza2:	
					st.latex(r'''
							\text{Es la fuerza generada en el momento que dos cuerpos entran en contacto.}
				   			''')
					st.latex(r'''
							\text{Su dirección es perpendicular a las superficies en contacto.}
				   			''')
					st.latex(r'''
							\text{Se lo representa con: } {\color{red}N } \text{ , de Fuerza Normal }
				   			''')
					st.latex(r'''
							\text{Unidades en el S.I. }: {\color{red}[N]} 
					   		''')
				with tabfuerza3:	
					st.latex(r'''
							\text{Surge cuando dos cuerpos están en contacto y uno de ellos tiende a moverse o realmente se mueve en relación al otro.}
				   			''')
					st.latex(r'''
							\text{Su dirección es tangente a la superficies en contacto y su sentido es contrario al movimiento relativo.}
				   			''')
					st.latex(r'''
							{\color{red}\text{ Fuerza de rozamiento estática}}
				   			''')
					st.latex(r'''
							\text{Cuando un cuerpo tiende a moverse sobre otro}
				   			''')
					st.latex(r'''
							{\color{red}fr_{e}} = \mu_e \cdot N
				   			''')
					st.latex(r'''
							{\color{blue}\mu_e}: \text{Coeficiente de rozamiento estático} 
					   		''')		
					st.latex(r'''
							{\color{blue}N}: \text{Fuerza Normal entre los cuerpos en contacto} 
					   		''')
					st.latex(r'''
							{\color{red}\text{ Fuerza de rozamiento cinética}}
				   			''')
					st.latex(r'''
							\text{Cuando un cuerpo se mueve en relación a otro}
				   			''')
					st.latex(r'''
							{\color{red}fr_{c}} = \mu_c \cdot N
				   			''')
					st.latex(r'''
							{\color{blue}\mu_c}: \text{Coeficiente de rozamiento cinético} 
					   		''')		
					st.latex(r'''
							{\color{blue}N}: \text{Fuerza Normal entre los cuerpos en contacto} 
					   		''')
					st.latex(r'''
							\text{Unidades en el S.I. }: {\color{red}[N]} 
					   		''')
				with tabfuerza4:	
					st.latex(r'''
							\text{Es aquella que permite a un cuerpo restituirse a sus condiciones naturales.}
				   			''')
					st.latex(r'''
							\text{Su dirección va hacia la posición en que el resorte no está deformado.}
				   			''')
					st.latex(r'''
							{\color{red}F_e} = {\color{blue} - } k \cdot x
				   			''')
					st.latex(r'''
							{\color{blue}F_e}: \text{Fuerza de recuperación elástica} 
					   		''')		
					st.latex(r'''
							{\color{blue}k}: \text{Constante del resorte} 
					   		''')		
					st.latex(r'''
							{\color{blue}x}: \text{deformación} 
					   		''')
					st.latex(r'''
							{\color{blue}(-) }:\text{Indica que la fuerza de recuperación elástica tiene sentido opuesto al de la deformación (x).}
				   			''')
					
					st.latex(r'''
							\text{Unidades en el S.I. }: {\color{red}[N]} 
					   		''')

				with tabfuerza5:	
					st.latex(r'''
							\text{Es la fuerza de tracción que actúa en línea recta a lo largo de un elemento flexible (cuerda).}
				   			''')
					st.latex(r'''
							\text{La tensión de una cuerda se dirige a lo largo de la cuerda misma, desde un extremo hacia el otro.}
				   			''')
					st.latex(r'''
							\text{Se lo representa con: } {\color{red}T } \text{ , Tensión }
				   			''')
					st.latex(r'''
							\text{Unidades en el S.I. }: {\color{red}[N]} 
					   		''')
		if din=="Ejercicio Práctico":
			def generate2_widget_key(name):
					return f"{name}_{id(name)}"
			tabfuerzaej1, tabfuerzaej2, tabfuerzaej3, tabfuerzaej4 = st.tabs(["Peso","Normal","Fricción o rozamiento", "Elástica"])
			with tabfuerzaej1:
				st.latex(r'''
						{\color{red}\vec{Peso}} = m \cdot \vec{g}
				   		''')
				st.subheader("INGRESO DE DATOS")
				masa = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.00, key=generate2_widget_key("masa_fuerza"))
				Peso = float(masa) * 9.8 
				st.write("El Peso del cuerpo es: **{:.2f}**".format(Peso), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
			with tabfuerzaej2:
				st.latex(r'''
						{\color{red}N} = \frac{fr}{\mu}
				   		''')
				st.subheader("INGRESO DE DATOS")
				fr = st.number_input('Ingrese el valor de la Fuerza de fricción o rozamiento, (N)', 0.00, key=generate2_widget_key("fuerza_rozamiento1"))
				u = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento', 0.01, key=generate2_widget_key("coeficiente_rozamiento1"))
				Normal = float(fr) / float(u) 
				st.write("La Fuerza Normal es: **{:.2f}**".format(Normal), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
			with tabfuerzaej3:
				st.latex(r'''
						{\color{red}fr} = \mu \cdot N
				   		''')
				st.subheader("INGRESO DE DATOS")
				Normal2 = st.number_input('Ingrese el valor de la Fuerza Normal, (N)', 0.00, key=generate2_widget_key("normal_fuerza2"))
				u2 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento', 0.00, key=generate2_widget_key("coeficiente_rozamiento2"))
				fr2 = float(Normal2) * float(u2) 
				st.write("La Fuerza de Rozamiento o Fricción es: **{:.2f}**".format(fr2), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
			with tabfuerzaej4:
				st.latex(r'''
						{\color{red}F_e} = - k \cdot x
				   		''')
				st.subheader("INGRESO DE DATOS")
				kfe = st.number_input('Ingrese el valor de la constante del resorte, (N/m)', 0.00, key=generate2_widget_key("constante_fuerzaelastica"))
				xfe = st.number_input('Ingrese el valor de la deformación, (m)', 0.00, key=generate2_widget_key("deformacion_fuerzaelasticas"))
				Fe = - float(kfe) * float(xfe) 
				st.write("La Fuerza de Recuperación Elástica es: **{:.2f}**".format(Fe), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)

	if MENU3 == "Leyes de Newton":	
		ley=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if ley=="Teoría":
			primeraley=st.checkbox("Primera Ley de Newton", value=False)
			if primeraley == True:
				st.latex(r'''
						{\color{red}\text{Ley de la Inercia o Ley de Equilibrio}}
				   		''')
				st.latex(r'''
						\text{Cualquier objeto permanece en su estado de reposo o en movimiento rectilíneo uniforme (MRU), a menos que,}
				   		''')
				st.latex(r'''
						\text{sea forzado a cambiar ese estado debido a la acción de fuerzas externas que actúan sobre él.}
				   		''')
				st.latex(r'''
						\begin{aligned}
					    \sum \vec{F} &= 0 \\
					    \vec{a} &= 0
					    \end{aligned}
				   		''')
				st.latex(r'''
						\begin{aligned}
					    \sum F_x &= 0 \quad & \sum F_y &= 0
					    \end{aligned}
				   		''')
			segundaley=st.checkbox("Segunda Ley de Newton", value=False)
			if segundaley == True:
				st.latex(r'''
						{\color{red}\text{Ley de la Dinámica o Ley de la Fuerza}}
				   		''')
				st.latex(r'''
						\text{La aceleración de un objeto aumenta o disminuye en la misma proporción que la fuerza neta que actúa sobre él,}
				   		''')
				st.latex(r'''
						\text{pero se reduce si el objeto tiene una masa mayor.}
				   		''')
				st.latex(r'''
						\begin{aligned}
					    \vec{a} \quad {\color{red}\alpha} \quad \frac{\vec{F}}{m} & 
					    \end{aligned}
				   		''')
				st.latex(r'''
						\begin{aligned}
					    \vec{F} &=  m \cdot \vec{a} \\
					    {\color{blue}\text{Donde:}} & \\
					    \vec{a} &=  \text{ aceleración} \\
					    m &=  \text{ masa} \\
					    \vec{F} &=  \text{ Fuerza neta} 
					    \end{aligned}
				   		''')
			terceraley=st.checkbox("Tercera Ley de Newton", value=False)
			if terceraley == True:
				st.latex(r'''
						{\color{red}\text{Ley de la Acción y Reacción}}
				   		''')
				st.latex(r'''
						\text{Cuando dos objetos interactúan entre sí, la fuerza que el primer objeto ejerce sobre el segundo (acción) es igual en  }
				   		''')
				st.latex(r'''
						\text{magnitud y dirección a la que el segundo objeto ejerce sobre el primero (reacción), pero se dirige en sentido contrario.}
				   		''')
				st.latex(r'''
						\begin{aligned}
					    {\color{blue} \vec{F}_{B/A} = \vec{F}_{A/B} } & \\ 
					    \vec{F}_{B/A} \quad {\color{red}\rightarrow} \\
					    \vec{F}_{A/B} \quad {\color{red}\leftarrow} \\
					    \end{aligned}
				   		''')
			reglas=st.checkbox("Reglas para resolver problemas de dinámica", value=False)
			if reglas == True:
				st.latex(r'''
						{\color{red}\text{Se deben tomar en cuenta las siguientes reglas:}}
				   		''')
				st.latex(r'''
						\textbf{1. Identifica las fuerzas relevantes:}
						''')
				st.latex(r'''
						\text{ Analiza cuidadosamente todas las fuerzas que actúan sobre el objeto en cuestión.}
				   		''')
				st.latex(r'''
						\textbf{2. Dibuja un diagrama de cuerpo libre:}
						''')
				st.latex(r'''
						\text{ Representa el objeto a analizar como un punto y dibuja todas las fuerzas que actúan sobre él.}
				   		''')
				st.latex(r'''
						\textbf{3. Aplica la Segunda Ley de Newton:}
						''')
				st.latex(r'''
						\text{ Asegúrate de considerar la dirección y magnitud de la aceleración correctamente.}
				   		''')
				st.latex(r'''
						\textbf{4. Considera la acción y reacción:}
						''')
				st.latex(r'''
						\text{ Ten en cuenta ambas fuerzas al analizar el sistema.}
				   		''')
				st.latex(r'''
						\textbf{5. Usa unidades adecuadas: }
						''')
				st.latex(r'''
						\text{ Asegúrate de usar las unidades correctas para todas las magnitudes involucradas en el problema.}
				   		''')
				st.latex(r'''
						\textbf{6. Resuelve el problema paso a paso:}
						''')
				st.latex(r'''
						\text{ Divide el problema en etapas más sencillas y resuelve cada parte por separado. }
				   		''')
		if ley=="Ejercicio Práctico":
			def generate3_widget_key(name):
					return f"{name}_{id(name)}"
			tableyej1, tableyej2, tableyej3, tableyej4, tableyej5, tableyej6, tableyej7, tableyej8, tableyej9, tableyej10 = st.tabs(["Ejemplo 1","Ejemplo 2","Ejemplo 3", "Ejemplo 4", "Ejemplo 5", "Ejemplo 6", "Ejemplo 7", "Ejemplo 8", "Ejemplo 9", "Ejemplo 10"])
			with tableyej1:
				st.image(imagen14, width = 500)
				st.subheader("INGRESO DE DATOS")
				angulol1 = st.number_input('Ingrese el ángulo que forma la Fuerza con la horizontal, (°)', 0.00, key=generate3_widget_key("ángulo_ley1"))
				masal1 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate3_widget_key("masa_ley1"))
				Fuerzal1 = st.number_input('Ingrese el valor de la Fuerza, [N]', 0.00, key=generate3_widget_key("fuerza_ley1"))
				ul1 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento', 0.00, key=generate3_widget_key("coefroz_ley1"))
				Pesol1 = float(masal1) * 9.8 
				Nl1 = float(Pesol1) - float((Fuerzal1 *math.sin(math.radians(angulol1))))
				al1 =  (float((Fuerzal1 *math.cos(math.radians(angulol1)))) - float(ul1*Nl1))/ float(masal1)
				reglas=st.checkbox("Diagrama de Cuerpo Libre", value=False)
				if reglas == True:
					st.image(imagen15, width = 500)
				st.write("La aceleración con la que se mueve el cuerpo es: **{:.2f}**".format(al1), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)		
			with tableyej2:
				st.image(imagen16, width = 400)
				st.subheader("INGRESO DE DATOS")
				masal2 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate3_widget_key("masa_ley2"))
				Fuerzal2 = st.number_input('Ingrese el valor de la Fuerza, [N]', 0.00, key=generate3_widget_key("fuerza_ley2"))
				ul2 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento', 0.00, key=generate3_widget_key("coefroz_ley2"))
				Pesol2 = float(masal2) * 9.8 
				Nl2 = float(Fuerzal2)
				al2 =  (float(Pesol2) - float(ul2*Nl2))/ float(masal2)
				st.write("La aceleración con la que se mueve el cuerpo es: **{:.2f}**".format(al2), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
			with tableyej3:
				st.image(imagen17, width = 550)
				st.subheader("INGRESO DE DATOS")
				angulol3 = st.number_input('Ingrese el ángulo para el plano inclinado, (°)', 0.00, key=generate3_widget_key("ángulo_ley3"))
				masal3 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate3_widget_key("masa_ley3"))
				Pesol3 = float(masal3) * 9.8 
				Nl3 = float(Pesol3)*float(math.sin(math.radians(angulol3)))
				ul3 = float(math.tan(math.radians(angulol3)))
				st.write("El coeficiente de rozamiento entre el bloque y el plano inclinado es: **{:.2f}**".format(ul3), unsafe_allow_html=True)		
			with tableyej4:
				st.image(imagen18, width = 350)
				st.subheader("INGRESO DE DATOS")
				masa1l4 = st.number_input('Ingrese el valor de la masa del bloque 1, (kg)', 0.01, key=generate3_widget_key("masa1_ley4"))
				masa2l4 = st.number_input('Ingrese el valor de la masa del bloque 2, (kg)', 0.01, key=generate3_widget_key("masa2_ley4"))
				Peso1l4 = float(masa1l4) * 9.8 
				Peso2l4 = float(masa2l4) * 9.8 
				al4 =  (float(Peso2l4) - float(Peso1l4))/ (float(masa1l4)+float(masa2l4))
				Tl4 = (float(masa1l4)*float(al4)) + float(Peso1l4)
				st.write("La aceleración con la que se mueve el sistema es: **{:.2f}**".format(al4), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión en la cuerda es: **{:.2f}**".format(Tl4), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
			with tableyej5:
				st.image(imagen19, width = 450)
				st.markdown('<p style="color:red;">Nota: La masa de la polea es despreciable</p>', unsafe_allow_html=True)
				st.subheader("INGRESO DE DATOS")
				masa1l5 = st.number_input('Ingrese el valor de la masa del bloque 1, (kg)', 0.01, key=generate3_widget_key("masa1_ley5"))
				masa2l5 = st.number_input('Ingrese el valor de la masa del bloque 2, (kg)', 0.01, key=generate3_widget_key("masa2_ley5"))
				Peso1l5 = float(masa1l5) * 9.8 
				Peso2l5 = float(masa2l5) * 9.8 
				a1l5 =  (2*float(Peso2l5) - float(Peso1l5))/ (float(masa1l5)+ (4*float(masa2l5)))
				a2l5 = 2*float(a1l5)
				T1l5 = (float(masa1l5)*float(a1l5)) + float(Peso1l5)
				T2l5 = float(T1l5)/2
				st.write("La aceleración con la que se mueve el bloque 1 es: **{:.2f}**".format(a1l5), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La aceleración con la que se mueve el bloque 2 es: **{:.2f}**".format(a2l5), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión 1 es: **{:.2f}**".format(T1l5), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
				st.write("La Tensión 2 es: **{:.2f}**".format(T2l5), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
			with tableyej6:
				st.image(imagen20, width = 550)
				st.subheader("INGRESO DE DATOS")
				masa1l6 = st.number_input('Ingrese el valor de la masa del bloque 1, (kg)', 0.01, key=generate3_widget_key("masa1_ley6"))
				masa2l6 = st.number_input('Ingrese el valor de la masa del bloque 2, (kg)', 0.01, key=generate3_widget_key("masa2_ley6"))
				ul6 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento', 0.00, key=generate3_widget_key("coefroz_ley6"))
				Peso1l6 = float(masa1l6) * 9.8 
				Peso2l6 = float(masa2l6) * 9.8 
				Nl6 = float(Peso1l6)
				frl6 = float(ul6)*float(Nl6)
				al6 =  (float(Peso2l6) - float(frl6))/ (float(masa1l6)+ float(masa2l6))
				Tl6 = (float(masa1l6)*float(al6)) + float(frl6)
				st.write("La aceleración con la que se mueve el sistema es: **{:.2f}**".format(al6), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión en la cuerda es: **{:.2f}**".format(Tl6), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
			with tableyej7:
				st.image(imagen21, width = 650)
				st.subheader("INGRESO DE DATOS")
				masa1l7 = st.number_input('Ingrese el valor de la masa del bloque 1, (kg)', 0.01, key=generate3_widget_key("masa1_ley7"))
				masa2l7 = st.number_input('Ingrese el valor de la masa del bloque 2, (kg)', 0.01, key=generate3_widget_key("masa2_ley7"))
				angulo1l7 = st.number_input('Ingrese el ángulo 𝛼1 de inclinación, (°)', 0.00, key=generate3_widget_key("ángulo1_ley7"))
				angulo2l7 = st.number_input('Ingrese el ángulo 𝛼2 de inclinación, (°)', 0.00, key=generate3_widget_key("ángulo2_ley7"))
				u1l7 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento entre el bloque 1 y la superficie', 0.00, key=generate3_widget_key("coefroz1_ley7"))
				u2l7 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento entre el bloque 2 y la superficie', 0.00, key=generate3_widget_key("coefroz2_ley7"))
				Peso1l7 = float(masa1l7) * 9.8 
				Peso1xl7 = float(Peso1l7)*float(math.sin(math.radians(angulo1l7)))
				Peso1yl7 = float(Peso1l7)*float(math.cos(math.radians(angulo1l7)))
				Peso2l7 = float(masa2l7) * 9.8 
				Peso2xl7 = float(Peso2l7)*float(math.sin(math.radians(angulo2l7)))
				Peso2yl7 = float(Peso2l7)*float(math.cos(math.radians(angulo2l7)))
				N1l7 = float(Peso1yl7)
				N2l7 = float(Peso2yl7)
				fr1l7 = float(u1l7)*float(N1l7)
				fr2l7 = float(u2l7)*float(N2l7)
				al7 =  (float(Peso2xl7) - float(Peso1xl7) - float(fr1l7) - float(fr2l7))/ (float(masa1l7)+ float(masa2l7))
				Tl7 = (float(masa1l7)*float(al7)) + float(Peso1xl7) + float(fr1l7)
				st.write("La aceleración con la que se mueve el sistema es: **{:.2f}**".format(al7), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión en la cuerda es: **{:.2f}**".format(Tl7), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
			with tableyej8:
				st.image(imagen22, width = 650)
				st.subheader("INGRESO DE DATOS")
				masa1l8 = st.number_input('Ingrese el valor de la masa del bloque 1, (kg)', 0.01, key=generate3_widget_key("masa1_ley8"))
				masa2l8 = st.number_input('Ingrese el valor de la masa del bloque 2, (kg)', 0.01, key=generate3_widget_key("masa2_ley8"))
				masa3l8 = st.number_input('Ingrese el valor de la masa del bloque 3, (kg)', 0.01, key=generate3_widget_key("masa3_ley8"))
				ul8 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento entre el bloque 2 y la superficie', 0.00, key=generate3_widget_key("coefroz_ley8"))
				Peso1l8 = float(masa1l8) * 9.8 
				Peso2l8 = float(masa2l8) * 9.8 
				Peso3l8 = float(masa3l8) * 9.8 
				Nl8 = float(Peso2l8)
				frl8 = float(ul8)*float(Nl8)
				al8 =  (float(Peso3l8) - float(Peso1l8) - float(frl8))/ (float(masa1l8)+ float(masa2l8)+float(masa3l8))
				T1l8 = (float(masa1l8)*float(al8)) + float(Peso1l8)
				T2l8 = float(Peso3l8) - (float(masa3l8)*float(al8)) 
				st.write("La aceleración con la que se mueve el sistema es: **{:.2f}**".format(al8), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión 1 es: **{:.2f}**".format(T1l8), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)		
				st.write("La Tensión 2 es: **{:.2f}**".format(T2l8), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
			with tableyej9:
				st.image(imagen23, width = 650)
				st.subheader("INGRESO DE DATOS")
				masa1l9 = st.number_input('Ingrese el valor de la masa del bloque 1, (kg)', 0.01, key=generate3_widget_key("masa1_ley9"))
				masa2l9 = st.number_input('Ingrese el valor de la masa del bloque 2, (kg)', 0.01, key=generate3_widget_key("masa2_ley9"))
				masa3l9 = st.number_input('Ingrese el valor de la masa del bloque 3, (kg)', 0.01, key=generate3_widget_key("masa3_ley9"))
				ul9 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento entre el bloque 2 y la superficie', 0.00, key=generate3_widget_key("coefroz_ley9"))
				angulol9 = st.number_input('Ingrese el ángulo 𝛼 de inclinación, (°)', 0.00, key=generate3_widget_key("ángulo_ley9"))
				Peso1l9 = float(masa1l9) * 9.8 
				Peso2l9 = float(masa2l9) * 9.8 
				Peso2xl9 = float(Peso2l9)*float(math.sin(math.radians(angulol9)))
				Peso2yl9 = float(Peso2l9)*float(math.cos(math.radians(angulol9)))
				Peso3l9 = float(masa3l9) * 9.8 
				Nl9 = float(Peso2yl9)
				frl9 = float(ul9)*float(Nl9)
				al9 =  (float(Peso3l9) + float(Peso2xl9) - float(Peso1l9) - float(frl9))/ (float(masa1l9)+ float(masa2l9)+float(masa3l9))
				T1l9 = (float(masa1l9)*float(al9)) + float(Peso1l9)
				T2l9 = float(Peso3l9) - (float(masa3l9)*float(al9)) 
				st.write("La aceleración con la que se mueve el sistema es: **{:.2f}**".format(al9), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión 1 es: **{:.2f}**".format(T1l9), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)		
				st.write("La Tensión 2 es: **{:.2f}**".format(T2l9), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)		
			with tableyej10:
				st.image(imagen24, width = 650)
				st.markdown('<p style="color:red;">Nota: La masa de la polea es despreciable</p>', unsafe_allow_html=True)
				st.subheader("INGRESO DE DATOS")
				masa1l10 = st.number_input('Ingrese el valor de la masa del bloque A, (kg)', 0.01, key=generate3_widget_key("masa1_ley10"))
				masa2l10 = st.number_input('Ingrese el valor de la masa del bloque B, (kg)', 0.01, key=generate3_widget_key("masa2_ley10"))
				ul10 = st.number_input('Ingrese el valor del coeficiente de fricción o rozamiento entre el bloque A y la superficie', 0.00, key=generate3_widget_key("coefroz_ley10"))
				angulol10 = st.number_input('Ingrese el ángulo 𝛼 de inclinación, (°)', 0.00, key=generate3_widget_key("ángulo_ley10"))
				Peso1l10 = float(masa1l10) * 9.8 
				Peso2l10 = float(masa2l10) * 9.8 
				Peso1xl10 = float(Peso1l10)*float(math.sin(math.radians(angulol10)))
				Peso1yl10 = float(Peso1l10)*float(math.cos(math.radians(angulol10)))
				Nl10 = float(Peso1yl10)
				frl10 = float(ul10)*float(Nl10)
				a2l10 =  ((2*float(Peso1xl10)) - float(Peso2l10) - (2*float(frl10)))/ (float(masa2l10)+ (4*float(masa1l10)))
				a1l10 = 2*float(a2l10)
				T2l10 = (float(masa2l10)*float(a2l10)) + float(Peso2l10)
				T1l10 = float(T2l10)/2
				st.write("La aceleración con la que se mueve el bloque A es: **{:.2f}**".format(a1l10), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La aceleración con la que se mueve el bloque B es: **{:.2f}**".format(a2l10), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)
				st.write("La Tensión del boque A es: **{:.2f}**".format(T1l10), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)
				st.write("La Tensión del boque B es: **{:.2f}**".format(T2l10), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)

	if MENU3 == "Fuerzas en el Mov. Circular":	
		fmc=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if fmc=="Teoría":
			st.latex(r'''
					\text{En un movimiento circular, el sistema dinámico de la partícula es formado por los ejes radial y tangencial.}
			   		''')
			st.image(imagen25, width = 650, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 207")
			st.latex(r'''
					{\color{red}\text{𝐸𝑗𝑒 𝑁𝑜𝑟𝑚𝑎𝑙 (𝑅𝑎𝑑𝑖𝑎𝑙)}}
			   		''')
			st.latex(r'''
					\text{Se encuentra en el mismo plano del movimiento, atraviesa la posición de la partícula en el momento analizado, }
			   		''')
			st.latex(r'''
					\text{y también pasa por el centro del círculo. Su dirección es positiva, apuntando hacia el centro de la curva.}
			   		''')
			st.latex(r'''
					{\color{red}\text{𝐸𝑗𝑒 𝑇𝑎𝑛𝑔𝑒𝑛𝑐𝑖𝑎𝑙}}
			   		''')
			st.latex(r'''
					\text{Se encuentra en el mismo plano del movimiento y forma un ángulo de 90 grados con el eje central.}
			   		''')
			st.latex(r'''
					\text{Su dirección positiva es aquella que coincide con la dirección del movimiento.}
			   		''')
			st.latex(r'''
					{\color{red}\text{Aplicación de la Segunda Ley de Newton}}
			   		''')

			st.latex(r'''
					\begin{aligned}
				    \sum \vec{F} &= m \cdot \vec{a} \Rightarrow  \vec{a} = \vec{a}_T + \vec{a}_c \\
				    \sum \vec{F} &= m (\vec{a}_T + \vec{a}_c) \\
				    \sum \vec{F} &= m \cdot \vec{a}_T + m \cdot \vec{a}_c \\
				    \sum \vec{F} &= \sum \vec{F}_T + \sum \vec{F}_c
				    \end{aligned}
			   		''')
			tablefmc1, tablefmc2, tablefmc3 = st.tabs(["Fuerza Tangencial","Fuerza Centrípeta","Fuerza Axial"])
			with tablefmc1:
				st.latex(r'''
					\text{Es la parte de la fuerza neta que actúa en la dirección tangencial, provocando en la partícula una aceleración tangencial, }
			   		''')
				st.latex(r'''
					\text{y siendo responsable de cambiar la magnitud de su velocidad.}
			   		''')
				st.latex(r'''
						\begin{aligned}
					    \sum \vec{F}_T &= m \cdot \vec{a}_T \\
					    \sum \vec{F}_T &= m \cdot \frac{\Delta \vec{\upsilon}}{\Delta t} \\
					    \sum F_T &= m \cdot \alpha \cdot R 
					    \end{aligned}
				   		''')
				st.text("DONDE:")
				st.latex(r'''
						{\color{red}m} = \text{ Masa, (kg)}  
				   		''')
				st.latex(r'''
						{\color{red}\alpha} = \text{ Aceleración angular, (rad/s²)}  
				   		''')
				st.latex(r'''
						{\color{red}R} = \text{ Radio, (m)}  
				   		''')
				st.latex(r'''
						{\color{red}t} = \text{ Tiempo, (s)}  
				   		''')
				st.latex(r'''
					{\color{red}\text{Fuerza tangencial es nula = 0}}
			   		''')
				st.latex(r'''
					\text{Si la velocidad angular es constante, es decir en un Movimiento Circular Uniforme.}
			   		''')
				st.latex(r'''
						\omega = constante \Rightarrow \vec{a}_T = 0
					    ''')
				st.latex(r'''
						\begin{aligned}
					    \sum \vec{F} &= \sum \vec{F}_T + \sum \vec{F}_c \\
					    \sum \vec{F} &= \sum \vec{F}_c 
					    \end{aligned}
				   		''')
				st.latex(r'''
					{\color{red}\text{Fuerza tangencial es diferente de 0}}
			   		''')
				st.latex(r'''
					\text{Si existe un cambio en la velocidad angular, es decir en un Movimiento Circular Uniformemente Variado.}
			   		''')
				st.latex(r'''
						\sum \vec{F} = \sum \vec{F}_T + \sum \vec{F}_c 
					    ''')
			with tablefmc2:
				st.latex(r'''
					\text{Es la parte de la fuerza neta que actúa en la dirección central, generando una aceleración centrípeta en la partícula, }
			   		''')
				st.latex(r'''
					\text{y siendo responsable de cambiar la dirección de su velocidad.}
			   		''')
				st.latex(r'''
						\begin{aligned}
					    \sum \vec{F}_c &= m \cdot \vec{a}_c \\
					    \sum \vec{F}_c &= m \cdot \frac{\upsilon²}{R} \\
					    \sum F_c &= m \cdot \omega² \cdot R 
					    \end{aligned}
				   		''')
				st.text("DONDE:")
				st.latex(r'''
						{\color{red}m} = \text{ Masa, (kg)}  
				   		''')
				st.latex(r'''
						{\color{red}\upsilon} = \text{ Rapidez tangencial, (m/s)}  
				   		''')
				st.latex(r'''
						{\color{red}\omega} = \text{ Rapidez angular, (rad/s)}  
				   		''')
				st.latex(r'''
						{\color{red}R} = \text{ Radio, (m)}  
				   		''')
				st.latex(r'''
					{\color{red}\text{Fuerza centrípeta es nula = 0}}
			   		''')
				st.latex(r'''
					\text{Si el movimiento es rectilíneo.}
			   		''')
				st.latex(r'''
						\begin{aligned}
					    \sum \vec{F} &= \sum \vec{F}_T + \sum \vec{F}_c \\
					    \sum \vec{F} &= \sum \vec{F}_T 
					    \end{aligned}
				   		''')
				st.latex(r'''
					{\color{red}\text{Fuerza centrípeta es diferente de 0}}
			   		''')
				st.latex(r'''
					\text{En cualquier movimiento circular.}
			   		''')
			with tablefmc3:
				st.latex(r'''
					\text{Debido a que el movimiento circular ocurre en un solo plano, la fuerza neta en la dirección perpendicular a ese plano es cero. }
			   		''')
				st.latex(r'''
					\text{Esta dirección se conoce como "axial" y suele representarse mediante el eje z.}
			   		''')
				st.latex(r'''
					\text{En esta dirección, no hay fuerza neta que afecte al movimiento circular.}
			   		''')
				st.latex(r'''
						\begin{aligned}
					    \sum \vec{F}_z &= m \cdot \vec{a}_z \\
					    \sum \vec{F}_z &= 0
					    \end{aligned}
				   		''')
				st.image(imagen26, width = 550, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 209")
		if fmc=="Ejercicio Práctico":
			def generate4_widget_key(name):
					return f"{name}_{id(name)}"
			tablefmcej1, tablefmcej2, tablefmcej3, tablefmcej4= st.tabs(["Ejemplo 1","Ejemplo 2","Ejemplo 3", "Ejemplo 4"])
			with tablefmcej1:
				st.latex(r'''
					{\color{red}\text{Fuerzas en el Movimiento Circular sobre un Plano Horizontal}}
			   		''')
				st.image(imagen27, width = 650)
				st.subheader("INGRESO DE DATOS")
				masafmc1 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate4_widget_key("masa_fmc1"))
				radiofmc1 = st.number_input('Ingrese el valor del radio de la circunferencia, (m)', 0.01, key=generate4_widget_key("radio_fmc1"))
				rangularfmc1 = st.number_input('Ingrese el valor del radio de la rapidez angular, (rad/s)', 0.01, key=generate4_widget_key("rangular_fmc1"))
				acfmc1 = (float(rangularfmc1)**2) * float(radiofmc1)
				vfmc1 =  float(rangularfmc1)*float(radiofmc1) 
				Fcfmc1 = float(masafmc1) * float(acfmc1)
				st.write("La aceleración centrípeta es: **{:.2f}**".format(acfmc1), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)		
				#st.write("La rapidez del cuerpo es: **{:.2f}**".format(vfmc1), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)
				st.write("La Fuerza centrípeta que actúa sobre el cuerpo es: **{:.2f}**".format(Fcfmc1), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
			with tablefmcej2:
				st.latex(r'''
					{\color{red}\text{Fuerzas en el Movimiento Circular sobre un Plano Vertical}}
			   		''')
				st.image(imagen28, width = 650)
				st.subheader("INGRESO DE DATOS")
				masafmc2 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate4_widget_key("masa_fmc2"))
				radiofmc2 = st.number_input('Ingrese la longitud del péndulo, (m)', 0.01, key=generate4_widget_key("radio_fmc2"))
				Tfmc2 = st.number_input('Ingrese el valor de la Tensión de la cuerda, ([N])', 0.02, key=generate4_widget_key("tensión_fmc2"))
				angulofmc2 = st.number_input('Ingrese el ángulo θ, (°)', 0.01, key=generate4_widget_key("ángulo_fmc2"))
				Pesoxfmc2 = float(masafmc2)*9.8*float(math.sin(math.radians(angulofmc2)))
				Pesoyfmc2 = float(masafmc2)*9.8*float(math.cos(math.radians(angulofmc2)))
				atfmc2 = float(Pesoxfmc2) / float(masafmc2)
				acfmc2 = (float(Tfmc2) - float(Pesoyfmc2)) / float(masafmc2)
				Fcfmc2 = float(masafmc2) * float(acfmc2)
				Ftfmc2 = float(masafmc2) * float(atfmc2)
				st.write("La aceleración tangencial es: **{:.2f}**".format(atfmc2), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)		
				st.write("La aceleración centrípeta es: **{:.2f}**".format(acfmc2), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)		
				st.write("La Fuerza tangencial que actúa sobre el cuerpo es: **{:.2f}**".format(Ftfmc2), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
				st.write("La Fuerza centrípeta que actúa sobre el cuerpo es: **{:.2f}**".format(Fcfmc2), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
			with tablefmcej3:
				st.latex(r'''
					{\color{red}\text{Fuerzas en el Movimiento Circular sobre un Plano Horizontal y Plano Axial (z)}}
			   		''')
				st.image(imagen29, width = 650)
				st.subheader("INGRESO DE DATOS")
				masafmc3 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate4_widget_key("masa_fmc3"))
				radiofmc3 = st.number_input('Ingrese la longitud del péndulo, (m)', 0.01, key=generate4_widget_key("radio_fmc3"))
				angulofmc3 = st.number_input('Ingrese el ángulo θ, (°)', 0.01, key=generate4_widget_key("ángulo_fmc3"))
				rfmc3 = float(radiofmc3)*float(math.sin(math.radians(angulofmc3)))
				Pesofmc3 = float(masafmc3)*9.8
				Tfmc3 = float(Pesofmc3)/float(math.cos(math.radians(angulofmc3)))
				Txfmc3 = float(Tfmc3)*float(math.sin(math.radians(angulofmc3)))
				Tyfmc3 = float(Tfmc3)*float(math.cos(math.radians(angulofmc3)))
				acfmc3 = float(Txfmc3) / float(masafmc3)
				Fcfmc3 = float(masafmc3) * float(acfmc3)
				st.write("La Tensión en la cuerda es: **{:.2f}**".format(Tfmc3), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
				st.write("La aceleración centrípeta es: **{:.2f}**".format(acfmc3), "<span style='color: red;'>**m/s²**</span>", unsafe_allow_html=True)		
				st.write("La Fuerza centrípeta que actúa sobre el cuerpo es: **{:.2f}**".format(Fcfmc3), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
			with tablefmcej4:
				st.latex(r'''
					{\color{red}\text{Fuerzas en el Movimiento Circular sobre un Plano Vertical (Velocidad mínima o crítica)}}
			   		''')
				st.latex(r'''
						\upsilon_{mínima} = \upsilon_{crítica} = \sqrt{g \cdot R} 
					    ''')
				st.image(imagen30, width = 650)
				st.subheader("INGRESO DE DATOS")
				masafmc4 = st.number_input('Ingrese el valor de la masa del cuerpo, (kg)', 0.01, key=generate4_widget_key("masa_fmc4"))
				radiofmc4 = st.number_input('Ingrese el radio de la circunferencia, (m)', 0.01, key=generate4_widget_key("radio_fmc4"))
				vpbfmc4 = st.number_input('Ingrese la rapidez en el punto más bajo, (m/s)', 0.01, key=generate4_widget_key("velocidad_fmc4"))
				Pesofmc4 = float(masafmc4)*9.8
				vmcfmc4 = float(math.sqrt(float(9.8*radiofmc4)))
				Tfmc4 = float(Pesofmc4) + (float(masafmc4)*float(vpbfmc4**2)/float(radiofmc4))
				st.write("La velocidad mínima es: **{:.2f}**".format(vmcfmc4), "<span style='color: red;'>**m/s**</span>", unsafe_allow_html=True)		
				st.write("La Tensión en la cuerda es: **{:.2f}**".format(Tfmc4), "<span style='color: red;'>**[N]**</span>", unsafe_allow_html=True)	
	if MENU3 == "Equilibrio de un sólido":	
		eqs=st.sidebar.selectbox(" ¿Qué te gustaría aprender? ", ("Teoría", "Ejercicio Práctico"))
		if eqs=="Teoría":
			st.latex(r'''
					\text{Si las fuerzas están aplicadas sobre un sólido rígido, los efectos en relación al movimiento pueden ser: }
			   		''')
			st.latex(r'''
					\bullet \text{Traslación} \quad \bullet\text{Rotación}
			   		''')
			st.latex(r'''
					{\color{red}\text{Torque o Momento de Fuerza}}
			   		''')
			st.latex(r'''
					\text{El torque o momento de fuerza es la fuerza responsable de producir la rotación de un objeto alrededor}
			   		''')
			st.latex(r'''
					\text{de un punto o eje específico, y depende tanto de la fuerza aplicada como de la distancia desde el punto de giro.}
			   		''')
			st.latex(r'''
					{\color{blue}\text{Cuanto mayor sea la fuerza y cuanto mayor sea la distancia al punto de giro, más fácil será que exista el una rotación.}}
			   		''')
			st.latex(r'''
					{\color{red}\vec{\tau}} = \vec{r} \times \vec{F} 
			   		''')
			st.text("DONDE:")
			st.latex(r'''
					{\color{red}\vec{\tau}} = \text{ Torque, ([N.m])}  
			   		''')
			st.latex(r'''
					{\color{red}\vec{r}} = \text{ Vector posición de un punto cualquiera de la línea de acción de la fuerza, (m)}  
			   		''')
			st.latex(r'''
					{\color{red}\vec{F}} = \text{ Fuerza aplicada al cuerpo, ([N])}  
			   		''')
			st.image(imagen31, width = 550, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 221")
			st.latex(r'''
					{\color{green}\text{Ecuación por definición del Torque}}
			   		''')
			st.latex(r'''
					{\color{red}\tau_o} = F \cdot r \cdot \sin{\theta} 
			   		''')
			st.latex(r'''
					{\color{green}\text{Ecuación calculando el brazo de palanca (d)}}
			   		''')
			st.latex(r'''
					{\color{red}\tau_o} = F \cdot d 
			   		''')
			tableeqs1, tableeqs2, tableeqs3 = st.tabs(["Condiciones de Equilibrio del Sólido","Reacciones en los apoyos","Reglas para resolver los problemas"])
			with tableeqs1:
				st.latex(r'''
						{\color{red}\text{1. La fuerza neta aplicada sobre el cuerpo debe ser nula:}}
			   			''')
				st.latex(r'''
						\text{No existe movimiento de traslación, ya que su velocidad inicial es 0.}
			   			''')
				st.latex(r'''
						\sum \vec{F} = 0
						''')
				st.latex(r'''
						{\color{red}\text{2. El torque neto evaluado en cualquier punto del cuerpo o sistema, debe ser nulo:}}
			   			''')
				st.latex(r'''
						\text{No existe movimiento de rotación, ya que su velocidad angular inicial es 0.}
			   			''')
				st.latex(r'''
						\sum \vec{\tau}_o = 0
						''')
				st.latex(r'''
						{\color{Blue}\text{Por lo tanto, como las fuerzas son coplanares, las ecuaciones a utilizarse serán:}}
			   			''')
				st.latex(r'''
						\sum {F}_x = 0
						''')
				st.latex(r'''
						\sum {F}_y = 0
						''')
				st.latex(r'''
						\sum \tau_o = 0
						''')
			with tableeqs2:
				st.latex(r'''
						{\color{red}\text{¿Hacia dónde apuntan las reacciones?}}
			   			''')
				st.latex(r'''
						\text{Primero, las reacciones siempre contrarrestan las otras fuerzas, de lo contrario,}
			   			''')
				st.latex(r'''
						\text{apuntan hacia la derecha en el eje "x" y hacia arriba en el eje "y".}
			   			''')
				st.latex(r'''
						{\color{blue}\text{Si la fuerza es +}} \Rightarrow \text{Sentido correcto}
			   			''')
				st.latex(r'''
						{\color{red}\text{Si la fuerza es -}} \Rightarrow \text{Sentido incorrecto, hay que cambiar de sentido}
			   			''')
				st.latex(r'''
						{\color{green}\text{Tipos de Reacciones}}
			   			''')
				contacto=st.checkbox("Contacto", value=False)
				if contacto == True:
					st.image(imagen32, width = 550, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 223")
				rodillo=st.checkbox("Rodillo", value=False)
				if rodillo == True:
					st.image(imagen33, width = 550, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 223")
				pasador=st.checkbox("Pasador", value=False)
				if pasador == True:
					st.image(imagen34, width = 550, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 223")
				empotramiento=st.checkbox("Empotramiento", value=False)
				if empotramiento == True:
					st.image(imagen35, width = 550, caption = "Fuente: Física Vectorial 1 Vallejo Zambrano, pg. 223")
			with tableeqs3:
				st.latex(r'''
						{\color{red}\text{Se deben tomar en cuenta las siguientes reglas:}}
				   		''')
				st.latex(r'''
						\textbf{1. Identifica el o los cuerpos de interés:}
						''')
				st.latex(r'''
						\text{ Analiza el o los objetos en cuestión.}
				   		''')
				st.latex(r'''
						\textbf{2. Representa gráficamente todas las fuerzas externas:}
						''')
				st.latex(r'''
						\text{ Dibuja las fuerzas que actúan sobre el objeto, por lo general son el peso y las generadas por los apoyos.}
				   		''')
				st.latex(r'''
						\textbf{3. Elige un sistema de referencia adecuado:}
						''')
				st.latex(r'''
						\text{ Asegúrate de tener un sistema de referencia óptimo, para que puedas descomponer las fuerzas aplicadas al sólido.}
				   		''')
				st.latex(r'''
						\textbf{4. Aplica las condiciones de equilibrio:}
						''')
				st.latex(r'''
						\sum {F}_x = 0 \quad ; \quad \sum {F}_y = 0 \quad ; \quad \sum \tau_o = 0
						''')
				st.latex(r'''
						\textbf{5. Resuelve el sistema de ecuaciones: }
						''')
				st.latex(r'''
						\text{ Segumaramente obtendrás un sistema de ecuaciones que permita calcular el valor de las diferentes incógnitas.}
				   		''')
		
		if eqs=="Ejercicio Práctico":
			def generate5_widget_key(name):
					return f"{name}_{id(name)}"		
			eqsej1=st.checkbox("Por definición del Torque", value=False)
			if eqsej1 == True:
				st.latex(r'''
						{\color{red}\tau_o} = F \cdot r \cdot \sin{\theta} 
				   		''')
				st.image(imagen36, width = 550)
				st.subheader("INGRESO DE DATOS")
				Fuerzaeqs1 = st.number_input('Ingrese el valor de la Fuerza, [N]', 0.01, key=generate5_widget_key("fuerza_eqs1"))
				mposeqs1 = st.number_input('Ingrese el valor del módulo del vector posición, (m)', 0.01, key=generate5_widget_key("posicion_eqs1"))
				anguloeqs1 = st.number_input('Ingrese el valor del ángulo que forma la fuerza con la horizontal, (°)', 0.01, key=generate5_widget_key("angulo_eqs1"))
				τeqs1 = float(Fuerzaeqs1) * float(mposeqs1)* float(math.sin(math.radians(anguloeqs1)))
				st.write("El Torque es: **{:.2f}**".format(τeqs1), "<span style='color: red;'>**[N.m]**</span>", unsafe_allow_html=True)	

			eqsej2=st.checkbox("Calculando el brazo de palanca", value=False)
			if eqsej2 == True:
				st.latex(r'''
						{\color{red}\tau_o} = F \cdot d 
				   		''')
				st.image(imagen37, width = 550)
				st.subheader("INGRESO DE DATOS")
				Fuerzaeqs2 = st.number_input('Ingrese el valor de la Fuerza, [N]', 0.01, key=generate5_widget_key("fuerza_eqs2"))
				deqs2 = st.number_input('Ingrese la distancia perpendicular a la línea de acción de la fuerza, (m)', 0.01, key=generate5_widget_key("distancia_eqs2"))
				τeqs2 = float(Fuerzaeqs2) * float(deqs2)
				st.write("El Torque es: **{:.2f}**".format(τeqs2), "<span style='color: red;'>**[N.m]**</span>", unsafe_allow_html=True)	
			

if selected == "Autor":
	#st.title(f"{selected}")
	st.subheader("Datos Personales:")
	st.latex(r'''
				\text{✉ santiago.arias.tt@gmail.com}
		   		''')
	st.latex(r'''
		    	\text{📱 +593 992998904}
		   		''')
	st.latex(r'''
		    	\text{💻 https://www.linkedin.com/in/santiagoariasbautista/}
		   		''')
		