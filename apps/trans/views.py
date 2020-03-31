# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils.encoding import uri_to_iri

import sys

#import googletrans
#from googletrans import Translator

# Create your views here.
def traductor(request):
    if request.method == 'GET':
        texto = request.GET.get('traductor_box') #captura texto que se quiere traducir
        #traducc = request.GET.get('traduccion') #captura la forma de traduccion
        origen = request.GET.get('origen')
        destino = request.GET.get('destino')

        enc_origen = uri_to_iri(origen)
        enc_destino = uri_to_iri(destino)
        
        if texto == None or texto == "":
            texto = "Hola"
            
       

        print(origen)
        print(enc_origen)
        print(enc_destino)

        
        
        if origen == "Español":
            trans_o = "es"
        else:
            trans_o = "en"
            

        if destino == "Ingles":
            trans_f = "en"
            if texto == None or texto == "":
                texto = "hi"
        else:
            trans_f = "es"
           
        

        #if texto == None:
        #    texto = "Hola"

        #if traducc == None:
        #    trans_o = "es"
        #    trans_f = "en"
        #else:
        #    trans_o = "en"
        #    trans_f = "es"
        
        import googletrans #importa libreria
        from googletrans import Translator #importa libreria de funcion translate
        #import pandas as pd
        translator = Translator() #almacenamos el proceso en funciones
        resultado = translator.translate(texto, src=trans_o, dest=trans_f) #funcion final de traduccion
        ctx = {'TEXT' : resultado.text , 'Original': texto , 'ORIGEN': origen, 'DESTINO': destino}
        return render(request, 'traductor/index.html', ctx)
    else:
        return render(request, 'traductor/index.html')
