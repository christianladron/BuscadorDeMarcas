import requests

lista = open("lista.csv")
for nombre in lista:
    print nombre
    r=requests.post(url="http://marcanet.impi.gob.mx/marcanet/controler/FoneticaLista",headers={"Content-Type":"application/x-www-form-urlencoded"},data="denominacion="+nombre+"&clase=32")
    argPDFinicio = r.text.find("PDF")+18
    argPDFfinal = r.text[argPDFinicio:].find("/")
    argPDF = r.text[argPDFinicio:argPDFinicio+argPDFfinal]
    p = requests.get(url="http://marcanet.impi.gob.mx/marcanet/controler/FoneticaPDF/_denominacion/"+argPDF+"/_mc/direct")
    PDF = open("resultados/"+nombre+".pdf","w")
    PDF.write(p.content)
    PDF.close()
lista.close()
