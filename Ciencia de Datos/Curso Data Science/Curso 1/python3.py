#Ejercicio 1 (Conditions)
age= 18
if(age>18):
	print("You can enter")
elif(age==18):
	print("Go see Pink Floyd")
else:
	print("You can't enter")
print("Move on")

#Ejercicio 2
rating= 8.5
if(rating>8):
	print("This album is amazing!")
elif(rating==8):
	print("This album is ok")
else:
	print("This album sucks!")

#Ejercicio 3
album_year= 1980
if(album_year==1980) or (album_year==1991) or (album_year==1993):
	print("This album came out in the year", album_year)

#Ejericio 4 (Loops)
number= 5
for x in range(-4,5):
	print(x)

#Ejercicio 5
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

#Ejercicio 6
squares= ['red','yellow','green','purple','blue']
for square in squares:
	print(square)

#Ejercicio 7
PlayListRatings= [10,9.5,10,8,7.5,5,10,10]
i=0
rating= PlayListRatings[0]
while(i < len(PlayListRatings) and rating>=6):
	rating= PlayListRatings[i]
	print(rating)
	i= i+1

#Ejercicio 8
squares= ['orange','orange','purple','blue','orange']
new_squares= []
i= 0
while(i <len(squares) and squares[i] == 'orange'):
	new_squares.append(squares[i])
	i= i+1
print(new_squares)

#Ejercicio 9 (Functions)
def div(a, b):
	return(a/b)

#Ejercicio 10
def con(a, b):
	return(a + b)

#Ejercicio 11 (Exception Handling)
a= 1
try:
	b= int(input("Please enter a number to divide a"))
	a= a/b
	print("Success a=",a)
except:
	print("There was an error")

#Ejercicio 12 (Objects and Classes)
class analysedText(object):
	def _init_ (self,text):
		formattedText= text.replace('.',' ').replace('!',' ').replace('?',' ').replace(',',' ')
		formattedText = formattedText.lower()
		self.fmtText = formattedText
	def freqAll(self):
		wordList = self.fmtText.split(' ')
		freqMap = {}
		for word in set(wordList):
			freqMap[word] = wordList.count(word)
		return freqMap
	def freqOf(self,word):
		freqDict = self.freqAll()
		if word in freqDict:
			return freqDict[word]
		else:
			return 0




