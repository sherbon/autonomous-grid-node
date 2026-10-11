import time
import random
from signal_filter import MovingAverageFilter

TRIP_AMPS = 95          # shed above this filtered current
RECOVER_AMPS = 80       # re-engage only if predicted load is below this
ROBOT_LINE_AMPS = 40    # assumed current drawn by the Priority 3 robot line

def run_automation_loop():
    print("=== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===")
    data_filter = MovingAverageFilter(window_size=3)
    robot_line_active = True

    for tick in range(1, 21):
        if 5 <= tick <= 10:
            raw_load = random.randint(115, 135)
        elif 11 <= tick <= 14:
            raw_load = random.choice([65, 130, 70, 125])
        else:
            raw_load = random.randint(65, 80)

        # CLOSED LOOP: shedding really removes the robot line's current
        if not robot_line_active:
            raw_load -= ROBOT_LINE_AMPS

        smoothed_load = data_filter.filter_noise(raw_load)

        # Decide first, print after, so the status matches the numbers
        message = None
        if smoothed_load > TRIP_AMPS and robot_line_active:
            robot_line_active = False
            message = " >> ALERT: Current surge detected. Dropping Priority 3 systems!"
        elif not robot_line_active and smoothed_load + ROBOT_LINE_AMPS < RECOVER_AMPS:
            robot_line_active = True
            message = " >> NOTICE: Predicted load is safe. Re-engaging hardware."

        status = "NOMINAL" if robot_line_active else "SHEDDING ACTIVE"
        print(f"[TICK {tick:02d}] Raw: {raw_load}A | Filtered: {smoothed_load:.1f}A | Grid State: {status}")
        if message:
            print(message)

        time.sleep(0.5)

if __name__ == "__main__":
    random.seed(1)   # same numbers every run, so your README log can be reproduced
    run_automation_loop()
