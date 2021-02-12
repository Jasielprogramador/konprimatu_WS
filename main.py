import sys
import zlib
import requests

# HTTP eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
#Las comillas simples y las dobles son lo mismo en python

metodoa = 'GET'
uria = "https://www.google.es/"
goiburuak = {'Host': 'www.google.es'}
edukia=''

compressed= False

if len(sys.argv)==1:
    goiburuak['Accept-Encoding']='identity'
elif sys.argv[1]=='compress':
    compressed=True
    goiburuak['Accept-Encoding']='gzip'
else:
    print("Errorea komandoa --- python main.py compress --- moduan jarri egin behar da")
    exit(0)

erantzuna = requests.request(metodoa, uria, data=edukia, headers=goiburuak, allow_redirects=False, stream=True)

kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)
print("RESPONSE CONTENT LENGTH: " + str(len(erantzuna.raw.data))+" byte")

if compressed:
    edukia_compressed=erantzuna.raw.data
    edukia_uncompressed=zlib.decompress(edukia_compressed,16+zlib.MAX_WBITS)
    print("UNCOMPRESSED RESPONSE CONTENT LENGTH: "+str(len(erantzuna.raw.data))+" byte")

