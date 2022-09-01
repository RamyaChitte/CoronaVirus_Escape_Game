import pygame
import random

screen_size = [200,480]
screen=pygame.display.set_mode(screen_size)
pygame.font.init()

background=pygame.image.load('bg.png')
user=pygame.image.load('user.png')
virus=pygame.image.load('virus.png')

def display_score(score):
  font=pygame.font.SysFont('Comic Sans MS',30)
  score_text='Score: '+str(score)
  text_img=font.render(score_text,True,(255,0,0))
  screen.blit(text_img,[10,10])

def rand_offset():
  return -1*random.randint(100,800)

def infect(idx):
  global score
  global keep_alive
  score=score-20
  print("infected by Virus ",idx,score)
  virus_y[idx]=rand_offset()
  if(score<=-20):
    keep_alive=False

virus_y=[rand_offset(),rand_offset(),rand_offset()]
user_x=80
score=0

def update_pos(idx):
  global score
  if virus_y[idx]>480:
     virus_y[idx]=rand_offset()
     score=score+5
     print('score',score)
  else:
     virus_y[idx]+=3

keep_alive = True
clock=pygame.time.Clock()
while keep_alive:
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and user_x < 150:
      user_x = user_x + 6
  elif keys[pygame.K_LEFT] and user_x > 0:
      user_x = user_x - 6
  update_pos(0)
  update_pos(1)
  update_pos(2)
  
  screen.blit(background,[0,0])
  screen.blit(user,[user_x,295])
  screen.blit(virus,[5,virus_y[0]])
  screen.blit(virus,[80,virus_y[1]])
  screen.blit(virus,[145,virus_y[2]])

  if virus_y[0]>480 and user_x < 40:
    infect(0)
  if virus_y[1]>480 and user_x > 65 and user_x < 95:
    infect(1)
  if virus_y[2]>480 and user_x > 110:
    infect(2)

  display_score(score)
  pygame.display.update()
  clock.tick(90)
