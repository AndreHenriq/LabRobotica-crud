import sys
from PyQt5.QtWidgets import QApplication
from view import *
from controller import Controller
from model import Model

if __name__ =="__main__":
    app = QApplication(sys.argv)
    view_MWindow = MWindow()
    view_logar = logar()
    model = Model()
    contr = Controller(view_logar, view_MWindow, model)
    view_MWindow.set_controller(contr)
    view_logar.set_controller(contr)
    model.set_controller(contr)
    view_logar.show()
    app.exec()
