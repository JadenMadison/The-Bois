import sys,pygame
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) =(int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode (size)
clock = pygame.time.Clock()
colour = (32,0,255)

fimage = pygame.image.load("fish.png")
fimage = pygame.transform.smoothscale(fimage,(120, 60))

fishy_rect = fimage.get_rect()

fishy_rect.center = (width//2,height//2)

speed = pygame.math.Vector2(0,0)

def movethanos():
    global fimage
    fishy_rect.move_ip(speed)
    if fishy_rect.bottom > height or fishy_rect.top < 0:
        speed[1] *= -1
        fimage = pygame.transform.flip(fimage,False,True)
    if fishy_rect.right > width or fishy_rect.left < 0:
        speed[0] *= -1
        fimage = pygame.transform.flip(fimage,True,False)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    speed[0] += -3
                if event.key == pygame.K_d:
                    speed[0] += 3
                if event.key == pygame.K_w:
                    speed[1] += -3
                if event.key == pygame.K_s:
                    speed[1] += 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    speed[0] = 0
                if event.key == pygame.K_d:
                    speed[0] = 0
                if event.key == pygame.K_w:
                    speed[1] = 0
                if event.key == pygame.K_s:
                    speed[1] = 0

            clock.tick(60)
            movethanos()
            screen.fill(colour)
            screen.blit(fimage,fishy_rect)
            pygame.display.flip()
if __name__ == "__main__":
    main()
