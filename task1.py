
  


file = open("20k.txt","r")

for word in file:
	for letter in word:
		 if letter == "o":
            		word = word.replace(letter,"0")
		 if letter == "a":
            		word = word.replace(letter,"4")
		 if letter == "e":
            		word = word.replace(letter,"3")
		 if letter == "i":
            		word = word.replace(letter,"1")
		 s="er"
		 rep="x0r"
		 if word.endswith(s):
    			word = word[:-len(s)] + rep
		 
		
	 print(word)
			
