
class PID:

    # Define the constructor
    def __init__(self, kp, ki, kd, dt = 0.1):
        # Gains of P, I, D
        self.kp = kp
        self.ki = ki
        self.kd = kd
        # Set the time interval default as "0.1 seconds"
        self.dt = dt 

        # Initialize needed variables
        self.target = 0
        self.feedback = 0
        self.deadzone = 0

        # Variables to track errors and "integrate/derive" them
        self.prev_error = 0
        self.integral = 0

    # Method to set the target
    def set_target(self, target):
        self.target = target

    # Update the feedback to the controller (current value)
    def update_feedback(self, feedback):
        self.feedback = feedback

    # Compute method
    def compute(self):
        # Calculate the error 
        error = self.target - self.feedback

        # Calculate proportional action
        P = self.kp * error

        # Integral action
        # Estimate the integral of errors (sum tends to infinity)
        self.integral += error * self.dt
        I = self.ki * self.integral

        # Derivative action 
        # Calculate the derivative (Slope)
        derivative = (error - self.prev_error) / self.dt
        D = self.kd * derivative

        # Store the previous error for utilization
        self.prev_error = error
