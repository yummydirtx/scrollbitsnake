let pp: number;
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
let rand2 = 0
let rand1 = 0
let direction = 0
//  cooper
let length = 1
let snakeLocation = [0, 0]
let dead = true
let firstPass = true
function drawSnake(snakeLocation: number[]) {
    //  clear the screen before drawing
    scrollbit.clear()
    //  repeat this for every pair of coordinates
    for (let x = 0; x < snakeLocation.length / 2; x++) {
        //  if x is length divided by two it has to be multiplied again
        scrollbit.setPixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1], 50)
    }
    scrollbit.setPixel(snakeLocation[snakeLocation.length - 2], snakeLocation[snakeLocation.length - 1])
    scrollbit.setPixel(rand2, rand1)
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


drawSnake(snakeLocation)
function checkContact(snakeLocation: number[]): boolean {
    let contact = false
    let frontX = snakeLocation[snakeLocation.length - 2]
    let frontY = snakeLocation[snakeLocation.length - 1]
    for (let x2 = 0; x2 < snakeLocation.length / 2 - 1; x2++) {
        if (frontX == snakeLocation[x2 * 2]) {
            if (frontY == snakeLocation[x2 * 2 + 1]) {
                contact = true
            }
            
        }
        
    }
    return contact
}

function checkDeath(snakeLocation: number[]): boolean {
    let death = checkContact(snakeLocation)
    if (snakeLocation[snakeLocation.length - 1] > 6 || snakeLocation[snakeLocation.length - 2] > 16) {
        death = true
    }
    
    if (snakeLocation[snakeLocation.length - 1] < 0 || snakeLocation[snakeLocation.length - 2] < 0) {
        death = true
    }
    
    return death
}

while (true) {
    if (!dead) {
        food(snakeLocation)
        snakeLocation = moveSnake(snakeLocation, direction, length)
        if (checkDeath(snakeLocation)) {
            direction = 0
            //  cooper
            length = 1
            rand1 = 0
            rand2 = 0
            snakeLocation = [0, 0]
            dead = true
            scrollbit.scrollText("GAME OVER", 100, 10)
        }
        
        drawSnake(snakeLocation)
        for (let index = 0; index < 200; index++) {
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
    } else {
        if (firstPass) {
            scrollbit.scrollText("MicroSnake", 100, 50)
            scrollbit.show()
            scrollbit.scrollText("Alex Frutkin and Cooper Weissman", 100, 20)
            scrollbit.show()
            firstPass = false
        }
        
        scrollbit.scrollText("PRESS ANY BUTTON", 100, 20)
        for (pp = 0; pp < 1000; pp++) {
            if (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
                dead = false
                pp = 1000
            }
            
            basic.pause(1)
        }
    }
    
}
