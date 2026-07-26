from DRCF import *

color = "green"

def rainbow():
    global color

    for i in range(5):

        # red
        set_state_led_color(1, 0, 0)
        color = "red"
        wait(0.4)

        # yellow
        set_state_led_color(1,1,0)
        color = "yellow"
        wait(0.4)

        # green
        set_state_led_color(0,1,0)
        color = "green"
        wait(0.4)

        # cyan
        set_state_led_color(0,1,1)
        color = "cyan"
        wait(0.4)

        # blue
        set_state_led_color(0,0,1)
        color = "blue"
        wait(0.4)

        # magenta
        set_state_led_color(1,0,1)
        color = "magenta"
        wait(0.4)