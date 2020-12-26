#!/usr/bin/env python
# coding: utf-8
import pyperclip, os, signal, sys
print('@johanPosada')

def signal_handler(signal, frame):
    print('...Exiting...')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

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
    
    return switcher.get(arguments) 

print('Choose one of this items by knowing the number:\n ')

arguments = {
    1: 'lowercase',
    2: 'uppercase',
    3: 'title: first each word letter to upper',
    4: 'swap-case',
    5: 'capitalize: first text letter to upper'
}

print(sorted(arguments.items()),' \n')

while True:
    try:
        arguments = int(input('Insert the the item number here: '))
     
    except ValueError:
        continue
    else:
        text = (methods(arguments))
        print('Text has been copied to clipboard!:\n', text,'\n')
        break
        
pyperclip.copy(text)
exec_ = input('Do you want to continue? Y/n ~ ')
while exec_ == '':
    exec_ = input('Do you want to continue? Y/n ~ ')
else:
    if exec_ == 'Y' or exec_ == 'y':
        os.system('python3 ' + __file__)
    else:
        print('See you later...')
