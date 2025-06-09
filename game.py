import pygame
pygame.init()

pygame.display.set_caption('examen 111')
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('public/track6.png')
car = pygame.image.load('public/tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
drive = True
clock = pygame.time.Clock()
direction = 'up'
mov = False

def mover(m):
    global car_x, car_y
    a = -1 if m else 1
    if direction == 'up' and up_px == 255:
        car_y -= 4
    elif direction == 'down' and down_px == 255:
        car_y += 4
    elif direction == 'right' and (right_px == 255 or left_px == 255):
        car_x += 4 * a

def girar1():
    global direction, car, car_x, car_y, cam_x_offset, cam_y_offset
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x += 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y += 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x += 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)

def girar2(m, x_px):
    global direction, car, car_x, car_y, cam_x_offset, cam_y_offset
    a = -1 if m else 1
    if direction == 'up' and up_px != 255 and x_px == 255:
        direction = 'right'
        #print(cam_x_offset)
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and x_px != 255 and down_px == 255:
        direction = 'down'
        cam_y_offset = 30
        car = pygame.transform.rotate(car, 90)
        #print(cam_x_offset)
    elif direction == 'down' and down_px != 255 and x_px == 255:
        direction = 'right'
        car_y += 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, -90)
        #print(cam_x_offset)
    elif direction == 'right' and x_px != 255 and up_px == 255:
        direction = 'up'
        print(cam_x_offset)
        car = pygame.transform.rotate(car, -90)
    
    
while drive:
    prev_x = car_x
    prev_y = car_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode == 'q': drive = False

    cam_x = car_x +cam_x_offset+ 15
    cam_y = car_y + cam_y_offset + 15

    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    left_px = window.get_at((cam_x - focal_dis-4, cam_y))[0]
    girar1() if not mov else girar2(mov, left_px)
    

    mover(mov)
    if prev_x == car_x != 150 and prev_y == car_y != 300 and not mov:
        print(car_x, car_y)
        mov = True
        if direction == 'up':
            direction = 'down'
            car = pygame.transform.rotate(car, 180)
            cam_y_offset = 30

        elif direction == 'down':
            direction = 'up'
            car = pygame.transform.rotate(car, 180)
            cam_y_offset = 0
        else:
            car = pygame.transform.rotate(car, 90)
            
        


    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y)) if mov else None
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5) if mov else None
    pygame.display.update()
    clock.tick(60 if mov else 0)