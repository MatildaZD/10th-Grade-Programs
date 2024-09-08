
f = open("deniro.csv", 'r')
listOfLines = f.readlines()
moviesByYear = {} #create two dictionaries
scoresByTitle = {}
x1 = []
for i in range(1, len(listOfLines)):
  #extract information
  line = listOfLines[i]
  titleSplit = line.split('"')
  nameTitle = titleSplit[1]
  DateScore = titleSplit[0].split(", ")
  score = float(DateScore[1])
  Date = int(DateScore[0])

  #for the graph of movies per year
  if Date not in x1: #make sure there are no duplicates 
  	x1.append(Date) #makes a list of all the dates to use later 


  #update dictionaries
  scoresByTitle[nameTitle] = score #insert movie as key, score as value
  if Date in moviesByYear:#if we already have a movie in this year
    moviesByYear[Date].append(nameTitle) #append new title to list
  else:#if this is the first movie that year
    moviesByYear[Date] = [nameTitle] #insert key year with value list containing one title

  	#The number of movies Robert De Niro appeared in each year
def numberPerYear(year):
	list1 = moviesByYear[year]
	final = len(list1)
	return final

	#The average Rotten Tomatoes score of De Niro's movies each year.
def AveragePerYear(year):
	listOfScores = []
	total = 0
	for i in moviesByYear[year]:
	 listOfScores.append(scoresByTitle[i])
	 total += scoresByTitle[i]
	 average = total/len(listOfScores)
	return average



y1 = []
y2 = []
for i in x1:
	y1.append(numberPerYear(i))
	y2.append(AveragePerYear(i))
	
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
#now that we have x1 and y1,y2 coordinates, all thats left to do is graph
plt.bar(x1, y1)
plt.xticks(x1, x1, rotation='vertical')
plt.xlabel('Years')
plt.ylabel('Number Of Movies Made')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(x1,y2, "r")
plt.xticks(x1, x1, rotation='vertical')
plt.xlabel('Years')
plt.ylabel('Average Score Of Movies')
plt.show()


f.close()