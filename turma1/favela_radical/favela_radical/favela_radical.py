#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from -> de         import -> importar
from PyQt5.QtWidgets import QApplication

#    sys -> sistema
from sys import argv, exit

from interface import JanelaPrincipal

class Aplicativo(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        
        self.window = JanelaPrincipal()

def main():
    app = Aplicativo(argv)
    
    exit(app.exec_())

if __name__ == "__main__":
    main()