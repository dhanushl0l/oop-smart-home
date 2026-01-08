# Smart Device Control System

### Overview

This project simulates a smart home control system using Python. It demonstrates Object-Oriented Programming (OOP) concepts like inheritance and encapsulation. The system is designed to be scalable—meaning you can add new devices (like a TV or AC) easily without changing the existing controller logic.

### Steps to Set Up

You need Python 3 installed on your machine.

1. **Create a virtual environment:**
```bash
python -m venv .venv

```

2. **Activate the environment:**

* **Activate the environment (Linux/macOS, bash):**
```bash
source .venv/bin/activate

```

* **Windows:**
```cmd
.venv\Scripts\activate

```

### Instructions to Run

Once the environment is active, simply run the main driver script:

```bash
python main.py

```

**Alternative (Linux/macOS only):**
I have included a helper script that sets up the environment and runs the code in one step:

```bash
chmod +x setup.sh
./setup.sh

```

### Assumptions & Limitations

* **Simulation only:** Since there is no actual hardware, "Starting" a device just prints a confirmation message to the console.
* **State:** The device state (On/Off) is stored in memory and will reset every time you restart the program.
* **Safety:** The code is designed so that you cannot accidentally turn on a device that is already on (it handles duplicate commands gracefully).
