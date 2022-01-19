import pygame
from random import *
# 초기화
pygame.init()
# 게임 화면
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
# 게임 이름
pygame.display.set_caption("똥 피하기")
# FPS
clock = pygame.time.Clock()
# 배경화면
background = pygame.image.load("C:\\Users\\kimpa\\Desktop\\Pythonworkspace\\pygame_basic\\background.png")
# 캐릭터 이미지 가져오고 사이즈 확인 및 생성 위치 확인
character = pygame.image.load("C:\\Users\\kimpa\\Desktop\\Pythonworkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
# 이동할 좌표
to_x = 0 # 이동은 character가 x 좌표만 이동이 될꺼라 to_x 만 있으면 됨

# 이동속도
character_speed = 0.6
enemy_speed = 0.6
# 적 생성 세로 맨위에서 랜덤 생성
enemy = pygame.image.load("C:\\Users\\kimpa\\Desktop\\Pythonworkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0 # 창의 맨 위라서 0

# 이벤트 루프
running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    # 캐릭터 위치 정의
    character_x_pos += to_x * dt
    # 똥은 위에서 아래로 계속 떨어질꺼니까 그냥 똥의 y 위치에서 speed를 더해주면 됨
    enemy_y_pos += enemy_speed * dt
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0 # 똥이 화면 밖을 나가면 맨위로 되돌아오게
        enemy_x_pos = randint(0, screen_width - enemy_width) # 똥이 화면 밖을 나가면 x 좌표 랜덤으로 재생성
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect): # 캐릭터와 적이 충돌했는가?
        print("충돌")
        running = False
    # 그림 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

pygame.quit()