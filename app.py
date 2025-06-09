import pygame
pygame.init()
n = input()
pygame.display.set_caption('examen 111')
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load(f'public/track{n}.png')
car = pygame.image.load('public/tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
mov = False

def girar(x_px, m):
    global direction, car, car_x, car_y, cam_x_offset, cam_y_offset
    a = -1 if m else 1
    if direction == 'up' and up_px != 255 and x_px == 255:
        direction = 'right'
        cam_x_offset = 0 if m else 30
        car = pygame.transform.rotate(car, -90*a)
    elif direction == 'right' and x_px != 255 and down_px == 255:
        direction = 'down'
        car_x += 0 if m else 30
        cam_y_offset = 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, -90*a)
    elif direction == 'down' and down_px != 255 and x_px == 255:
        direction = 'right'
        car_y += 30
        cam_y_offset = 0
        cam_x_offset = 0 if m else 30
        car = pygame.transform.rotate(car, 90*a)
    elif direction == 'right' and x_px != 255 and up_px == 255:
        direction = 'up'
        car_x += 0 if m else 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90*a)

def mover(m):
    global car_x, car_y
    a = -1 if m else 1
    if direction == 'up' and up_px == 255:
        car_y -= 4
    elif direction == 'down' and down_px == 255:
        car_y += 4
    elif direction == 'right' and (right_px == 255 or left_px == 255):
        car_x += 4 * a

while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: drive = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'q': drive = False

    prev_x = car_x
    prev_y = car_y
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15

    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    left_px = window.get_at((cam_x - focal_dis-4, cam_y))[0]

    girar(left_px if mov else right_px, mov)
    mover(mov)

    if prev_x == car_x != 150 and prev_y == car_y != 300 and not mov:
        print(car_x, car_y)
        mov = True
        if direction in ('up', 'down'):
            direction = 'up' if direction == 'down' else 'down'
            car = pygame.transform.rotate(car, 180)
            cam_y_offset = 0 if direction == 'up' else 30
        else:
            car = pygame.transform.rotate(car, 90)
    
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y)) if mov else None
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5) if mov else None
    pygame.display.update()
    clock.tick(70 if mov else 0)