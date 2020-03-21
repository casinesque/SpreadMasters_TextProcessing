import fitz
import db_connection
from collections import Iterable

pdf_document = "[ITA]Antologia.pdf"
doc = fitz.open(pdf_document)
contentList=[]
print ("number of pages: %i" % doc.pageCount)
for page in doc.pages(59,309,1):
    contentList.append(page.getText("text"))
# cleaning list from spaces. I got a list with all the text inside. 
contentList = [ item.replace('\t', ' ').replace('\n','££').replace(',','$$') for item in contentList ]
wordSeparatedContestList=[]
for i in range(len(contentList)):
    wordSeparatedContestList.append(contentList[i].split(' '))
len = len(wordSeparatedContestList)
#Defining a sublist for each page
#print(wordSeparatedContestList)
for element in wordSeparatedContestList:
#Trying to accessing the first word of each sublist, looking for beginning lower chars strings   
    if (element[0].islower() or element[0].istitle()) and not(element[0].isupper()):
        index=wordSeparatedContestList.index(element)
        if(index!=0):
            wordSeparatedContestList[index-1].append(wordSeparatedContestList[index])
            del wordSeparatedContestList[index]
# Flattening an irregular list of lists, 
# Flatten a list which not only sublist inside but also primitives elements   
def flatten(items):
        for word in items:
            if isinstance(word, Iterable) and not isinstance(word, (str, bytes)):
                yield from flatten(word)
            else:
                yield word    
flat_list=[list(flatten(item)) for item in wordSeparatedContestList]

flat_cleaned_list=[]
for ilist in flat_list:
    ilist2=[]
    for item in ilist:
        item=item.replace(' ', '\t').replace('££','\n ').replace('$$',',')
        ilist2.append(item)
    flat_cleaned_list.append(ilist2)

#POPULATE DB:
id=1
for poem in flat_cleaned_list:
    fullStr = ' '.join(poem) #trasforming each sublist in a string to be better saved on db.
    print(fullStr)
    db_connection.inserisciPoesia(fullStr,id)
    id=id+1

