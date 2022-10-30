import pygame
from pygame.locals import DOUBLEBUF, QUIT, KEYUP, K_ESCAPE
import sys

pygame.init()

# 디스플레이 초기화
DISPLAYSURF = pygame.display.set_mode((640, 480), DOUBLEBUF)
pygame.display.set_caption("등축 투영")


# 맵 데이터: (1) 벽, (0) 바닥
map_data = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

# 타일 이미지 로드
wall = pygame.image.load("map_tset01.png").convert_alpha()
grass = pygame.image.load("map_test02.png").convert_alpha()
TILEWIDTH = 64  # 타일 너비
TILEHEIGHT = 64  # 타일 높이
TILEHEIGHT_HALF = TILEHEIGHT / 2
TILEWIDTH_HALF = TILEWIDTH / 2

# 타일 배치
for row_nb, row in enumerate(map_data):
    for col_nb, tile in enumerate(row):
        if tile == 1:
            tileImage = wall
        else:
            tileImage = grass
        cart_x = row_nb * TILEWIDTH_HALF
        cart_y = col_nb * TILEHEIGHT_HALF
        iso_x = cart_x - cart_y
        iso_y = (cart_x + cart_y) / 2
        centered_x = DISPLAYSURF.get_rect().centerx + iso_x
        centered_y = DISPLAYSURF.get_rect().centery / 2 + iso_y
        DISPLAYSURF.blit(tileImage, (centered_x, centered_y))

# 게임 실행
FPSCLOCK = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    FPSCLOCK.tick(30)