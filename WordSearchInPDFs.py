
import pdfplumber
import os
import re
from pdfplumber.utils import extract_text


path="C://datafile"

#data loading
def GetDataPath(Path):
        try :
            DataFilePath = Path
            FileList=os.listdir(DataFilePath)
            return FileList,Path
        except :
                DataFilePath = input("file path miss,Please entrer the file path\n =>")
                return GetDataPath(DataFilePath)

result= GetDataPath(path)
FileList=result[0]
DataFilePath=result[1]+"/"

ListPage=[]

def TextMatching(InputText):
    DicFile={}
    for FileName in FileList:
        with pdfplumber.open(DataFilePath+FileName) as pdf:
            for i,pg in enumerate(pdf.pages):
                PdfText= pdf.pages[i].extract_text()
                matchObj=re.search(InputText,PdfText,re.I)
                if matchObj:
                    ListPage.append(i+1)
                    DicFile={FileName:ListPage}
    if DicFile!={}:
        print ("Le mot \"" + InputText + "\" dans le fichier avec les pages : ",DicFile)
        DicFile.clear()
    else :
        print("Oups, rien trouvé dans les fichiers")
                    
while True:
    InputText = str(input ("Tapes ton mot, ma cherie jess\n =>"))
    TextMatching(InputText)
    Answer=str(input ("Tapes \"N\" pour stopper, tapes n'importe quelle touche pour continuer ?\n =>"))
    if Answer=="N" or Answer=="n":
        break
