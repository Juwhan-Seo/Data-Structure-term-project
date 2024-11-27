import pygame

# 초기화
pygame.init()

# 화면 크기
width, height = 600, 600  
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("최단거리 탐색 알고리즘 시각화")

# 색
w = (255, 255, 255)
b = (0, 0, 0)
g = (200, 200, 200)

# 기본 사각형 칸 설정
ROWS, COLS = 3, 3

# 크기 입력 받기
def square_size():
    while True:
        user_input = input('row와 col을 정해주세요(예시: 3*3을 만들고 싶다면 3, 3 입력):')
        
        if user_input == "":
            return 3, 3
        
        rows, cols = map(int, user_input.split(','))

        return rows, cols

#그리기
def draw_squares(rows, cols):
    screen.fill(w)
    
    square_width = width // cols  # 각 사각형의 너비
    square_height = height // rows  # 각 사각형의 높이

    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * square_width, row * square_height, square_width, square_height)
            pygame.draw.rect(w, b, rect, 3)  # 테두리 두께(3)
    
    pygame.display.update()


