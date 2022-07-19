# Toast

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
initial_velocity1 = 43                           # Left Thumb
initial_velocity2 = 25                             # Left Finger      
initial_velocity4 = -21                            # Middle Finger      
initial_velocity3 = -25                             # Right Finger      
initial_velocity5 = -43                             # Right Thumb      
magic_t = 4         # Time needed to grip
t_pause = 2       # Time needed to pause
t_pause1 = 1

# THE PROGRAM STARTS FROM BELOW -------------------------------------------
dxl.establish_connection(device_name = 'COM3')

dxl.set_operating_mode(motor_ids, VELOCITY_CONTROL_MODE)


dxl.set_torque_enabled(motor_ids, True)
time.sleep(17)
dxl.set_goal_vel(motor_ids[0], initial_velocity1)
dxl.set_goal_vel(motor_ids[4], initial_velocity5)
time.sleep(magic_t)
dxl.set_goal_vel(motor_ids[0], 0)
dxl.set_goal_vel(motor_ids[4], 0)
time.sleep(1)
dxl.set_goal_vel(motor_ids[1], initial_velocity2)
dxl.set_goal_vel(motor_ids[2], initial_velocity3)
dxl.set_goal_vel(motor_ids[3], initial_velocity4)
time.sleep(magic_t)               
dxl.set_goal_vel(motor_ids, 0)
# input("Press Enter to tighten")
time.sleep(2.5)
dxl.set_goal_vel(motor_ids[0], initial_velocity1)
dxl.set_goal_vel(motor_ids[4], initial_velocity5)
time.sleep(t_pause1)
dxl.set_goal_vel(motor_ids[0], 0)
dxl.set_goal_vel(motor_ids[4], 0)
# input("Press Enter to release")
time.sleep(13.5)
dxl.set_goal_vel(motor_ids[0], -initial_velocity1)
dxl.set_goal_vel(motor_ids[1], -initial_velocity2)
dxl.set_goal_vel(motor_ids[2], -initial_velocity3)
dxl.set_goal_vel(motor_ids[3], -initial_velocity4)
dxl.set_goal_vel(motor_ids[4], -initial_velocity5)
time.sleep(magic_t)
dxl.set_goal_vel(motor_ids, 0)
dxl.set_goal_vel(motor_ids[0], -initial_velocity1)
dxl.set_goal_vel(motor_ids[4], -initial_velocity5)
time.sleep(t_pause1)
dxl.set_goal_vel(motor_ids[0], 0)
dxl.set_goal_vel(motor_ids[4], 0)

dxl.set_torque_enabled(motor_ids, False)

dxl.disconnect() 