import pygame
import networkx as nx
import numpy as np
import random

# 화면 설정
screen_size = (600, 600)
background_color = (255, 255, 255)
wall_color = (0, 0, 0)
path_color = (0, 255, 0, 100)  # 경로 색상 (반투명 초록색)
ai_color = (0, 255, 0)  # AI 색상 (초록색)
exit_color = (0, 255, 0)  # 탈출 지점 색상 (초록색)

# 미로 생성 함수
def create_random_maze(width, height):
    maze = np.ones((height, width))
    stack = [(1, 1)]
    maze[1, 1] = 0

    while stack:
        current = stack[-1]
        neighbors = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 1 <= nx < height and 1 <= ny < width and maze[nx, ny] == 1:
                neighbors.append((nx, ny))

        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
            maze[next_cell[0], next_cell[1]] = 0
            maze[(current[0] + next_cell[0]) // 2, (current[1] + next_cell[1]) // 2] = 0
        else:
            stack.pop()

    maze[1, 1] = 0  # 시작점
    maze[height - 2, width - 2] = 0  # 목표점
    return maze

# 미로를 그래프로 변환
def maze_to_graph(maze):
    G = nx.grid_2d_graph(*maze.shape)
    for (i, j) in list(G.nodes):
        if maze[i, j] == 1:
            G.remove_node((i, j))
    return G

# 최적 경로 찾기
def find_path(G, start, goal):
    try:
        path = nx.shortest_path(G, source=start, target=goal, method='dijkstra')
    except nx.NetworkXNoPath:
        path = None
    return path

# 미로 시각화 및 경로 표시
def draw_maze(screen, maze, path=None, exit_point=None):
    block_size = screen_size[0] // maze.shape[0]
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            color = background_color if maze[i, j] == 0 else wall_color
            pygame.draw.rect(screen, color, pygame.Rect(j*block_size, i*block_size, block_size, block_size))
    
    if path:
        for (i, j) in path:
            pygame.draw.rect(screen, path_color[:3], pygame.Rect(j*block_size, i*block_size, block_size, block_size))

    if exit_point:
        pygame.draw.rect(screen, exit_color, pygame.Rect(exit_point[1]*block_size, exit_point[0]*block_size, block_size, block_size))

# AI 이동 표시
def move_ai(screen, maze, path):
    block_size = screen_size[0] // maze.shape[0]
    if path:
        for (i, j) in path:
            pygame.draw.rect(screen, ai_color, pygame.Rect(j*block_size, i*block_size, block_size, block_size))
            pygame.display.flip()
            pygame.time.delay(300)  # 속도 조절

# 초기 설정
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Maze Escape AI")
clock = pygame.time.Clock()

# 미로 생성
maze_width, maze_height = 31, 31
maze = create_random_maze(maze_width, maze_height)

# 시작점과 목표점 설정
start, goal = (1, 1), (maze_height - 2, maze_width - 2)

# 미로를 그래프로 변환 및 경로 계산
G = maze_to_graph(maze)
path = find_path(G, start, goal)

# 메인 루프
running = True
path_index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # 'r' 키를 눌러 새로운 미로 생성
                maze = create_random_maze(maze_width, maze_height)
                G = maze_to_graph(maze)
                path = find_path(G, start, goal)
                path_index = 0
    
    screen.fill(background_color)
    draw_maze(screen, maze, path[:path_index], exit_point=goal)
    if path and path_index < len(path):
        path_index += 1
    pygame.display.flip()
    clock.tick(5)  # 5 FPS로 설정

pygame.quit()
