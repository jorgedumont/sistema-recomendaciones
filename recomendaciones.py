import analisis_Lexico as al

def gettitulo(fichero): #coger titulo para las recomendaciones
    f1=open(fichero,'r',encoding="utf8")
    titulo=f1.readlines()[0].replace("Titulo:","").strip()
    return titulo



def vectorTags(fichero):
    wordlist1 = []
    f1=open(fichero,'r',encoding="utf8")
    lineatags=f1.readlines()[4].replace("Tags: ","").replace(",\n","").replace(", \n","").strip()
    wordlist1=wordlist1+lineatags.split(", ")
    return wordlist1




def preprocesarVector(vector):
    vectorsalida=[]
    for elemento in vector:
        vectorsalida.append(al.preprocess(elemento).strip())
    return vectorsalida



def CoeficienteSoerensenDice(fichero1,fichero2):
    listatags1=vectorTags(fichero1)
    listatags2=vectorTags(fichero2)
    conjuntotags1=set(listatags1)
    conjuntotags2=set(listatags2)
    return 2*len(conjuntotags1.intersection(conjuntotags2))/(len(conjuntotags1)+len(conjuntotags2))


def obtenerTagsporFrecuencia(articulo):
    palabras=""
    for x in articulo:
        palabras+=x.text
    palabras=al.preprocess(palabras)
    palabras=al.listaParada(palabras).split()
    vecespalabra={}
    for palabra in list(set(palabras)):
        vecespalabra[palabra]=palabras.count(palabra)
    l=ordenarsimilitudes(vecespalabra)
    salida=""
    for i in range(5):
        salida+=l[i][0]+", "
    return salida



def ordenarsimilitudes(d):
    l=[(k,v) for k, v in sorted(d.items(), key=lambda item: item[1])]
    l.reverse()
    return l






