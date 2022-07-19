# Milchbrot

# Get the stuffs here
from dynamixel_port import *                           # communication with Dynamixel motors
import time                                            # handling time
dxl = DynamixelPort()                                   # Port to dynamixel motors

def initial_time():
    global t_start
    t_start=time.time()


# THE CONTROL PANEL -----------------------------------------------------------------
motor_ids = [1,2,3,4,5]                                # CHANGE THIS VALUE TO THE CORRESPONDING MOTOR!!!!!!!
# ================= BELOW IS ALLOWED TO CHANGE ====================
# Every finger shall has its own value.
initial_velocity1 = 52                           # Left Thumb
initial_velocity2 = 27                             # Left Finger      
initial_velocity4 = -22.5                            # Middle Finger      
initial_velocity3 = -27                             # Right Finger      
initial_velocity5 = -49                             # Right Thumb 
# ================= END OF EDITABLE CODE ==========================
#      
magic_t = 4         # Time needed to grip
t_pause = 2       # Time needed to pause

# THE PROGRAM STARTS FROM BELOW -------------------------------------------
dxl.establish_connection(device_name = 'COM3')
dxl.set_operating_mode(motor_ids, VELOCITY_CONTROL_MODE)
dxl.set_torque_enabled(motor_ids, True)


# --------------------------------------------------------------------------

# ==================== YOU CAN CHANGE THIS =======================
input("Press Enter to grasp")
time.sleep(25)   # The 13th second is the time it starts grabbing the bread
# ===================== DON'T CHANGE BELOW =======================

# Three fingers start grabbing
dxl.set_goal_vel(motor_ids[1], initial_velocity2)
dxl.set_goal_vel(motor_ids[2], initial_velocity3)
dxl.set_goal_vel(motor_ids[3], initial_velocity4)
time.sleep(magic_t)
dxl.set_goal_vel(motor_ids, 0)  # They stop

# ========================== YOU CAN CHANGE THIS =====================

# input("Press Enter to continue")
time.sleep(16)

# DON'T CHANGE BELOW =================================================

# Two thumbs start grabbing
dxl.set_goal_vel(motor_ids[0], initial_velocity1)
dxl.set_goal_vel(motor_ids[4], initial_velocity5)
time.sleep(magic_t)      
dxl.set_goal_vel(motor_ids, 0)

# ========================== YOU CAN CHANGE THIS ===================== 

# input("Press Enter to release")
time.sleep(18)

# DON'T CHANGE BELOW =================================================

# Release the grab
dxl.set_goal_vel(motor_ids[0], -initial_velocity1)
dxl.set_goal_vel(motor_ids[1], -initial_velocity2)
dxl.set_goal_vel(motor_ids[2], -initial_velocity3)
dxl.set_goal_vel(motor_ids[3], -initial_velocity4)
dxl.set_goal_vel(motor_ids[4], -initial_velocity5)
time.sleep(magic_t)
dxl.set_goal_vel(motor_ids, 0)


dxl.set_torque_enabled(motor_ids, False)

dxl.disconnect()