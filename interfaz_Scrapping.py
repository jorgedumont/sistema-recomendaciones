# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Scrapping.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import io
import glob
import recomendaciones as sim

from PyQt5 import QtCore, QtGui, QtWidgets

class Scrapping(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.pushButtonElMundoExecute)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.pushButtonElPaisExecute)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 410, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.pushButton20MinutosExecute)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(270, 10, 501, 141))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(270, 180, 501, 141))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(270, 350, 501, 141))
        self.listView_3.setObjectName("listView_3")
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
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        
        
    def cargarNoticiaElMundo(self,url,periodico,seccion,n):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print("parseando "+url)
        articulo = soup.find("div", {"class":"ue-l-article__body ue-c-article__body"})
        titulo = soup.find("h1")
        entradilla=soup.find("p", {"class":"ue-c-article__standfirst"})
        fecha=soup.find("time")
        articulo=articulo.findAll('p')
        tags =soup.findAll("ul",{"class":"ue-c-article__tags ue-l-article--leftcol-width-from-desktop ue-l-article--float-left-from-desktop ue-l-article--move-to-leftcol-from-desktop ue-l-article--bottom-absolute-from-desktop"})
        tags1=""
        if len(tags)==0:
            tags1=sim.obtenerTagsporFrecuencia(articulo)
        else:
            for i in tags[0]:
                tags1=tags1+" "+i.get_text().strip()+","
        if articulo is None or entradilla is None or titulo is None or fecha is None or tags is None or tags1 is None:
            print("Error parseando\n")
            return False
        nombrefichero="%s\%s\%s.%s.%03d.txt"%(periodico,seccion,seccion,fecha["datetime"][:10],n)
        f = io.open(nombrefichero, 'w',encoding="utf-8")
        f.writelines("Titulo: " + titulo.get_text() + "\n\n")
        f.writelines("Entradilla: " + entradilla.get_text() + "\n\n")
        f.writelines("Tags:"+tags1+ "\n\n")
        for x in articulo:
            f.writelines(x.text)
        f.close()
        return True

    def cargarNoticiaElPais(self,url,periodico,seccion,n):
        dmeses ={"ene":1,"feb":2,"mar":3,"abr":4,"may":5,"jun":6,"jul":7,"ago":8,"sep":9,"oct":10,"nov":11,"dic":12}
        print("parseando "+url)
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error parseando\n")
            return False
        articulo = soup.find("div", {"class":"articulo-cuerpo"})
        if articulo is None:
            articulo= soup.find("div",{"class":"article_body"})
        titulo = soup.find("h1")
        entradilla=soup.find("h2")
        if entradilla is None:
            entradilla=soup.find("div",{"class":"articulo-introduccion"})
        fecha=soup.find("a", {"class":"a_ti"})
        if not fecha is None:
            datos=fecha.get_text().split(" - ")
            if len(datos)==3:
                fechatext=datos[1].strip()
            else:
                fechatext=datos[0].strip()
            datosfecha=fechatext.split(" ")[:3]
            cadenafecha="%s-%02d-%s"%(datosfecha[2],dmeses[datosfecha[1]],datosfecha[0])
        else:
            fecha=soup.find("time")
            cadenafecha=fecha["datetime"][:10]
        tags=soup.find("meta", {"name":"news_keywords"})
        if tags is None:
            return False
        tags=tags.get("content").split(",")
        if articulo is None or entradilla is None or titulo is None or fecha is None or tags is None:
            print("Error parseando\n")
            return False
        articulo=articulo.findAll('p')
        nombrefichero="%s\%s\%s.%s.%03d.txt"%(periodico,seccion,seccion,cadenafecha,n)
        f = io.open(nombrefichero, 'w',encoding="utf-8")
        f.writelines("Titulo: " + titulo.get_text() + "\n\n")
        f.writelines("Entradilla: " + entradilla.get_text() + "\n\n")
        tagsstr=""
        if len(tags)==0:
            tagsstr=sim.obtenerTagsporFrecuencia(articulo)
        else:
            for t in tags:
                tagsstr+=t+", "
        f.writelines("Tags: "+tagsstr+ "\n\n")
        for x in articulo:
            f.writelines(x.text)
        f.close()
        return True
    
    def cargarNoticia20minutos(self,url,periodico,seccion,n):
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            print("Error parseando\n")
            return False
        print("parseando "+url)
        articulo = soup.find("div", {"class":"article-text"})
        titulo = soup.find("h1")
        entradilla=soup.find("div", {"id":"m35-34-36"})
        if entradilla is None:
            entradilla=soup.find("div",{"id":"m96-95-97"})
        fecha=soup.find("span", {"class":"article-date"})
        if not fecha is None:
            datos=fecha.get_text().split(" - ")
            fechatext=datos[0].strip()
            datosfecha=fechatext.split(".")[:3]
            cadenafecha="%s-%s-%s"%(datosfecha[2],datosfecha[1],datosfecha[0])
        tags =soup.find("div",{"class":"module module-related"})
        if tags != None:
            tags=tags.find("ul")
            tags1=""
            if len(tags)==0:
                tags1=sim.obtenerTagsporFrecuencia(articulo)
            else:
                for i in tags:
                    tags1=tags1+" "+i.get_text().strip()+","
        else:
            return False;
        if articulo is None or entradilla is None or titulo is None or fecha is None or tags is None or tags1 is None:
            print("Error parseando\n")
            return False
        articulo=articulo.findAll('p')
        nombrefichero="%s\%s\%s.%s.%03d.txt"%(periodico,seccion,seccion,cadenafecha,n)
        f = io.open(nombrefichero, 'w',encoding="utf-8")
        f.writelines("Titulo: " + titulo.get_text().strip() + "\n\n")
        f.writelines("Entradilla: " + entradilla.get_text().strip() + "\n\n")
        f.writelines("Tags: "+tags1+ "\n\n")
        for x in articulo:
            f.writelines(x.text)
        f.close()
        return True
    
       
    def cargarListanoticiasElMundo(self,url,periodico,seccion):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("a",{"class":"ue-c-cover-content__link"})
        n=1;
        for l in links:
            if self.cargarNoticiaElMundo(l["href"],periodico,seccion,n):
                n=n+1
                
                
    def cargarListanoticiasElPais(self,url,periodico,seccion):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("h2",{"class":"headline"})
        n=1;
        for l in links:
            url="http://www.elpais.com" + l.find("a")["href"]
            if self.cargarNoticiaElPais(url,periodico,seccion,n):
                n=n+1
                
                
    def cargarListanoticias20minutos(self,url,periodico,seccion):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.findAll("div",{"class":"media-content"})
        n=1;
        for l in links:
            url=l.find("a")["href"]
            if self.cargarNoticia20minutos(url,periodico,seccion,n):
                n=n+1
                
    def pushButtonElMundoExecute(self):
        self.cargarListanoticiasElMundo("https://www.elmundo.es/ciencia-y-salud/salud.html","ElMundo","Salud")
        self.cargarListanoticiasElMundo('https://www.elmundo.es/tecnologia.html','ElMundo','Tecnologia')
        self.cargarListanoticiasElMundo("https://www.elmundo.es/ciencia-y-salud/ciencia.html","ElMundo","Ciencia")
        lista=glob.glob("ElMundo/Salud/*.txt")
        lista2=glob.glob("ElMundo/Tecnologia/*.txt")
        lista3=glob.glob("ElMundo/Ciencia/*.txt")
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in lista:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista2:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista3:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        
    def pushButtonElPaisExecute(self):
        self.cargarListanoticiasElPais("https://elpais.com/noticias/sanidad-publica/","ElPais","Salud")
        self.cargarListanoticiasElPais("https://elpais.com/tecnologia/","ElPais","Tecnologia")
        self.cargarListanoticiasElPais("https://elpais.com/ciencia/","ElPais","Ciencia")
        lista=glob.glob("ElPais/Salud/*.txt")
        lista2=glob.glob("ElPais/Tecnologia/*.txt")
        lista3=glob.glob("ElPais/Ciencia/*.txt")
        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)
        for i in lista:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista2:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista3:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        
    def pushButton20MinutosExecute(self):
        self.cargarListanoticias20minutos("https://www.20minutos.es/salud/","20Minutos","Salud")
        self.cargarListanoticias20minutos("https://www.20minutos.es/tecnologia/","20Minutos","Tecnologia")
        self.cargarListanoticias20minutos("https://www.20minutos.es/ciencia/","20Minutos","Ciencia")
        lista=glob.glob("20Minutos/Salud/*.txt")
        lista2=glob.glob("20Minutos/Tecnologia/*.txt")
        lista3=glob.glob("20Minutos/Ciencia/*.txt")
        model = QtGui.QStandardItemModel()
        self.listView_3.setModel(model)
        for i in lista:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista2:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        for i in lista3:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Scrapping()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

