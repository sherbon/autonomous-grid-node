# ⚡ Autonomous Grid Telemetry Node

`🔧 Engine: Python 3` • `🧠 Domain: Systems Automation` • `🧱 Stack: Modular Edge`

A deterministic mechatronics control loop engineered to mitigate systemic hardware overcurrent events (I²R Joule heating) and voltage sags through automated priority load shedding.

---

## 📺 Example Output
Output of python src/load_shedder.py (random seed 1):
```text
== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===
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

## 🛠️ The Physics Problem Space

When heavy industrial actuators or grid inverters switch on from a zero-spin state, their static inertia creates near-zero initial internal resistance (R → 0). According to **Ohm's Law**, this drops systemic bus voltage and spikes electric current lines:

> **I = V / R**  
*(Where I represents Current in Amperes, V is Voltage, and R is Resistance)*

Left unchecked, heat energy generated within copper circuit board traces grows exponentially via **Joule Heating**, where power loss scales with the square of the current load:

> **P = I² × R**  
*(Where P represents Power lost as heat in Watts)*

This system acts as a digital barrier against physical thermal breakdowns and voltage sag faults by implementing algorithmic priority overrides before analog fuses or breakers trip.

---

## 🧱 Code Architecture

<details>
<summary>📂 View Project Directory Map (Click to Expand)</summary>

*   **`src/signal_filter.py`**: A specialized low-pass filtering object utilizing a 3-tick window array to calculate rolling mathematical trends and suppress physical sensor circuit wire noise.
*   **`src/load_shedder.py`**: The executive 20-tick monitoring state-machine tracking deterministic grid threshold variations and recovery thresholds.
*   **`tests/test_load_shedder.py`**: automated tests for the shedding decision and the filter.
*   **`.gitignore`**: Global environment safety config explicitly blocking machine cache noise footprints (`__pycache__/`) from polluting the workspace tree structure.
*   **`LICENSE`**: Licensed under the universally standard open-source **MIT License** layout.
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