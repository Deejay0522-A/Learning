import pygame

pygame.init()

access = input("Which type of control are you using? \ncontroller = controller input \nkeyboard = keyboard input")

if access == "controller":
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        raise RuntimeError("No controller connected")
elif access == "keyboard":
    pass

controller = pygame.joystick.Joystick(0)
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
controller.init()

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            break

    x = controller.get_axis(0)
    y = controller.get_axis(1)

    deadzone = 0.15
    if abs(x) < deadzone:
        x = 0
    if abs(y) < deadzone:
        y = 0

    pygame.display.flip()
    clock.tick(60)
quit()