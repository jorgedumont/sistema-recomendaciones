# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Recomendacion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import recomendaciones as sim
import glob
import analisis_Lexico as al

class Recomendacion(object):
    def setupUi(self, MainWindow):
        self.listanoticias=[]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 50, 73, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 50, 101, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.cargarNoticias)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(410, 30, 371, 101))
        self.listView.setObjectName("listView")
        self.listView.doubleClicked.connect(self.cargarNoticiaFichero)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(410, 10, 61, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 20, 55, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(140, 20, 61, 16))
        self.label_13.setObjectName("label_13")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 681, 121))
        self.textEdit.setObjectName("textEdit")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 110, 55, 16))
        self.label_14.setObjectName("label_14")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 390, 701, 161))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 280, 151, 16))
        self.label_15.setObjectName("label_15")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 310, 181, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.CalculoRecomendaciones)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(210, 280, 551, 101))
        self.listView_2.setObjectName("listView_2")
        self.listView_2.doubleClicked.connect(self.ImprimirNoticia)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Todos"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "ElMundo"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "ElPais"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "20Minutos"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Todos"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Salud"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Tecnologia"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Ciencia"))
        self.pushButton.setText(_translate("MainWindow", "Buscar"))
        self.label_11.setText(_translate("MainWindow", "Noticias:"))
        self.label_12.setText(_translate("MainWindow", "Medio:"))
        self.label_13.setText(_translate("MainWindow", "Categoria:"))
        self.label_14.setText(_translate("MainWindow", "Preview:"))
        self.label_15.setText(_translate("MainWindow", "Top 5 Recomendaciones:"))
        self.pushButton_2.setText(_translate("MainWindow", "Buscar Recomendaciones"))
        
    def getnoticias(self,medio,categoria):
        lista=glob.glob(medio+'\\'+categoria+"/*.txt")
        lista+=glob.glob(medio+'\\'+categoria+"/*.txt")
        lista+=glob.glob(medio+'\\'+categoria+"/*.txt")
        return lista
        
    def obtenerListaNoticiasSeleccionada(self):
        seleccion=str(self.comboBox_3.currentText())
        categoria=str(self.comboBox_4.currentText())
        print("seleccion:",seleccion,"categoria:",categoria)
        listanoticias=[]
        if seleccion=='Todos'or seleccion=='ElPais'and categoria=='Salud':
            listanoticias+=self.getnoticias('ElPais','Salud')
        if seleccion=='Todos'or seleccion=='ElPais'and categoria=='Tecnologia':
            listanoticias+=self.getnoticias('ElPais','Tecnologia')
        if seleccion=='Todos'or seleccion=='ElPais'and categoria=='Ciencia':
            listanoticias+=self.getnoticias('ElPais','Ciencia')
        if seleccion=='Todos'or seleccion=='ElMundo'and categoria=='Salud':
            listanoticias+=self.getnoticias('ElMundo','Salud')
        if seleccion=='Todos'or seleccion=='ElMundo'and categoria=='Tecnologia':
            listanoticias+=self.getnoticias('ElMundo','Tecnologia')
        if seleccion=='Todos'or seleccion=='ElMundo'and categoria=='Ciencia':
            listanoticias+=self.getnoticias('ElMundo','Ciencia')
        if seleccion=='Todos'or seleccion=='20Minutos'and categoria=='Salud':
            listanoticias+=self.getnoticias('20Minutos','Salud')
        if seleccion=='Todos'or seleccion=='20Minutos'and categoria=='Tecnologia':
            listanoticias+=self.getnoticias('20Minutos','Tecnologia')
        if seleccion=='Todos'or seleccion=='20Minutos'and categoria=='Ciencia':
            listanoticias+=self.getnoticias('20Minutos','Ciencia')
        return listanoticias
    
    def cargarNoticias(self):
        listanoticias=self.obtenerListaNoticiasSeleccionada()
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in listanoticias:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
            
    def cargarNoticiaFichero(self):
        noticia = self.listView.selectedIndexes()
        dato=noticia[0].data()
        self.cargarNoticia(dato,self.textEdit)

    def cargarNoticia(self,dato,textedit):
        file = open(dato, encoding="utf8")
        textedit.setText(file.read())
        
    def obtenerListaNoticiasSeleccionada2(self,seleccion="Todos"):
        listanoticias=[]
        if seleccion=='Todos'or seleccion=='ElPais':
            listanoticias+=self.getnoticias2('ElPais')
        if seleccion=='Todos'or seleccion=='ElMundo':
            listanoticias+=self.getnoticias2('ElMundo')
        if seleccion=='Todos'or seleccion=='20Minutos':
            listanoticias+=self.getnoticias2('20Minutos')
        return listanoticias
    
    
    def getnoticias2(self,carpeta):
        lista=glob.glob(carpeta+"\\Salud\\*.txt")
        lista+=glob.glob(carpeta+"\\Tecnologia\\*.txt")
        lista+=glob.glob(carpeta+"\\Ciencia\\*.txt")
        return lista
    
    def CalculoRecomendaciones(self):
        noticia = self.listView.selectedIndexes()
        noticiareferencia=noticia[0].data()
        print("Noticiareferencia:", noticiareferencia)
        dicnoticias={}
        for noticia in self.obtenerListaNoticiasSeleccionada2():
            noticia != noticiareferencia
            coeficiente=sim.CoeficienteSoerensenDice(noticiareferencia,noticia)
            dicnoticias[noticia]=coeficiente
        ranking=5
        ordenado=sim.ordenarsimilitudes(dicnoticias)[:ranking]
        texto=""
        self.listanoticias=[]
        for (noticia,similitud) in ordenado:
            self.listanoticias.append(noticia)
            medio=noticia.split("\\")[0]
            print(noticia)
            titulo=sim.gettitulo(noticia)
            texto+="Titular: "+titulo + "(" + medio + ")" + " - " + str(round(similitud,3)) + "\n"
        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)
        for i in texto.split("\n"):
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        return self.listanoticias
    
    def ImprimirNoticia(self):
        noticia=self.listView_2.selectedIndexes()
        indice= noticia[0].row()
        print("indice:",indice)
        self.cargarNoticia(self.listanoticias[indice],self.textEdit_2)
        
            
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Recomendacion()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

