import pygame
import time
from winsound import Beep as beep
pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("Pygame Timer")
white = (225,225,225)
win.fill(white)
font = pygame.font.SysFont('arial',40)
h = 0
m = 0
s = 0
secondsfortimer = 0
currenttime = "{}:{}:{}".format(h,m,s)
print('press "m" to add a minute, "s" to add a second, "h" to add an hour, "c" to reset the timer to 0:0:0, and "t" to start the timer.')
class timer(): #all the timer functions
    def func():
        global h
        global s
        global m
        if h < 10:
            h = "0"+str(h)
        if s < 10:
            s = "0"+str(s)
        if m < 10:
            m = "0"+str(m)
    def changetime(): # updates the time
        global h
        global s
        global m
        timer.func()
        currenttime = "{}:{}:{}".format(h,m,s)
        win.fill(white)
        text = font.render(currenttime,True,(0,0,0))
        x = text.get_width()
        win.blit(text,(200-(x/2),150))
        pygame.display.update()
        try:
            int(h)
        except:
            secondsfortimer = 0
        else:
            h = int(h)
        try:
            int(s)
        except:
            secondsfortimer = 0
        else:
            s = int(s)
        try:
            int(m)
        except:
            secondsfortimer = 0
        else:
            m = int(m)
    def addminute():
        global m
        global secondsfortimer
        m += 1
        secondsfortimer += 60
        if m == 60:
            m = 0
            secondsfortimer -= 3600
        timer.changetime()
    def addsecond():
        global s
        global secondsfortimer
        s += 1
        secondsfortimer += 1
        if s == 60:
            s = 0
            secondsfortimer -= 60
        timer.changetime()
    def addhour():
        global h
        global secondsfortimer
        h += 1
        secondsfortimer += 3600
        if h == 100:
            h = 0
            secondsfortimer -= 360000
        timer.changetime()
    def clear(): #resets the timer to 0:0:0
        global m
        global h
        global s
        global secondsfortimer
        m = 0
        h = 0
        s = 0
        secondsfortimer = 0
        timer.changetime()
running = True
timeron = False
timer.changetime()
minute = False
second = False
hour = False
clock = pygame.time.Clock()
while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            running = False
        if eve.type == pygame.KEYDOWN:
            #what happens if you press certain buttons
            if eve.key == pygame.K_m:
                minute = True
            elif eve.key == pygame.K_h:
                hour = True
            elif eve.key == pygame.K_s:
                second = True
            elif eve.key == pygame.K_c:
                timer.clear()
            elif eve.key == pygame.K_t: #what happens when you press t (starts or stops the timer)
                timeron = True
                start = time.time()
                pasttime = currenttime
                while timeron:
                    if secondsfortimer <= 0:
                        timer.clear()
                        beep(880,3000)
                        break
                    secondsfortimer -= 1
                    s -= 1
                    if s ==-1:
                        s = 59
                        m -= 1
                        if m ==-1:
                            m = 59
                            h -= 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            timeron = False
                            running = False
                            pygame.quit()
                            break
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_t:
                                timeron = False
                                break
                    if timeron == False:
                        break
                    clock.tick(1)
                    timer.changetime()
        if eve.type == pygame.KEYUP:
            #what happens if you don't press certain buttons
            if eve.key == pygame.K_m:
                minute = False
            if eve.key == pygame.K_h:
                hour = False
            if eve.key == pygame.K_s:
                second = False
    if minute == True:
        timer.addminute()
    elif second == True:
        timer.addsecond()
    elif hour == True:
        timer.addhour()
    elif running == False:
        break
    clock.tick(10)
pygame.quit()
