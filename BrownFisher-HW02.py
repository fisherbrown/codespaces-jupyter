# Fisher Brown
# UWYO COSC 1010
# 27 Oct 24
# HW 02
# Lab Section: 10
# Sources, people worked with, help given to: 
# your
# comments
# here

morse_code = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.',
              'h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.',
              'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-',
              'v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'  '}

decoded_message = ''

message = input('Write message to be translated to morse code: ')
message = message.lower()
for char in message:
    for key, value in morse_code.items():
        if char.isalpha() and char == key:
            decoded_message += morse_code[key]
            decoded_message += ' '
        else:
            continue

print(decoded_message)