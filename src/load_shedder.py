import time
import random
from signal_filter import MovingAverageFilter

def run_automation_loop():
    print("=== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===")
    data_filter = MovingAverageFilter(window_size=3)
    robot_line_active = True

    # 1. Expand the timeline to 20 operational ticks
    for tick in range(1, 21):
        
        # 2. Program a realistic, prolonged physical grid timeline
        if 5 <= tick <= 10:
            # Ticks 5-10 simulate a massive, sustained synchronized motor surge
            raw_load = random.randint(115, 135)
        elif 11 <= tick <= 14:
            # Ticks 11-14 simulate a dangerous high-frequency flickering current
            raw_load = random.choice([65, 130, 70, 125])
        else:
            # All other ticks simulate stable, baseline factory operation
            raw_load = random.randint(65, 80)
            
        smoothed_load = data_filter.filter_noise(raw_load)
        
        # Format a clean system telemetry log layout
        status = "NOMINAL" if robot_line_active else "SHEDDING ACTIVE"
        print(f"[TICK {tick:02d}] Raw: {raw_load}A | Filtered: {smoothed_load:.1f}A | Grid State: {status}")
        
        # 3. Dynamic Priority 3 Load Shedding Check
        if smoothed_load > 95 and robot_line_active:
            print(" >> ALERT: Sustained current surge detected. Dropping Priority 3 systems!")
            robot_line_active = False
            
        # 4. Automated Recovery Check (Ensures the grid safely cools down)
        elif smoothed_load < 80 and not robot_line_active:
            print(" >> NOTICE: Bus load stabilized below safety threshold. Re-engaging hardware.")
            robot_line_active = True
            
        time.sleep(0.5) # Fast 0.5s clock step for a smoother mobile console view

if __name__ == "__main__":
    run_automation_loop()
