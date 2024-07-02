let Light = 0
radio.setGroup(216)
pins.digitalWritePin(DigitalPin.P0, 0)
pins.digitalWritePin(DigitalPin.P1, 0)
loops.everyInterval(500, function () {
    if (Light % 2 == 0) {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    Light += 1
})
loops.everyInterval(2000, function () {
    radio.sendNumber(input.temperature())
    radio.sendNumber(input.lightLevel())
    radio.sendNumber(input.compassHeading())
    radio.sendNumber(input.soundLevel())
})
