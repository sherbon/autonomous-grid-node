import time
import random
from signal_filter import MovingAverageFilter

TRIP_AMPS = 95          # shed above this current
RECOVER_AMPS = 80       # re-engage only if predicted load is below this
ROBOT_LINE_AMPS = 40    # assumed current drawn by the Priority 3 robot line
TICKS_TO_TRIP = 2       # raw readings in a row over TRIP_AMPS before shedding


def decide(smoothed_load, robot_line_active, ticks_over):
    """Return the new robot_line_active state."""
    if robot_line_active and smoothed_load > TRIP_AMPS and ticks_over >= TICKS_TO_TRIP:
        return False
    if not robot_line_active and smoothed_load + ROBOT_LINE_AMPS < RECOVER_AMPS:
        return True
    return robot_line_active


def run_automation_loop():
    print("=== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===")
    data_filter = MovingAverageFilter(window_size=3)
    robot_line_active = True
    ticks_over = 0

    for tick in range(1, 21):
        if 5 <= tick <= 10:
            raw_load = random.randint(115, 135)
        elif 11 <= tick <= 14:
            raw_load = random.choice([65, 130, 70, 125])
        else:
            raw_load = random.randint(65, 80)

        if not robot_line_active:
            raw_load -= ROBOT_LINE_AMPS

        # count consecutive raw readings over the limit (a lone spike resets next tick)
        if raw_load > TRIP_AMPS:
            ticks_over += 1
        else:
            ticks_over = 0

        smoothed_load = data_filter.filter_noise(raw_load)

        new_state = decide(smoothed_load, robot_line_active, ticks_over)
        message = None
        if robot_line_active and not new_state:
            message = " >> ALERT: Sustained current surge. Dropping Priority 3 systems!"
        elif not robot_line_active and new_state:
            message = " >> NOTICE: Predicted load is safe. Re-engaging hardware."
        robot_line_active = new_state

        status = "NOMINAL" if robot_line_active else "SHEDDING ACTIVE"
        print(f"[TICK {tick:02d}] Raw: {raw_load}A | Filtered: {smoothed_load:.1f}A | Grid State: {status}")
        if message:
            print(message)

        time.sleep(0.5)


if __name__ == "__main__":
    random.seed(1)
    run_automation_loop()