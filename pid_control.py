
class PID:
    # Define the constructor
    def __init__(self, kp, ki, kd, dt = 0.1):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt

        # Initialize needed variables
        self.target = 0
        self.feedback = 0
        self.deadzone = 0

        # Variables to track errors and "integrate" them
        self.prev_error = 0
        self.integral = 0

        