# -*- coding=utf-8 -*-

#import Image
from PIL import Image
#import argparse
import argparse

#creating a parser
parser = argparse.ArgumentParser()

#adding argument 'file'
parser.add_argument('file')
#adding argument '-o', '--output'
parser.add_argument('-o', '--output')
#adding argument 'width', setting type and default
parser.add_argument('--width', type = int, default = 80)
#adding argument 'height', setting type and default
parser.add_argument('--height', type = int, default = 80)

#creating args with parse_args() method.
args = parser.parse_args()

#set IMG to file attribute of args
IMG = args.file
#set OUTPUT to output attribute of args
OUTPUT = args.output
#set WIDTH to width attribute of args
WIDTH = args.width
#set HEIGHT to height attribute of args
HEIGHT = args.height

#setting ascii_char, used to turn pixel to character
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#mapping 256 greyscale to ascii_char
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    #convert RGB to grayscale
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    #open IMG, set it to im
    im = Image.open(IMG)
    #resize im to the lowest quality
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    #create txt attribute
    txt = ""

    #count every pixel in the picture
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    #output.txt
    if OUTPUT:
        with open(OUTPUT, 'w') as f: #if there is an input name
            f.write(txt)
    else:
        with open("output.txt", 'w') as f: #else output as output.txt
            f.write(txt)
