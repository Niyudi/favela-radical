#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#                dormir
from time import sleep

class Personagem(object):
    def __init__(self):
        self.posição = 10.0
        self.velocidade = 3.0
    
    def update(self, tempo, aceleração):
        self.posição = self.posição + (self.velocidade * tempo)
        self.velocidade = self.velocidade + (aceleração * tempo)
        
        if (self.posição < 0):
            self.posição = 0
            self.velocidade = -self.velocidade

personagem = Personagem()

tempo = 0.01
gravidade = -5.0

i = 1
while (True):
    personagem.update(tempo, gravidade)
    
    print("Update número " + str(i))
    print(personagem.posição)
    print(personagem.velocidade)
    print("")
    
    i = i + 1
    
    sleep(tempo)