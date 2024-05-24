import sys
from caudaltrescasos import *

class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.ButtonCalcularA, QtCore.SIGNAL('clicked()'), self.dispcalculocaudal)
        QtCore.QObject.connect(self.ui.ButtonCalcularB, QtCore.SIGNAL('clicked()'), self.dispcalculovelocidad)
        QtCore.QObject.connect(self.ui.ButtonCalcularC, QtCore.SIGNAL('clicked()'), self.dispcalculoarea)

    def dispcalculocaudal(self):
        if len(self.ui.GrupoA2line01_Velocidad.text()) != 0:
            V_GA1 = float(self.ui.GrupoA2line01_Velocidad.text())
        else:
            V_GA1 = 0
        if len(self.ui.GrupoA2line02_Area.text()) != 0:
            A_GA1 = float(self.ui.GrupoA2line02_Area.text())
        else:
            A_GA1 = 0
        Q_GA1 = V_GA1 * A_GA1
        self.ui.labelResultadoCaudal.setText("Caudal: " + str(Q_GA1))

    def dispcalculovelocidad(self):
        if len(self.ui.GrupoB2line01_Caudal.text()) != 0:
            Q_GB1 = float(self.ui.GrupoB2line01_Caudal.text())
        else:
            Q_GB1 = 0
        if len(self.ui.GrupoB2line02_Area.text()) != 0:
            A_GB1 = float(self.ui.GrupoB2line02_Area.text())
        else:
            A_GB1 = 0
        V_GB1 = Q_GB1/A_GB1
        self.ui.labelResultadoVelocidad.setText("Velocidad: " + str(V_GB1))

    def dispcalculoarea(self):
        if len(self.ui.GrupoC2line01_Caudal.text()) != 0:
            Q_GC1 = float(self.ui.GrupoC2line01_Caudal.text())
        else:
            Q_GC1 = 0
        if len(self.ui.GrupoC2line02_Velocidad.text()):
            V_GC1 = float(self.ui.GrupoC2line02_Velocidad.text())
        else:
            V_GC1 = 0
        A_GB1 = Q_GC1/V_GC1
        self.ui.labelResultadoArea.setText("Area: " + str(A_GB1))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


