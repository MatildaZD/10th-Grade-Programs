import pygame, sys, pymunk
def newCircle(space,pos): #needs the space argument 
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC) #create a body 
                        #arguments are: mass, interia, body type 
    body.position = pos
    shape = pymunk.Circle(body,50) #make new shape, arguments: body, radius
    space.add(body,shape) #adds the shape under the body type to the space
    return shape

def drawCircles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)#need to be ints 
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50) #gives you the center of the shape
                            #place to spawn, color, center, radius
        
       	#print(circle.body.position.y)

def makeSquare(space,pos):
	body = pymunk.Body(1,10000,body_type = pymunk.Body.STATIC) 
	body.position = pos
	w, h = 200,5
	vs = [(-w/2+100,-h/2), (w/2+100,-h/2), (w/2+100,h/2), (-w/2+100,h/2)]
	#this creates the square under the right location
	shape = pymunk.Poly(body, vs)
	space.add(body,shape)
	return shape

def drawSquare(squares):
	for square in squares:
		pos_x = int(square.body.position.x)
		pos_y = int(square.body.position.y)
		pygame.draw.rect(screen,(255,0,0),(pos_x,pos_y,200,5))




pygame.init()
clock = pygame.time.Clock()

#create the pygame display surface 
screen = pygame.display.set_mode((600,600))

#create pymunk game space
space = pymunk.Space()
space.gravity = (500,1000) #create gravity in space

squares = []
circles = []

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			circles.append(newCircle(space,event.pos))
		
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 :
			squares.append(makeSquare(space,event.pos))

			
	
	
	screen.fill((200,200,200))#set color 
	 
	space.step(1/50)#updating the pymunk space
	drawSquare(squares)
	drawCircles(circles)
	clock.tick(30) #fps
	pygame.display.update()










