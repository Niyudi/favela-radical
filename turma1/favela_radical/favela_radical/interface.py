#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt # Novos imports
from PyQt5.QtGui import (QBrush, QColor, QPainter,
                         QPen) # Novos imports
from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QMainWindow,
                             QPushButton, QVBoxLayout, QWidget)

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.título = "Favela Radical"
    
        self.altura = 1600
        self.largura = 900
        
        self.iniciarImagem()
    
    def adicionarUm(self):
        self.imagem.contador += 1 # Adiciona 1 no contador
        self.imagem.update() # Atualiza o desenho
        
    def iniciarImagem(self):
        self.setWindowTitle(self.título)
        self.resize(self.altura, self.largura)
        
        # Imagem
        self.imagem = QImagem()
        
        botão1 = QPushButton("Adicionar 1!")
        botão1.clicked.connect(self.adicionarUm)
        botão2 = QPushButton("Subtrair 1!")
        botão2.clicked.connect(self.subtrairUm)
        
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        
        layout1.addWidget(self.imagem) # Substituí a label por imagem
        layout1.addLayout(layout2)
        
        layout2.addWidget(botão1)
        layout2.addWidget(botão2)
        
        central_widget = QWidget()
        central_widget.setLayout(layout1)
        self.setCentralWidget(central_widget)
        
        self.show()
    
    def subtrairUm(self):
        self.imagem.contador -= 1 # Adiciona 1 no contador
        self.imagem.update() # Atualiza o desenho

# Classe nova, extensão de widget, onde o jogo será desenhado!
class QImagem(QWidget):
    def __init__(self):
        super().__init__()
        
        self.contador = 0 # Incia o contador
    
    # Desenha no widget quando self.upadte() for chamada
    def paintEvent(self, event):
        # Define as cores
        fundo_cor = QColor(220, 255, 230)
        texto_cor = QColor(0, 0, 0)
        
        transparente = QColor(255, 255, 255)
        transparente.setAlphaF(0.0)
        
        # Começa o painter, a pen e o brush
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.SolidLine)
        brush = QBrush(Qt.SolidPattern)
        
        # Desenha o fundo
        pen.setWidth(2)
        pen.setColor(transparente)
        qp.setPen(pen)
        brush.setColor(fundo_cor)
        qp.setBrush(brush)
        qp.drawRect(0, 0, 500, 500) # Desenha um retangulo comecando na coordeanda (0, 0) e terminando em (500, 500)
        
        # Desenha o texto
        pen.setColor(texto_cor)
        qp.setPen(pen)
        qp.drawText(250, 250, str(self.contador)) # Desenha o número na coordenada (250, 250)
        
        # Termina o painter
        qp.end()