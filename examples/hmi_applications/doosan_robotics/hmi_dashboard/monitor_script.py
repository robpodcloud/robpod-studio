from DRCF import *
import random

test_running = False
out_status = [OFF]*6

drl_report_line(ON)

if "get_digital_output" not in globals():
    def get_digital_output(i):
        return out_status[i-1]


def test_controller():
    global test_running
    test_running = True

    while test_running:

        for i in range(1,7):
            set_digital_output(i, ON)
            out_status[i-1] = ON
            wait(0.5)

        for i in range(1,7):
            set_digital_output(i, OFF)
            out_status[i-1] = OFF
            wait(0.5)


def test_robot():
    global test_running
    test_running = True

    movej(posj(-89.7, -10.0, 105.7, 1.9, 84.3, -89.9), v=30, a=100)
    while test_running:
        movec(posx(41.2, -256.2, 249.7, 5.7, 178.3, 6.0), posx(51.9, -304.3, 70.1, 33.9, 178.5, 34.0), v=300, a=300, r=30)
        movec(posx(44.0, -451.5, 261.3, 22.2, 178.1, 22.4), posx(39.9, -294.4, 399.9, 0.2, 178.1, 0.2), v=300, a=300, r=30)


def test_joints():
    global test_running
    test_running = True

    movej(posj(-89.7, -10.0, 105.7, 1.9, 84.3, -89.9), v=30, a=100)
    amove_periodic([10, 45, 60, 10, 15, 10], [5, 3.5, 1.2, 6.5, 2.2, 2.1], repeat=100)
    while test_running:
        wait(1)
    stop(DR_QSTOP)


def test_task():
    global test_running
    test_running = True

    movej(posj(-89.7, -10.0, 105.7, 1.9, 84.3, -89.9), v=30, a=100)
    while test_running:
        movel(posx(52.4, -491.6, 40.4, 12.5, 180, 12.6), v=200, a=200)
        movel(posx(-60.8, -507.9, 504.8, 177.1, 90, 175.1), v=200, a=200)
        movej(posj(-89.7, -10.0, 105.7, 1.9, 84.3, -89.9), v=50, a=100)


