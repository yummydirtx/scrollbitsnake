def on_button_pressed_a():
    global direction
    if direction == 0:
        direction = 3
    elif direction == 1:
        direction = 0
    elif direction == 2:
        direction = 1
    elif direction == 3:
        direction = 2

def on_button_pressed_b():
    global direction
    if direction == 0:
        direction = 1
    elif direction == 1:
        direction = 2
    elif direction == 2:
        direction = 3
    elif direction == 3:
        direction = 0
ppFlag = False
rand2 = 0
rand1 = 0
direction = 0
# cooper
length = 1
snakeLocation = [0, 0]
dead = True
firstPass = True
def drawSnake(snakeLocation: List[number]):
    # clear the screen before drawing
    scrollbit.clear()
    # repeat this for every pair of coordinates
    for x in range(len(snakeLocation) / 2):
        # if x is length divided by two it has to be multiplied again
        scrollbit.set_pixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1], 50)
    scrollbit.set_pixel(snakeLocation[len(snakeLocation) - 2],
        snakeLocation[len(snakeLocation) - 1])
    scrollbit.set_pixel(rand2, rand1)
    # show the world
    scrollbit.show()
def moveSnake(snakeLocation: List[number], direction: number, length: number):
    # if going to the right
    if direction == 0:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] + 1)
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
    elif direction == 1:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] + 1)
    elif direction == 2:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] - 1)
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
    elif direction == 3:
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2])
        snakeLocation.append(snakeLocation[len(snakeLocation) - 2] - 1)
    while len(snakeLocation) / 2 > length:
        # remove extra snake
        snakeLocation = snakeLocation.slice(2)
    return snakeLocation
def food(snakeLocation: List[number]):
    global length, rand1, rand2
    if snakeLocation[len(snakeLocation) - 2] == rand2 and snakeLocation[len(snakeLocation) - 1] == rand1:
        length = length + 1
        rand1 = randint(0, 6)
        rand2 = randint(0, 16)
    return length
drawSnake(snakeLocation)
def checkContact(snakeLocation: List[number]):
    contact = False
    frontX = snakeLocation[len(snakeLocation) - 2]
    frontY = snakeLocation[len(snakeLocation) - 1]
    for x2 in range(len(snakeLocation) / 2 - 1):
        if frontX == snakeLocation[x2 * 2]:
            if frontY == snakeLocation[x2 * 2 + 1]:
                contact = True
    return contact
def checkDeath(snakeLocation: List[number]):
    death = checkContact(snakeLocation)
    if snakeLocation[len(snakeLocation) - 1] > 6 or snakeLocation[len(snakeLocation) - 2] > 16:
        death = True
    if snakeLocation[len(snakeLocation) - 1] < 0 or snakeLocation[len(snakeLocation) - 2] < 0:
        death = True
    return death
while True:
    if not (dead):
        food(snakeLocation)
        snakeLocation = moveSnake(snakeLocation, direction, length)
        if checkDeath(snakeLocation):
            direction = 0
            # cooper
            length = 1
            rand1 = 0
            rand2 = 0
            snakeLocation = [0, 0]
            dead = True
            scrollbit.scroll_text("GAME OVER", 100, 10)
        drawSnake(snakeLocation)
        for index in range(200):
            if ppFlag == False:
                if input.button_is_pressed(Button.A):
                    on_button_pressed_a()
                    ppFlag = True
                if input.button_is_pressed(Button.B):
                    on_button_pressed_b()
                    ppFlag = True
            basic.pause(1)
        ppFlag = False
    else:
        if firstPass:
            scrollbit.scroll_text("MicroSnake", 100, 50)
            scrollbit.show()
            scrollbit.scroll_text("Alex Frutkin and Cooper Weissman", 100, 20)
            scrollbit.show()
            firstPass = False
        scrollbit.scroll_text("PRESS ANY BUTTON", 100, 20)
        for pp in range(1000):
            if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                dead = False
                pp = 1000
            basic.pause(1)