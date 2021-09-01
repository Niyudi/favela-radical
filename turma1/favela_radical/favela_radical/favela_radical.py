#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from -> de         import -> importar
from PyQt5.QtWidgets import QApplication, QMainWindow

#    sys -> sistema
from sys import argv, exit

class Aplicativo(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        
        self.window = QMainWindow()
        self.window.show()

def main():
    app = Aplicativo(argv)
    
    exit(app.exec_())

if __name__ == "__main__":
    main()