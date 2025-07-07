input.onButtonPressed(Button.A, function () {
    if (playerX > 0) {
        playerX += -1
    }
})
input.onButtonPressed(Button.B, function () {
    if (playerX < 4) {
        playerX += 1
    }
})
let score = 0
let ballY = 0
let playerX = 0
let ballX = 0
playerX = 2
basic.forever(function () {
    basic.clearScreen()
    ballY += 1
    if (ballY == 5) {
        ballY = 0
        ballX = Math.randomRange(0, 4)
    }
    led.plot(ballX, ballY)
    led.plot(playerX, 4)
    if (ballY == 4 && ballX == playerX) {
        score += 1
        basic.showNumber(score)
    }
    basic.pause(500)
})
