let lengthfunc: number;
function on_button_pressed_a() {
    
    if (direction == 0) {
        direction = 3
    } else if (direction == 1) {
        direction = 0
    } else if (direction == 2) {
        direction = 1
    } else if (direction == 3) {
        direction = 2
    }
    
}

function on_button_pressed_b() {
    
    if (direction == 0) {
        direction = 1
    } else if (direction == 1) {
        direction = 2
    } else if (direction == 2) {
        direction = 3
    } else if (direction == 3) {
        direction = 0
    }
    
}

let ppFlag = false
let direction = 0
//  cooper
let length = 1
let snakeLocation = [0, 0]
function drawSnake(snakeLocation: number[]) {
    //  clear the screen before drawing
    scrollbit.clear()
    //  repeat this for every pair of coordinates
    for (let x = 0; x < snakeLocation.length / 2; x++) {
        //  if x is length divided by two it has to be multiplied again
        scrollbit.setPixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1], 50)
    }
    scrollbit.setPixel(snakeLocation[snakeLocation.length - 2], snakeLocation[snakeLocation.length - 1])
    //  show the world
    scrollbit.show()
}

function moveSnake(snakeLocation: number[], direction: number, length: number): number[] {
    //  if going to the right
    if (direction == 0) {
        snakeLocation.push(snakeLocation[snakeLocation.length - 2] + 1)
        snakeLocation.push(snakeLocation[snakeLocation.length - 2])
    } else if (direction == 1) {
        snakeLocation.push(snakeLocation[snakeLocation.length - 2])
        snakeLocation.push(snakeLocation[snakeLocation.length - 2] + 1)
    } else if (direction == 2) {
        snakeLocation.push(snakeLocation[snakeLocation.length - 2] - 1)
        snakeLocation.push(snakeLocation[snakeLocation.length - 2])
    } else if (direction == 3) {
        snakeLocation.push(snakeLocation[snakeLocation.length - 2])
        snakeLocation.push(snakeLocation[snakeLocation.length - 2] - 1)
    }
    
    while (snakeLocation.length / 2 > length) {
        //  remove extra snake
        snakeLocation = snakeLocation.slice(2)
    }
    return snakeLocation
}

function food() {
    
    if (snakeLocation[lengthfunc - 2] == 1 && snakeLocation[lengthfunc - 1] == 1) {
        length = length + .5
    }
    
    return length
}

drawSnake(snakeLocation)
function checkDeath(snakeLocation: any, lengthfunc: number): boolean {
    let death = false
    if (snakeLocation[lengthfunc - 1] > 6 || snakeLocation[lengthfunc - 2] > 16) {
        death = true
    }
    
    return death
}

while (true) {
    food()
    lengthfunc = snakeLocation.length
    snakeLocation = moveSnake(snakeLocation, direction, length)
    drawSnake(snakeLocation)
    for (let x2 = 0; x2 < 200; x2++) {
        if (ppFlag == false) {
            if (input.buttonIsPressed(Button.A)) {
                on_button_pressed_a()
                ppFlag = true
            }
            
            if (input.buttonIsPressed(Button.B)) {
                on_button_pressed_b()
                ppFlag = true
            }
            
        }
        
        basic.pause(1)
    }
    ppFlag = false
}
