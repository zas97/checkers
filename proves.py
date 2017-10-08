import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                image = pygame.transform.scale(image, (75, 63))
                _image_library[path] = image
        return image


def prova(ax):
    ax[0]=-7

pygame.init()
screen = pygame.display.set_mode((600, 504))
done = False
isBlue=True
x=[30]
y=30
clock = pygame.time.Clock()
moves=None
for i in x:
    print(i)
aux=(1,2)
ax=[1,2]
prova(ax)
print(ax)
x=5



while not done:
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if event.type == pygame.QUIT:
            done = True
        if pygame.mouse.get_pressed()[0]:
            (x,y)=pygame.mouse.get_pos()
            screen.fill(pygame.Color("black"))
            for i in range(0, 8):
                for j in range(0, 8):
                    if (i + j) % 2 == 0:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)
                    pygame.draw.rect(screen, color, pygame.Rect(i * 75, j * 63, 75, 63))
            screen.blit(get_image("images/KingBlack.png"), (x, y))
            pygame.display.flip()


    clock.tick(30)