# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils.encoding import uri_to_iri
from gtts import gTTS
import sys
import uuid
import threading
import json
from django.http import JsonResponse
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import googletrans
from googletrans import Translator 

translator = Translator()


@method_decorator(csrf_exempt)
def Traductor2(request,to,from_l, *args ,**kwargs):
    if request.method == 'POST':
        if to == "Español":
            trans_o = "es"
            trans_f = "en"
        else:
            trans_o = "en"
            trans_f = "es"
        
        json_ = json.loads(request.body.decode("utf-8"))
        texto = ''
        for i in json_:
            texto = json_[i]
        
        resultado = translator.translate(texto, src=trans_o, dest=trans_f)
        UUID = uuid.uuid1()
        audio = tssTheaad(resultado.text,trans_f,str(UUID))
        audio.start()

        return JsonResponse({"instance": resultado.text , 'audio': '/static/'+ str(UUID)+'.mp3' }, status=200, safe=False)
    else:
        return JsonResponse({"instance": 'adios'}, status=200, safe=False)



def traductor(request):
    return render(request, 'traductor/in.html')



class tssTheaad(threading.Thread):
    def __init__(self, text_file, lang, namefile):
        threading.Thread.__init__(self)
        self.text_file = text_file
        self.lang = lang
        self.namefile = namefile

    def run(self):
        try:
            file = gTTS(text=self.text_file, lang=self.lang)
            filename = self.namefile + '.mp3'
            file.save("static/%s" %(str(filename)))
            print('final de creacion')
        except:
            print('error en crear file')
