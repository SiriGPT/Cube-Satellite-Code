Light = 0
radio.set_group(216)
pins.digital_write_pin(DigitalPin.P0, 0)
pins.digital_write_pin(DigitalPin.P1, 0)

def on_every_interval():
    global Light
    if Light % 2 == 0:
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
    Light += 1
loops.every_interval(500, on_every_interval)

def on_every_interval2():
    radio.send_number(input.temperature())
    radio.send_number(input.light_level())
    radio.send_number(input.compass_heading())
    radio.send_number(input.sound_level())
loops.every_interval(2000, on_every_interval2)
