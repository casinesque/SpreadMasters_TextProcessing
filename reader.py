import fitz
import db_connection
from collections import Iterable

pdf_document = "[ITA]Antologia.pdf"
doc = fitz.open(pdf_document)
contentList=[]
print ("number of pages: %i" % doc.pageCount)
for page in doc.pages(59,309,1):
    contentList.append(page.getText("text"))
# pulisco la lista dagli spazi. Questa è una lista unica con tutto il destro dentro.
contentList = [ item.replace('\t', ' ').replace('\n',' ') for item in contentList ]
wordSeparatedContestList=[]
for i in range(len(contentList)):
    wordSeparatedContestList.append(contentList[i].split(' '))
len = len(wordSeparatedContestList)
#Dichiaro una sottolista per ogni pagina.
print(wordSeparatedContestList)
for element in wordSeparatedContestList:
#Tento di accedere al primo elemento di ogni parola in ogni lista
#element è ogni lista, devo controllare quelle che iniziano per valori lower.
    if (element[0].islower() or element[0].istitle()) and not(element[0].isupper()):
        index=wordSeparatedContestList.index(element)
        if(index!=0):
            wordSeparatedContestList[index-1].append(wordSeparatedContestList[index])
            del wordSeparatedContestList[index]
# questa operazione è detta --> Flatten an irregular list of lists, cioè una lista che non contiene solo liste all' interno ma anche elementi primitivi   
def flatten(items):
        for word in items:
            if isinstance(word, Iterable) and not isinstance(word, (str, bytes)):
                yield from flatten(word)
            else:
                yield word    
flat_list=[list(flatten(item)) for item in wordSeparatedContestList]
print(flat_list)

#POPULATE DB:
id=1
for poem in flat_list:
    print
    db_connection.inserisciPoesia(poem,id)
    id=id+1

