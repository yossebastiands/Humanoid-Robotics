# Holzteller
# Panda movement
# From above, go to the table surface, pushes the plate to the side. 
# Go above again, start rotating, put the palm facing upwards below the plate.
# The Panda lifts up, then moves away for 20 cm, then it goes down again.

# Get the stuffs here
from dynamixel_port import *                           # communication with Dynamixel motors
import time                                            # handling time
dxl = DynamixelPort()                                   # Port to dynamixel motors
# This program is planned to work only for 1 motor

def initial_time():
    global t_start
    t_start=time.time()


# THE CONTROL PANEL -----------------------------------------------------------------
motor_ids = [1,2,3,4,5]                                # CHANGE THIS VALUE TO THE CORRESPONDING MOTOR!!!!!!!
# Every finger shall has its own value.
initial_velocity1 = 67                           # Left Thumb
initial_velocity2 = 42                             # Left Finger      
initial_velocity4 = -40                            # Middle Finger      
initial_velocity3 = -40                             # Right Finger      
initial_velocity5 = -60                             # Right Thumb      
magic_t = 4         # Time needed to grip
t_pause = 2       # Time needed to pause
t_pause1 = 1

# THE PROGRAM STARTS FROM BELOW -------------------------------------------
dxl.establish_connection(device_name = 'COM3')

dxl.set_operating_mode(motor_ids, VELOCITY_CONTROL_MODE)

time.sleep(33.5)
dxl.set_torque_enabled(motor_ids, True)
# Palmar abduction
dxl.set_goal_vel(motor_ids[0], initial_velocity1)
dxl.set_goal_vel(motor_ids[4], initial_velocity5)
time.sleep(magic_t)
dxl.set_goal_vel(motor_ids, 0)
# input("Press Enter to continue")
time.sleep(2)
# Three fingers grip
dxl.set_goal_vel(motor_ids[1], initial_velocity2)
dxl.set_goal_vel(motor_ids[2], initial_velocity3)
dxl.set_goal_vel(motor_ids[3], initial_velocity4)
time.sleep(magic_t)               
dxl.set_goal_vel(motor_ids, 0)

# input("Press Enter to release")
time.sleep(14.5)
# Release grip
dxl.set_goal_vel(motor_ids[0], -initial_velocity1)
dxl.set_goal_vel(motor_ids[1], -initial_velocity2)
dxl.set_goal_vel(motor_ids[2], -initial_velocity3)
dxl.set_goal_vel(motor_ids[3], -initial_velocity4)
dxl.set_goal_vel(motor_ids[4], -initial_velocity5)
time.sleep(magic_t)
dxl.set_goal_vel(motor_ids, 0)

dxl.set_torque_enabled(motor_ids, False)

dxl.disconnect() 