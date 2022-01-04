s = " tacctggttg atcctgccag tagtcatatg cttgtctcaa agatgaagcc " # se ingresó la secuencia nucleotidica

t = s.replace(" ", "") # se reemplazo los espacios por sin espacio

if (len(s) - s.count(" ")) == len(t): # secuencia de control para saber si la union fue exitosa
   A = (t.count("a")/len(t))*100 # imprime porcentaje de adenina
   T = (t.count("t")/len(t))*100
   C = (t.count("c")/len(t))*100
   G = (t.count("g")/len(t))*100
   CG = C + G
else:
   print("tengo un error: ")

if A + T + C + G == 100:
   print(A, T, C, G, CG)
else:
   print("Error: ")

input("pulse enter para salir: ")
