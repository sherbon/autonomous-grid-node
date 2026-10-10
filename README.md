# ⚡ Autonomous Grid Telemetry Node

<p align="left">
  <img src="https://shields.io" alt="Python">
  <img src="https://shields.io" alt="Automation">
  <img src="https://shields.io" alt="Architecture">
</p>

A deterministic mechatronics control loop engineered to mitigate systemic hardware overcurrent events (I²R Joule heating) and voltage sags through automated priority load shedding.

---

## 📺 Live System Execution Proof

```text
=== SHATLER POWER INFRASTRUCTURE INTERFACE ONLINE ===
[TICK 01] Raw: 68A | Filtered: 68.0A | Grid State: NOMINAL
[TICK 02] Raw: 65A | Filtered: 66.5A | Grid State: NOMINAL
[TICK 03] Raw: 73A | Filtered: 68.7A | Grid State: NOMINAL
[TICK 04] Raw: 72A | Filtered: 70.0A | Grid State: NOMINAL
[TICK 05] Raw: 122A | Filtered: 89.0A | Grid State: NOMINAL
[TICK 06] Raw: 119A | Filtered: 104.3A | Grid State: NOMINAL
 >> ALERT: Sustained current surge detected. Dropping Priority 3 systems!
[TICK 07] Raw: 118A | Filtered: 119.7A | Grid State: SHEDDING ACTIVE
[TICK 08] Raw: 132A | Filtered: 123.0A | Grid State: SHEDDING ACTIVE
[TICK 09] Raw: 117A | Filtered: 122.3A | Grid State: SHEDDING ACTIVE
[TICK 10] Raw: 133A | Filtered: 127.3A | Grid State: SHEDDING ACTIVE
[TICK 11] Raw: 125A | Filtered: 125.0A | Grid State: SHEDDING ACTIVE
[TICK 12] Raw: 70A | Filtered: 109.3A | Grid State: SHEDDING ACTIVE
[TICK 13] Raw: 70A | Filtered: 88.3A | Grid State: SHEDDING ACTIVE
[TICK 14] Raw: 70A | Filtered: 70.0A | Grid State: SHEDDING ACTIVE
 >> NOTICE: Bus load stabilized below safety threshold. Re-engaging hardware.
[TICK 15] Raw: 71A | Filtered: 70.3A | Grid State: NOMINAL
[TICK 16] Raw: 72A | Filtered: 71.0A | Grid State: NOMINAL
```

---

## 🛠️ The Physics Problem Space

When heavy industrial actuators or grid inverters switch on from a zero-spin state, their static inertia creates near-zero initial internal resistance (R → 0). According to **Ohm's Law**, this drops systemic bus voltage and spikes electric current lines:

\[I = \frac{V}{R}\]

Left unchecked, heat energy generated within copper circuit board traces grows exponentially via **Joule Heating**, where power loss scales with the square of the current load:

\[P = I^2 \times R\]

This system acts as a digital barrier against physical thermal breakdowns and voltage sag faults by implementing algorithmic priority overrides before analog fuses or breakers trip.

---

## 🧱 Production Code Architecture

<details>
<summary>📂 View Project Directory Map (Click to Expand)</summary>

*   **`src/signal_filter.py`**: A specialized low-pass filtering object utilizing a 3-tick window array to calculate rolling mathematical trends and suppress physical sensor circuit wire noise.
*   **`src/load_shedder.py`**: The executive 20-tick monitoring state-machine tracking deterministic grid threshold variations and recovery thresholds.
*   **`.gitignore`**: Global environment safety config explicitly blocking machine cache noise footprints (`__pycache__/`) from polluting the workspace tree structure.
*   **`LICENSE`**: Licensed under the universally standard open-source **MIT License** layout.

</details>

---

## 🚀 How to Run Locally

### 1. Clone the environment
```bash
git clone https://github.com
cd autonomous-grid-node
```

### 2. Execute the Control Loop Node
Ensure you have Python 3 installed locally, then launch the core system driver:
```bash
python src/load_shedder.py
```
