# ⚡ Autonomous Grid Node

`🔧 Python 3` • `🧠 Simulation` • `🧪 pytest`

A Python simulation of an overcurrent protection loop. It smooths noisy current readings with a moving-average filter and sheds a low-priority load during sustained surges. Shedding reduces the simulated current, and the load is re-engaged only when the predicted load is safe.

---

## 📺 Example Output
Output of `python src/load_shedder.py` (random seed 1): 

```text
=== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===
[TICK 01] Raw: 69A | Filtered: 69.0A | Grid State: NOMINAL
[TICK 02] Raw: 67A | Filtered: 68.0A | Grid State: NOMINAL
[TICK 03] Raw: 73A | Filtered: 69.7A | Grid State: NOMINAL
[TICK 04] Raw: 68A | Filtered: 69.3A | Grid State: NOMINAL
[TICK 05] Raw: 130A | Filtered: 90.3A | Grid State: NOMINAL
[TICK 06] Raw: 129A | Filtered: 109.0A | Grid State: SHEDDING ACTIVE
 >> ALERT: Sustained current surge. Dropping Priority 3 systems!
[TICK 07] Raw: 90A | Filtered: 116.3A | Grid State: SHEDDING ACTIVE
[TICK 08] Raw: 95A | Filtered: 104.7A | Grid State: SHEDDING ACTIVE
[TICK 09] Raw: 87A | Filtered: 90.7A | Grid State: SHEDDING ACTIVE
[TICK 10] Raw: 81A | Filtered: 87.7A | Grid State: SHEDDING ACTIVE
[TICK 11] Raw: 25A | Filtered: 64.3A | Grid State: SHEDDING ACTIVE
[TICK 12] Raw: 85A | Filtered: 63.7A | Grid State: SHEDDING ACTIVE
[TICK 13] Raw: 25A | Filtered: 45.0A | Grid State: SHEDDING ACTIVE
[TICK 14] Raw: 85A | Filtered: 65.0A | Grid State: SHEDDING ACTIVE
[TICK 15] Raw: 38A | Filtered: 49.3A | Grid State: SHEDDING ACTIVE
[TICK 16] Raw: 25A | Filtered: 49.3A | Grid State: SHEDDING ACTIVE
[TICK 17] Raw: 39A | Filtered: 34.0A | Grid State: NOMINAL
 >> NOTICE: Predicted load is safe. Re-engaging hardware.
[TICK 18] Raw: 73A | Filtered: 45.7A | Grid State: NOMINAL
[TICK 19] Raw: 72A | Filtered: 61.3A | Grid State: NOMINAL
[TICK 20] Raw: 68A | Filtered: 71.0A | Grid State: NOMINAL
```

---

## ⚙️ How It Works

- Each tick, the current reading is smoothed with a 3-reading moving average.
- **Shed** the robot line when the filtered current is above 95 A *and* two raw readings in a row are above 95 A (so a single spike doesn't trigger it).
- Shedding removes 40 A (the assumed robot-line current) from the simulated readings.
- **Re-engage** only when the filtered current plus 40 A is below 80 A, meaning the load would still be safe with the robot line back.
- The filtered value lags the raw readings by up to 2 ticks after a sudden change.

---

## 🛠️ The Physics Problem 

When a motor starts from standstill, it has no back-EMF (the voltage a spinning motor generates against its supply). With nothing opposing the supply voltage, only the winding's own resistance limits the current, so it spikes to several times its running value:

> **I = V / R**
*(I is current in amperes, V is voltage, R is the winding resistance)*

That surge also flows through the supply and wiring, which have resistance too, so the bus voltage sags (ΔV = I × R_source).

The surge heats wires and windings. Power lost as heat is:

> **P = I² × R**
*(P is power lost as heat in watts)*

If the current doubles, the heating quadruples.

This simulation demonstrates how software could shed low-priority loads during a current surge, reducing stress on hardware protection such as fuses and breakers.

*This is a software simulation with simulated current readings. It is not safety-rated and does not replace hardware protection.*

---

## 🧱 Code Structure

<details>
<summary>📂 View Project Directory Map (Click to Expand)</summary>

*   **`src/signal_filter.py`**: Moving-average filter over the last 3 readings to smooth sensor noise.
*   **`src/load_shedder.py`**: Runs the 20-tick simulation. Shedding reduces the simulated current, and the load is re-engaged only if the predicted load is safe.
*   **`tests/test_load_shedder.py`**: automated tests for the shedding decision and the filter.
*   **`.gitignore`**: Ignores `__pycache__/`, `.pytest_cache/` and `output.txt`.
*   **`LICENSE`**: **MIT License**
*   **`pytest.ini`**: tells pytest where to find the source code.
</details>

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/sherbon/autonomous-grid-node
cd autonomous-grid-node
```

### 2. Run the simulation
Requires Python 3. The run takes about 10 seconds (0.5 s per tick).
```bash
python src/load_shedder.py
```
On Windows, use `py` instead of `python` if `python` isn't recognised.

### 3. Run the tests
```bash
pip install pytest
python -m pytest
```