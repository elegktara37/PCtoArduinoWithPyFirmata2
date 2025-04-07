# Arduino LCD Screen Messages with Python GUI
This project demonstrates how to send messages to an LCD connected to an Arduino board using Python's PyFirmata2 library and a very basic graphical user interface (GUI) built with Tkinter (Tk). It allows users to send messages from the PC to the Arduinos LCD.

## Prerequisites

* **Arduino IDE:** Installed and configured.
* **Arduino Board:** Connected to your computer.
* **Python 3.x:** Installed.
* **PyFirmata2:** Install using `pip install pyfirmata2` (https://pypi.org/project/pyFirmata2/).
* **Tkinter (Tk):** Install using `pip install tkinter`.

## Hardware Setup

1.  Connect the LCD to your Arduino board as shown below.
2.  Connect the Arduino board to your computer via USB.

Circuit Diagram
Here's the circuit diagram for this project:

![Schematic](https://github.com/user-attachments/assets/5678e1b1-c4d0-4689-9f2b-747a4cadaf6e)
          
## Software Setup

1.  **Upload pyfirmata.ino:**
    * Open the Arduino IDE.
    * Go to `File > Open > pyfirmata.ino`.
    * Upload the sketch to your Arduino board.

2.  **Run the Python Script:**
    * Save the Python code (e.g., `ArduinoController.py`) in a directory.
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the script.
    * Run the script using `python ArduinoController.py`.

## Installation Instructions

1.  **Install Python:**
    * Ensure you have Python 3.x installed on your system.
    * If not, download it from python.org and follow the installation instructions.

2.  **Install PyFirmata2:**
    * Open a terminal or command prompt.
    * Run the following command:
        ```bash
        pip install pyfirmata2
        ```

3.  **Install Tkinter (Tk):**
    * In the same terminal, run:
        ```bash
        pip install tkinter
        ```
## Code Explanation

* **PyFirmata2:** Establishes communication with the Arduino board and controls the LED pins using PWM.
* **Tkinter (CTk):** Creates the GUI with two buttons to send the messages.
* **`displayFirstName()`:** Function which sends as message the First Name.
* **`displayLastName()`:** Function which sends as message the Last Name.

## How to Use

1.  **Set Port Number:**
    * Modify the `port` variable in the script to match your Arduino's serial port (e.g., "COM3", "/dev/ttyACM0").

2.  **Run the Script:**
    * Execute the Python script.
    * A GUI window will appear.

3.  **Send Messagess:**
    * Click "Send First Name" to send and display the First Name of the LCD.
    * Click "Send Last Name" to send and display the Last Name of the LCD.


## Photos

![image](https://github.com/user-attachments/assets/2895d503-734d-4f55-b547-d42a744c1455)

![IMG_20250407_100626(1)](https://github.com/user-attachments/assets/9cf998f7-66d0-4ffb-9da5-7cf59d4295fa)

