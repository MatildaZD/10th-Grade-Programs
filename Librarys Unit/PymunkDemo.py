import pygame, sys, pymunk
#import pygame,system commands, pymunk

def newCircle(space,pos): #needs the space argument 
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC) #create a body 
                        #arguments are: mass, interia, body type 
    body.position = pos
    shape = pymunk.Circle(body,50) #make new shape, arguments: body, radius
    space.add(body,shape) #adds the shape to the space
    return shape

def drawCircles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50) #gives you the center of the shape
                            #place to spawn, color, center, radius

def staticBody(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC) #is static
    body.position = pos
    shape = pymunk.Circle(body,50)

    space.add(body, shape)
    return shape

def drawStatic(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),50)


#general setup: 
pygame.init()
clock = pygame.time.Clock()

#create the pygame display surface 
screen = pygame.display.set_mode((600,600))

#create pymunk game space
space = pymunk.Space()
space.gravity = (0,1000) #create gravity in space

circles = []


balls = []
balls.append(staticBody(space, (500,500)))
balls.append(staticBody(space, (300,500)))

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            circles.append(newCircle(space,event.pos))

    screen.fill((200,200,200)) 

    space.step(1/50)#updating the pymunk space
    drawCircles(circles)
    drawStatic(balls)

    pygame.display.flip()
    clock.tick(30)