import time
import random
from signal_filter import MovingAverageFilter

def run_automation_loop():
    print("=== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===")
    data_filter = MovingAverageFilter(window_size=3)
    robot_line_active = True

    # Simulate an active 6-second physical operational window
    for tick in range(1, 7):
        # Ticks 3 & 4 simulate a heavy physical inrush current voltage surge
        raw_load = random.randint(115, 130) if tick in [3, 4] else random.randint(65, 80)
        smoothed_load = data_filter.filter_noise(raw_load)
        
        print(f"[TICK {tick}] Raw Current: {raw_load}A | Filtered Bus Load: {smoothed_load:.1f}A")
        
        # Priority 3 Load Shedding Check
        if smoothed_load > 95 and robot_line_active:
            print(" >> WARNING: Current threshold breached. Isolating secondary systems!")
            robot_line_active = False
        elif smoothed_load < 80 and not robot_line_active:
            print(" >> NOTICE: Bus voltage stabilized. Safely re-engaging hardware.")
            robot_line_active = True
            
        time.sleep(1)

if __name__ == "__main__":
    run_automation_loop()
