#programe to find the words in Books that are non present in 20k.txt

book1uniqu.list = []
with open("Book1.txt", encoding="utf8") as f:
    with open("20k.txt", encoding="utf8") as fe:
        for line in f:
	   	for word in line.split():
              		for linefe in fe:
               			 if (word != linefe):
                   			 print(word)
					 book1uniqu.list.append(word)
                   			 break
                		  else:
                    			 break
                    			 
print(book1uniqu.list)


#programme to find words in the 20k.txt that are non present in any Books

rarewords.list = []
with open("20k.txt", encoding="utf8") as f:
    with open("book1.txt", encoding="utf8") as fe:
        for line in f:
	   	for linefe in fe:
			for word in linefe.split():	
			
               			 if ( != linefe):
                   			 print(word)
					 rarewords.list.append(word)
                   			 break
                		  else:
                    			 break

print(rarewords.list)

