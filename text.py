#!/usr/bin/env python
# coding: utf-8
import pyperclip, os
print('@johanPosada')

text = input('Insert the text here: ')

while text =='':
    text = input('Insert the text here: ')
    
def methods(arguments):
    
    switcher = {
        1: text.lower(),
        2: text.upper(),
        3: text.title(),
        4: text.swapcase(),
        5: text.capitalize()
    }
    
    return switcher.get(arguments) #La función methods toma su argumento el cual es la función que se le da en el switch-case


print('Choose one of this items by knowing the number:\n ')

#Se crea la variable arguments, en el cual el usuario elige el método a convertir el texto
arguments = {
    1: 'lowercase',
    2: 'uppercase',
    3: 'title: first each word letter to upper',
    4: 'swap-case',
    5: 'capitalize: first text letter to upper'
}

print(sorted(arguments.items()),' \n')

#Se crea un statement(bucle) en el que si el usuario no dijita algo lo vuelva a ejecutar
while True:
    try:
        arguments = int(input('Insert the the item number here: '))
     
    except ValueError:
        continue
    else:
        text = (methods(arguments)) #La funcion methods se muestra cuanto con el argumento que la persona le da, el texto ya es convertido
        print('Text has been copied to clipboard!:\n', text)
        break
        
pyperclip.copy(text)
exec_ = input('Do you want to continue? Y/n ~ ')
while exec_ == '':
    exec_ = input('Do you want to continue? Y/n ~ ')
else:
    if exec_ == 'Y' or exec_ == 'y':
        os.system('python3 text.py')
    else:
        print('See you later...')