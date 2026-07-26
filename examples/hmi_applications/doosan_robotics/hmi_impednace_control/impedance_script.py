from DRCF import *

# impedance control gains
Kp = 50
Kd = 40

running = False


# impedance control function
def start_task():
    global running

    # setup compliance parameters
    stiffness = [Kp*200, Kp*200, Kp*200, Kp*4, Kp*4, 400]
    damping = [max(0.1, Kd*0.02), max(0.1, Kd*0.02), max(0.1, Kd*0.02), max(0.1, Kd*0.02), max(0.1, Kd*0.02), 1]

    # home position
    movej(posj(90, 0, -90, 0, -90, -85.0), v=30, a=100)
    set_external_force_reset()

    # start impedance control
    task_compliance_ctrl(stx=stiffness)
    set_damping_factor(damping)

    # wait for user to stop impedance control
    running = True
    while running:
        wait(1)

    # resume position control
    release_compliance_ctrl()



