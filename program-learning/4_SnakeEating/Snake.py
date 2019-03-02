#-*- coding:utf-8 -*-
import pygame

#Here begin the Snake~
class Snack(object):
    def __init__(self):
        #I don't know what is that means..
        self.item = [(3, 25), (2, 25), (1, 25), (1, 24), ]
        #setting x and y
        self.x = 0
        self.y = -1

    #how does enlarge work here?
    def move(self, enlarge):
        #use enlarge to see if eat food
        if not enlarge:
            self.item.pop()
        head =

