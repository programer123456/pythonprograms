import pygame,time
pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("Pygame Stopwatch")
white = (225,225,225)
win.fill(white)
h = 0
s = 0
m = 0
currenttime = "{}:{}:{}".format(h,m,s)
font = pygame.font.SysFont('arial',40)
class Stopwatch():
    def func():
        global h
        global s
        global m
        global currenttime
        global text
        if h < 10:
            h = "0"+str(h)
        if s < 10:
            s = "0"+str(s)
        if m < 10:
            m = "0"+str(m)
        text = font.render(currenttime,True,(0,0,0))
        currenttime = "{}:{}:{}".format(h,m,s)
    def changetime():
        global h
        global s
        global m
        global currenttime
        Stopwatch.func()
        win.fill(white)
        win.blit(text,(150,150))
        pygame.display.update()
        h = int(h)
        s = int(s)
        m = int(m)
    def clear():
        global h
        global s
        global m
        m = 0
        s = 0
        h = 0
        Stopwatch.changetime()
#This is the main code that runs the stopwatch
running = True
Stopwatch.changetime()
ston = False
while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            running = False
            break
        elif eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_c:
                Stopwatch.clear()
            elif eve.key == pygame.K_s:
                ston = True
                start = time.time()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            ston = False
                            running = False
                            break
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                            ston = False
                            break
                    if time.time() - start >=0.995:
                        start = time.time()
                        s += 1
                        if s == 60:
                            s = 0
                            m += 1
                            if m == 60:
                                m = 0
                                h += 1
                                if h == 99:
                                    Stopwatch.clear()
                    if ston == False:
                        break
                    Stopwatch.changetime()
    if running == False:
        pygame.quit()
        break
    pygame.display.update()
pygame.quit()
