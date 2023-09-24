import pyjokes
from googletrans import Translator


ls = pyjokes.get_joke(language='en',category='neutral')
tranlator = Translator()
ss = tranlator.translate(ls,dest='uz')
print(ss.text,ls)