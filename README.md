# Keylogger Project

## Overview
This project implements a basic **keylogger** using Python's `pynput` library. A keylogger is a program designed to record every keystroke made by a user. This keylogger captures both alphanumeric and special keys, writes them to a log file, and prints them to the console in real-time.

> **Disclaimer:** This project is intended for educational purposes only. Unauthorized use of a keylogger is illegal and unethical. Always obtain explicit consent from users before monitoring their devices.

---

## Features
- Records both alphanumeric and special keys (e.g., `Enter`, `Space`, `Backspace`).
- Logs the keystrokes to a file (`log.txt`) in an organized manner.
- Prints the keystrokes to the console for real-time monitoring.
- Handles keypress and key release events.

---

## How It Works
1. **Key Press Handling**:
   - Alphanumeric keys are logged directly.
   - Special keys like `Space` and `Enter` are handled with readable labels (e.g., spaces and newline characters).
   - The pressed key is added to a list and written to a log file.
2. **Key Release Handling**:
   - Displays the released key in the console.
   - Stops the keylogger when the `Esc` key is released.
3. **Log File**:
   - All captured keys are saved in `log.txt`.
   - Handles formatting for special keys for better readability.

---

## File Descriptions
- `keylogger.py`: The main script containing the keylogger implementation.
- `log.txt`: The output file where captured keystrokes are stored.

---

## Code Explanation

### Dependencies
- `pynput`: Used to monitor and control keyboard input.

Install `pynput` using pip:
```bash
pip install pynput
```

### Key Functions
#### `on_press(key)`
- Captures and processes every key pressed.
- Appends the key to a list.
- Writes the key(s) to `log.txt`.

#### `write_file(keys)`
- Writes the captured keys to a log file.
- Formats special keys (e.g., spaces, backspaces) for readability.

#### `on_release(key)`
- Prints the released key to the console.
- Stops the keylogger when the `Esc` key is released.

---

## Usage
1. Clone or download the project files.
2. Run the script:
   ```bash
   python keylogger.py
   ```
3. Press keys on your keyboard, and observe the following:
   - Key presses are printed in the console.
   - All keystrokes are logged in the `log.txt` file.
4. To stop the keylogger, press the `Esc` key.

---

## Sample Output
### Console Output:
```
Alphanumeric key a pressed
Alphanumeric key b pressed
Special key Key.space pressed
Key.space released
```

### Log File (`log.txt`):
```
ab [space]
```

---

## Ethical Considerations
Keyloggers should only be used in the following scenarios:
- **Self-monitoring**: To monitor your own typing habits or for debugging purposes.
- **Authorized Use**: When explicit consent is given by the user.

**Never use keyloggers for malicious purposes such as stealing personal information.** Always follow ethical guidelines and local laws.

---

## References
- [Pynput Documentation](https://pynput.readthedocs.io/en/latest/)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Author
Developed by Dhatsheth Roshan.A.

