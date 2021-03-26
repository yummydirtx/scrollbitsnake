// cooper
let length = 2
let direction = 0
let snakeLocation = [0, 0]
function drawSnake(snakeLocation: number[]) {
    for (let x = 0; x < snakeLocation.length / 2; x++) {
        scrollbit.setPixel(snakeLocation[x * 2], snakeLocation[x * 2 + 1])
    }
    scrollbit.show()
}

drawSnake(snakeLocation)
