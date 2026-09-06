# Simple simulation for the PID controller
from pid_control import PID


def main():

    # Define the Gains
    kp = 1.0
    ki = 0.1
    kd = 0.4

    # Initialize simulation settings
    # Change in time (time interval)
    dt = 0.1
    target = 10.0
    current_state = 0

    # Create PID instance
    pid = PID(kp, ki, kd, dt)
    







if __name__ == "__main__":
    main()