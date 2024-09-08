import pygame, sys, pymunk, random, pymunk.pygame_util, math


shipImg = pygame.image.load('ship.png')
shipImg = pygame.transform.scale(shipImg, (15, 30))
#bring in ship image 

sizeList = []
massList = []
bodyList = []
shapeList = []
gravityList = []
#create lists for pymunk attributes


def makeShip(x,y):
	pygame.draw.circle(screen,(0,0,0),(x+7,y+13),12)
	screen.blit(shipImg, (x,y)) #simple function that draws the ship at mouse pos

def randomMass():
	aMass = random.randint(1,10)
	massList.append(aMass)
	return aMass #create a random mass and append to mass list

def randomSize(): 
	aSize = random.randint(20,150)
	sizeList.append(aSize)
	return aSize #create a random size and append to size list

def createBody(pos): 
	body = pymunk.Body(1,randomMass(),body_type = pymunk.Body.DYNAMIC)
	#create the pymunk body with a random mass
	body.position = pos
	#put the body position at the pos variable
	#which is a random location based on the input for the function
	bodyList.append(body)
	
	return body

def newAsteroid():
	#this checking system pretty much makes it spawn in locations that
	#make sense for which direction it will go in
	#so if the body is spawned above the screen, the gravitational pull will
	#go downward 
	if check == 1: 
		body = createBody((random.randint(-300,800),random.randint(-800,-300)))
	if check == 2: 
		body = createBody((random.randint(-300,800),random.randint(800,1100)))
	if check == 3: 
		body = createBody((random.randint(-400,-100),random.randint(-300,1000)))
	if check == 4: 
		body = createBody((random.randint(800,1100),random.randint(-300,1000)))
	shape = pymunk.Circle(body,randomSize())
	#create a random shape with one of the bodies with a random size
	shapeList.append(shape)
	#this shape is then appended to a shape list
	space.add(body,shape)
	#the shape and a body that corresponds to it is added to the space.
	#the location of this shape and its many attributes are stored
	#in the lists in the beginning, so I can use them later 
	if check == 1: 
		gravX = random.randrange(-100,100)
		gravY = random.randrange(10,100)
	if check == 2: 
		gravX = random.randrange(-100,100)
		gravY = random.randrange(-100,-10)
	if check == 3:
		gravX = random.randrange(10,100)
		gravY = random.randrange(-100,100)
	if check == 4: 
		gravX = random.randrange(-100,-10)
		gravY = random.randrange(-100,100)
	gravityList.append((gravX,gravY))

	return shape

asteroidImg = pygame.image.load('asteroid.png')
def spawnAsteroid(asteroids):
	for i in range(len(asteroids)):
		#this function updates the velocity for all the items
		#this is what gives it the affect of different speeds
		#becuase the amount of gravity is different for each one
		#it updates the bodies accordingly as well, so for each body
		#it adds a gravity, this gravity is also stored
		pymunk.Body.update_velocity(bodyList[i],gravityList[i], 1,.1)
	
		pos_x = int(shapeList[i].body.position.x)
		pos_y = int(shapeList[i].body.position.y)#need to be ints 
		
		#this created the asteroid image at the specific location of the physics
		#object, otherwise it wouldnt be visible.
		#this was really the hardest part, becuase I had to keep track of all
		#this information so I could spawn them visually correctly so the game 
		#would actually be playable
		NewasteroidImg = pygame.transform.scale(asteroidImg,(sizeList[i]*2,sizeList[i]*2))
		screen.blit(NewasteroidImg, (pos_x-sizeList[i],pos_y-sizeList[i]))
		#The positions are moved becase they spawn in the top right of the location. 
		
	

pygame.init()
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()
#create the pygame display surface 
screen = pygame.display.set_mode((600,600))
#create pymunk game space
space = pymunk.Space()
#space.gravity = (0,1000) #create gravity in space

asteroids = []

while True:

	time_elapsed_since_last_action += clock.tick()

	#working with collisions 
	x,y = pygame.mouse.get_pos()
	for i in range(len(asteroids)):
		distance = math.hypot(shapeList[i].body.position.x - x,shapeList[i].body.position.y-y)
		#if the distances between the two in the center (distance formula)
		#is smaller than the two radii added together, then they are colliding
		if distance < 15 + sizeList[i]:
			pygame.quit()
			sys.exit()
			

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill((0,0,0))#set color 

	if time_elapsed_since_last_action > 10: 
		check = random.randint(1,4)#make the random check
		asteroids.append(newAsteroid())#add a new asteroid to the list
		check = random.randint(1,4)#do it twice 
		asteroids.append(newAsteroid())
		
		time_elapsed_since_last_action = 0


	spawnAsteroid(asteroids) #always calling the spawn asteroids function
	#so any asteroid in the list is called 
	makeShip(x,y)
	space.step(1/50)#updating the pymunk space
	clock.tick(30) #fps
	pygame.display.update()





