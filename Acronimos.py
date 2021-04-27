#Un acrónimo es una forma corta de una palabra, creada usando la primera letra de cada palabra de una frase.

frase = str(input("Ingrese una frase para obtener su acrónimo"))
#Uso split para separar la frase en palabras
texto = frase.split()
#Con un for recorro cada palabra y guardo en a sólo el caracter que se encuentra en el indice 0.
# Con el método upper lo convierto en mayúsculas
a = " "
for i in texto:
    a = a+str(i[0]).upper()
print(a)
