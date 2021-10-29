#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QLabel, QMainWindow, QPushButton,
                             QVBoxLayout, QWidget)

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.título = "Favela Radical"
    
        self.altura = 1600
        self.largura = 900
        
        self.iniciarImagem()
    
    def mudarTexto(self):
        print("PRESSIONADO!")
    
    def iniciarImagem(self):
        self.setWindowTitle(self.título)
        self.resize(self.altura, self.largura)
        
        texto1 = QLabel("Olá!")
        
        botão1 = QPushButton("Botão!")
        botão1.clicked.connect(self.mudarTexto)
        
        layout1 = QVBoxLayout()
        
        layout1.addWidget(texto1)
        layout1.addWidget(botão1)
        
        central_widget = QWidget()
        central_widget.setLayout(layout1)
        self.setCentralWidget(central_widget)
        
        self.show()