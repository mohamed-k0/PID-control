# Simple simulation for the PID controller
from pid_control import PID


def main():

    # Define the Gains
    kp = 4.03
    ki = 0.081
    kd = 0.7

    # Initialize simulation settings
    dt = 0.1 # Change in time
    target = 30.0
    current_state = 0
    deadzone = 0.01

    # Create PID instance
    pid = PID(kp, ki, kd, dt)

    # Set the target and deadzone values
    pid.set_target(target)
    pid.set_deadzone(deadzone)

    # Loop
    STEPS = 100
    for step in range(STEPS):

        # Give feedback to the controller
        pid.update_feedback(current_state)

        # Compute the control signal (output)
        output = pid.compute()

        # Apply Physics to mimic mechanical movement
        current_state += output * dt

        # Calculate the error after movement (for display)
        error = target - current_state

        # Print Telemetry
        print(f"""Loop: {step}
Error: {error:.3f}
PID Output: {output:.3f}
Updated State: {current_state:.3f}
------------------------------"""
)


if __name__ == "__main__":
    main()