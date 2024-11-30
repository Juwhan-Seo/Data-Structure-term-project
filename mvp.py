import pygame
import heapq

# 초기화
pygame.init()

# 화면 크기
width, height = 600, 600  
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("최단거리 탐색 알고리즘 시각화")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)

# 기본 사각형 그리드의 크기를 설정 (3x3 ~ 9x9)
def get_grid_size():
    try:
        size = input("그리드 크기를 입력하세요 (3-9 사이, 엔터 입력 시 기본 3x3): ")
        if size == "":
            return 3  # 기본 크기 3x3
        size = int(size)
        if 3 <= size <= 9:
            return size
        else:
            print("3과 9 사이의 값을 입력하세요.")
            return 3  # 잘못된 입력시 기본값
    except ValueError:
        print("잘못된 입력입니다. 기본 3x3으로 설정합니다.")
        return 3

#그리기
def draw_grid(rows, cols):
    square_width = width // cols
    square_height = height // rows
    
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * square_width, row * square_height, square_width, square_height)
            pygame.draw.rect(screen, BLACK, rect, 1)
            


# 시작 버튼 그리기
def draw_start_button():
    font = pygame.font.SysFont(None, 40)
    button_rect = pygame.Rect(width // 2 - 50, height - 70, 100, 50)
    pygame.draw.rect(screen, GREY, button_rect)
    text = font.render("Start", True, BLACK)
    screen.blit(text, (width // 2 - 30, height - 60))
    return button_rect







# 메인 루프
def main():
    # 그리드 크기 설정
    grid_size = get_grid_size()  # 3x3 ~ 9x9
    rows, cols = grid_size, grid_size

    running = True
    screen.fill(WHITE)
    draw_grid(rows, cols)
    start_button = draw_start_button()  # 시작 버튼 그리기
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
