import os
import pygame
###########################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang") # 게임 이름

# FPS
clock = pygame.time.Clock()
###########################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, ,속도, 폰트 등)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 캐릭터가 위치하도록 (가로)
character_y_pos = screen_height - character_height - stage_height # stage 바로 위에서 생성하도록 stage 높이도 빼기

# 이동할 좌표
character_to_x = 0

# 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 적 enemy 캐릭터

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴

# 이벤트 루프 (게임 창이 안꺼지게)
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x * dt # 프레임에 따라 이동속도 차이가 나면 안되기 때문에 값을 고정해줌으로써 프레임이 달라도 이동속도가 일정하게 고정함

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
###############어려운 부분#################################
    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140, ....
    # 500, 200 -> 180, 160, 140, ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로
    
    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
###############어려운 부분#################################
    # 4. 충돌 처리

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 충돌 체크
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기 x = 0, y = 0 좌표에 그림을 넣어주면 그림이 우측아래로 그려지니까 꽉차게됨
    ###############어려운 부분#################################
    for weapon_x_pos, weapon_y_pos in weapons: # 순서대로 그려지기 때문에 무기를 캐릭터 뒤로 가게 하려면 먼저 그리도록 해야함
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    ###############어려운 부분#################################
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos)) # 생성할 객체, 생성 좌표
    
    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임 화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)
# pygame 종료
pygame.quit()