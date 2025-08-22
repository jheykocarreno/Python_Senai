#importar biblioteca ZipFile
import zipfile

with zipfile.ZipFile("zipado.zip", "w") as z:
    z.write("teste.txt")
    
zipfile.download("zipado.zip")

import zipfile
with zipfile.ZipFile("zipado.zip", "r") as z:
    z.extractall("descompactados")

print("Arquivos descompactados na pasta 'descopactados'")