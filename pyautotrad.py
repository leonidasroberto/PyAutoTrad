from googletrans import Translator
import clipboard
from time import sleep


translator=Translator()

def traduz(var):
    
    trad=(translator.translate(var, dest="pt").text)
    print("Tradução:",trad)
        
cont=0
while True:
    #sleep(3)
    var=clipboard.paste()
    
    if cont == var:
        print("Em espera...")
        
    else:
        traduz(var)
        cont=var
    
    sleep(3)

