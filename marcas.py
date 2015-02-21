import requests

lista = open("lista.csv")
clase = raw_input("clase a buscar")
if clase.isdigit():
    for nombre in lista:
        print nombre
        r=requests.post(url="http://marcanet.impi.gob.mx/marcanet/controler/FoneticaLista",headers={"Content-Type":"application/x-www-form-urlencoded"},data="denominacion="+nombre+"&clase="+clase)
        argPDFinicio = r.text.find("PDF")+18
        argPDFfinal = r.text[argPDFinicio:].find("/")
        argPDF = r.text[argPDFinicio:argPDFinicio+argPDFfinal]
        p = requests.get(url="http://marcanet.impi.gob.mx/marcanet/controler/FoneticaPDF/_denominacion/"+argPDF+"/_mc/direct")
        PDF = open("resultados/"+nombre[:-1]+"-"+clase+".pdf","w")
        PDF.write(p.content)
        PDF.close()
    lista.close()
else:
    print "clase invalida"
