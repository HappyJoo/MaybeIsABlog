#-*- coding:utf-8 -*-

from MyQR import myqr

PICTURE = input('What picture do you have, please give me a pic:')
OUTPUT = 'QR_' + PICTURE

col = input('Do you want it colorized?(Y/N)')
while col not in 'YyNn':
    col = input('Comon, give me a Y or N~~')

if col == 'Y' or col == 'y':
    col = True
else:
    col = False

myqr.run(
        words = 'https://www.shiyanlou.com',
        colorized = col,
        picture = PICTURE,
        save_name = OUTPUT,
        )
