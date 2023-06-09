#funtion input -> retorna string 
name = input('Como te llamas? \n')
age = int(input('Cuantos años tienes? \n'))
future= int(input('cuantos años mas?\n'))

print("Hola" + name)
print("En" +  str(future) + "años tendras"+ str (age + future))

#Format String 
"""
Hola Zueyma, en 3 años tendras 22 años
"""
text_complete = "Hola {}, en {} años tendras {} años"
print(text_complete.format(name, future,age + future))