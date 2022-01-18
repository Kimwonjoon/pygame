import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\kimpa\\Desktop\\Pythonworkspace\\pygame_basic\\background.png")

# 이벤트 루프 (게임 창이 안꺼지게)
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
    # screen.fill((0, 0, 255)) # RGB 값으로 배경 채우기 R, G는 0 이니까 색이 없고 B 만 최대값 255로 넣었기 때문에 배경은 파란색이 됨
    screen.blit(background, (0, 0)) # 배경 그리기 x = 0, y = 0 좌표에 그림을 넣어주면 그림이 우측아래로 그려지니까 꽉차게됨

    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료
pygame.quit()